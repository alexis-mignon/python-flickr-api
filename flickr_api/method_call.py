"""
method_call module.

This module is used to perform the calls to the REST interface.

Author: Alexis Mignon (c)
e-mail: alexis.mignon@gmail.com
Date: 06/08/2011

"""

import time
import urllib.parse
import urllib.request
import urllib.error
import requests
import hashlib
import logging
from typing import Any

from . import keys
from .utils import urlopen_and_read
from .flickrerrors import (
    FlickrAPIError,
    FlickrError,
    FlickrServerError,
)
from . import retry as retry_module
from .cache import SimpleCache

REST_URL = "https://api.flickr.com/services/rest/"

CACHE = None

IGNORED_FIELDS = set(["oauth_nonce", "oauth_timestamp", "oauth_signature"])

logger = logging.getLogger(__name__)

# Rate limit retry configuration
MAX_RETRIES: int = 3
RETRY_BASE_DELAY: float = 1.0  # Base delay in seconds for exponential backoff
RETRY_MAX_DELAY: float = 60.0  # Maximum delay between retries

# Proactive rate limiting configuration
_RATE_LIMIT_REQUESTS_PER_HOUR: float | None = None
_RATE_LIMIT_LAST_REQUEST: float | None = None


# Initialize retry module with our config getters
def _init_retry_module() -> None:
    """Initialize retry module with config getters."""
    retry_module.set_retry_config_getter(get_retry_config)
    retry_module.set_rate_limit_wait_func(_maybe_wait_for_rate_limit)


def enable_cache(cache_object: Any | None = None) -> None:
    """enable caching
    Parameters:
    -----------
    cache_object: object, optional
        A Django compliant cache object. If None (default), a SimpleCache
        object is used.
    """
    global CACHE
    CACHE = cache_object if cache_object is not None else SimpleCache()


def disable_cache() -> None:
    """Disable cachine capabilities"""
    global CACHE
    CACHE = None


# See requests package documentation for timeout usage details.
# https://requests.readthedocs.io/en/latest/user/quickstart/#timeouts
TIMEOUT: float = 10


def set_timeout(seconds: float) -> None:
    """Set timeout in seconds for requests calls"""
    global TIMEOUT
    TIMEOUT = seconds


def get_timeout() -> float:
    return TIMEOUT


def set_retry_config(
    max_retries: int | None = None,
    base_delay: float | None = None,
    max_delay: float | None = None,
) -> None:
    """Configure rate limit retry behavior.

    Parameters:
    -----------
    max_retries: int, optional
        Maximum number of retries on rate limit (default 3). Set to 0 to disable.
    base_delay: float, optional
        Base delay in seconds for exponential backoff (default 1.0)
    max_delay: float, optional
        Maximum delay between retries in seconds (default 60.0)
    """
    global MAX_RETRIES, RETRY_BASE_DELAY, RETRY_MAX_DELAY
    if max_retries is not None:
        MAX_RETRIES = max_retries
    if base_delay is not None:
        RETRY_BASE_DELAY = base_delay
    if max_delay is not None:
        RETRY_MAX_DELAY = max_delay


def get_retry_config() -> dict[str, Any]:
    """Get current retry configuration.

    Returns:
    --------
    dict with keys: max_retries, base_delay, max_delay
    """
    return {
        "max_retries": MAX_RETRIES,
        "base_delay": RETRY_BASE_DELAY,
        "max_delay": RETRY_MAX_DELAY,
    }


def set_rate_limit(requests_per_hour: float | None) -> None:
    """Enable or disable proactive rate limiting.

    Parameters:
    -----------
    requests_per_hour: float | None
        Maximum requests per hour. Set to None to disable rate limiting.
        Flickr's documented limit is 3600 requests per hour.

    Raises:
    -------
    ValueError: If requests_per_hour is not positive (zero or negative).
    """
    if requests_per_hour is not None and requests_per_hour <= 0:
        raise ValueError("requests_per_hour must be positive")
    global _RATE_LIMIT_REQUESTS_PER_HOUR
    _RATE_LIMIT_REQUESTS_PER_HOUR = requests_per_hour


