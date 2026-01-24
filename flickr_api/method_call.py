"""
method_call module.

This module is used to perform the calls to the REST interface.

Author: Alexis Mignon (c)
e-mail: alexis.mignon@gmail.com
Date: 06/08/2011

"""

import urllib.parse
import urllib.request
import urllib.error
import requests
import hashlib
import logging
from typing import Any

from . import keys
from .utils import urlopen_and_read
from .flickrerrors import FlickrError, FlickrAPIError, FlickrServerError
from .cache import SimpleCache

REST_URL = "https://api.flickr.com/services/rest/"

CACHE = None

IGNORED_FIELDS = set(["oauth_nonce", "oauth_timestamp", "oauth_signature"])

logger = logging.getLogger(__name__)


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
        resp = requests.post(request_url, args, auth=oauth_auth, timeout=get_timeout())
    else:
        cachekey = {k: v for k, v in args.items() if k not in IGNORED_FIELDS}
        cachekey = urllib.parse.urlencode(cachekey)

        resp = CACHE.get(cachekey) or requests.post(
            request_url, args, auth=oauth_auth, timeout=get_timeout()
        )
        if cachekey not in CACHE:
            CACHE.set(cachekey, resp)
            logger.debug("NO HIT for cache key: %s" % cachekey)
        else:
            logger.debug("   HIT for cache key: %s" % cachekey)

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