def get_rate_limit() -> dict[str, float | None]:
    """Get current rate limit configuration.

    Returns:
    --------
    dict with key: requests_per_hour (float | None)
    """
    return {"requests_per_hour": _RATE_LIMIT_REQUESTS_PER_HOUR}


def get_rate_limit_status() -> dict[str, Any]:
    """Get detailed rate limit status.

    Returns:
    --------
    dict with keys:
        - enabled: bool - Whether rate limiting is active
        - requests_per_hour: float | None - Configured limit
        - interval_seconds: float - Minimum time between requests (0.0 if disabled)
        - last_request_time: float | None - Timestamp of last request
    """
    enabled = _RATE_LIMIT_REQUESTS_PER_HOUR is not None
    interval = 3600.0 / _RATE_LIMIT_REQUESTS_PER_HOUR if enabled else 0.0
    return {
        "enabled": enabled,
        "requests_per_hour": _RATE_LIMIT_REQUESTS_PER_HOUR,
        "interval_seconds": interval,
        "last_request_time": _RATE_LIMIT_LAST_REQUEST,
    }


def _maybe_wait_for_rate_limit() -> None:
    """Wait if necessary to respect rate limit.

    This function should be called before making a request. It will:
    1. Do nothing if rate limiting is disabled
    2. Do nothing if this is the first request
    3. Sleep for the remaining interval time if needed
    4. Update the last request timestamp
    """
    global _RATE_LIMIT_LAST_REQUEST

    if _RATE_LIMIT_REQUESTS_PER_HOUR is None:
        return

    current_time = time.time()

    if _RATE_LIMIT_LAST_REQUEST is not None:
        interval = 3600.0 / _RATE_LIMIT_REQUESTS_PER_HOUR
        elapsed = current_time - _RATE_LIMIT_LAST_REQUEST
        remaining = interval - elapsed

        if remaining > 0:
            logger.debug("Rate limiting: sleeping for %.2f seconds", remaining)
            time.sleep(remaining)
            current_time = time.time()

    _RATE_LIMIT_LAST_REQUEST = current_time


def _calculate_retry_delay(attempt: int, retry_after: float | None) -> float:
    """Calculate delay before next retry.

    Uses Retry-After header if available, otherwise exponential backoff.

    Parameters:
    -----------
    attempt: int
        Current retry attempt number (0-indexed)
    retry_after: float | None
        Value from Retry-After header, if present

    Returns:
    --------
    Delay in seconds
    """
    # Delegate to retry module for consistency
    return retry_module.calculate_retry_delay(attempt, retry_after)


def _parse_retry_after(response: requests.Response) -> float | None:
    """Parse Retry-After header from response.

    Parameters:
    -----------
    response: requests.Response
        The HTTP response

    Returns:
    --------
    Seconds to wait, or None if header not present/parseable
    """
    # Delegate to retry module for consistency
    return retry_module.parse_retry_after(response)


def _make_request_with_retry(
    request_url: str,
    args: dict[str, Any],
    oauth_auth: Any,
) -> requests.Response:
    """Make HTTP request with automatic retry on transient errors.

    Handles HTTP 429 (rate limit), 5xx (server errors), timeouts, and
    connection errors with configurable retry behavior.

    Parameters:
    -----------
    request_url: str
        The URL to request
    args: dict
        Request arguments
    oauth_auth: Any
        OAuth authentication object (or None)

    Returns:
    --------
    requests.Response

    Raises:
    -------
    FlickrRateLimitError: If rate limit exceeded and max retries exhausted
    FlickrServerError: If server error and max retries exhausted
    FlickrTimeoutError: If timeout/connection error and max retries exhausted
    """
    # Ensure retry module is initialized
    _init_retry_module()

    def make_request() -> requests.Response:
        return requests.post(request_url, args, auth=oauth_auth, timeout=get_timeout())

    return retry_module.retry_request(make_request, operation_name="API call")


def send_request(url, data):
    """send a http request."""
    req = urllib.request.Request(url, data.encode())
    try:
        return urlopen_and_read(req)
    except urllib.error.HTTPError as e:
        raise FlickrError(e.read().split("&")[0])


def call_api(
    api_key=None,
    api_secret=None,
    auth_handler=None,
    needssigning=False,
    request_url=REST_URL,
    raw=False,
    **args,
):
    """
        Performs the calls to the Flickr REST interface.

    Parameters:
        api_key:
            The API_KEY to use. If none is given and a auth_handler is used
            the key stored in the auth_handler is used, otherwise, the values
            stored in the `flickr_keys` module are used.
        api_secret:
            The API_SECRET to use. If none is given and a auth_handler is used
            the key stored in the auth_handler is used, otherwise, the values
            stored in the `flickr_keys` module are used.
        auth_handler:
            The authentication handler object to use to perform authentication.
        request_url:
            The url to the rest interface to use by default the url in REST_URL
            is used.
        raw:
            if True the default xml response from the server is returned. If
            False (default) a dictionary built from the JSON answer is
            returned.
        args:
            the arguments to pass to the method.
    """

    if not api_key:
        if auth_handler is not None:
            api_key = auth_handler.key
        else:
            api_key = keys.API_KEY
    if not api_secret:
        if auth_handler is not None:
            api_secret = auth_handler.secret
        else:
            api_secret = keys.API_SECRET

    if not api_key or not api_secret:
        raise FlickrError("The Flickr API keys have not been set")

    clean_args(args)
    args["api_key"] = api_key
    if not raw:
        args["format"] = "json"
        args["nojsoncallback"] = 1

    # Get OAuth auth object if using authentication
    oauth_auth = None
    if auth_handler is None:
        if needssigning:
            query_elements = list(args.items())
            query_elements.sort()
            sig = keys.API_SECRET + ["".join(["".join(e) for e in query_elements])]
            m = hashlib.md5()
            m.update(sig)
            api_sig = m.digest()
            args["api_sig"] = api_sig
    else:
        oauth_request = auth_handler.complete_parameters(url=request_url, params=args)
        # Extract the OAuth auth object and params from the OAuthRequest
        oauth_auth = oauth_request.oauth
        args = dict(oauth_request.items())

    if CACHE is None:
        resp = _make_request_with_retry(request_url, args, oauth_auth)
    else:
        cachekey = {k: v for k, v in args.items() if k not in IGNORED_FIELDS}
        cachekey = urllib.parse.urlencode(cachekey)

        cached_resp = CACHE.get(cachekey)
        if cached_resp:
            resp = cached_resp
            logger.debug("   HIT for cache key: %s", cachekey)
        else:
            resp = _make_request_with_retry(request_url, args, oauth_auth)
            CACHE.set(cachekey, resp)
            logger.debug("NO HIT for cache key: %s", cachekey)

    if raw:
        return resp.content

    # catch for all 5xx errors
    if 500 <= resp.status_code < 600:
        raise FlickrServerError(resp.status_code, resp.content.decode("utf8"))

    try:
        resp = resp.json()

    except ValueError:
        logger.error("Could not parse response: %s", str(resp.content))

    if resp["stat"] != "ok":
        raise FlickrAPIError(resp["code"], resp["message"])

    resp = clean_content(resp)

    return resp


def clean_content(d):
    """
    Cleans out recursively the keys coming from the JSON
    dictionary.

    Namely: "_content" keys are replaces with their associated
        values if they are the only key of the dictionary. Other
        wise they are replaces by a "text" key with the same value.
    """
    if isinstance(d, dict):
        d_clean = {}
        if len(d) == 1 and "_content" in d:
            return clean_content(d["_content"])
        for k, v in d.items():
            if k == "_content":
                k = "text"
            d_clean[k] = clean_content(v)
        return d_clean
    elif isinstance(d, list):
        return [clean_content(i) for i in d]
    else:
        return d


# Unix timestamp parameters that must be integers for Flickr API
_TIMESTAMP_PARAMS = {
    "min_upload_date",
    "max_upload_date",
    "min_taken_date",
    "max_taken_date",
    "min_date",
    "max_date",
}


def clean_args(args):
    """
    Reformat the arguments.
    """
    for k, v in args.items():
        if isinstance(v, bool):
            args[k] = int(v)
        elif k in _TIMESTAMP_PARAMS and isinstance(v, float):
            args[k] = int(v)
