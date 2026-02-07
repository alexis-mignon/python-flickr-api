"""
Retry utilities for handling transient errors.

This module provides reusable retry logic for HTTP requests, handling:
- HTTP 429 (rate limit) with Retry-After header support
- HTTP 5xx (server errors)
- ReadTimeout exceptions
- ConnectionError exceptions

Author: python-flickr-api contributors
"""

import logging
import time
from typing import Any, Callable, TypeVar

import requests

from .flickrerrors import FlickrRateLimitError, FlickrServerError, FlickrTimeoutError

logger = logging.getLogger(__name__)

T = TypeVar("T")

# These are imported from method_call to share configuration
# We use a getter pattern to avoid circular imports
_get_retry_config: Callable[[], dict[str, Any]] | None = None
_get_rate_limit_wait: Callable[[], None] | None = None


def set_retry_config_getter(getter: Callable[[], dict[str, Any]]) -> None:
    """Set the function to get retry configuration.

    This is called during module initialization to avoid circular imports.
    """
    global _get_retry_config
    _get_retry_config = getter


def set_rate_limit_wait_func(func: Callable[[], None]) -> None:
    """Set the function to wait for rate limits.

    This is called during module initialization to avoid circular imports.
    """
    global _get_rate_limit_wait
    _get_rate_limit_wait = func


def _get_config() -> dict[str, Any]:
    """Get current retry configuration."""
    if _get_retry_config is None:
        # Default config if not initialized
        return {"max_retries": 3, "base_delay": 1.0, "max_delay": 60.0}
    return _get_retry_config()


def calculate_retry_delay(attempt: int, retry_after: float | None) -> float:
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
    config = _get_config()
    max_delay = config["max_delay"]
    base_delay = config["base_delay"]

    if retry_after is not None and retry_after > 0:
        return min(retry_after, max_delay)

    # Exponential backoff: base_delay * 2^attempt
    delay = base_delay * (2**attempt)
    return min(delay, max_delay)


def parse_retry_after(response: requests.Response) -> float | None:
    """Parse Retry-After header from response.

    Parameters:
    -----------
    response: requests.Response
        The HTTP response

    Returns:
    --------
    Seconds to wait, or None if header not present/parseable
    """
    retry_after = response.headers.get("Retry-After")
    if retry_after is None:
        return None

    try:
        return float(retry_after)
    except ValueError:
        # Could be an HTTP-date format, but Flickr typically uses seconds
        logger.warning("Could not parse Retry-After header: %s", retry_after)
        return None


def retry_request(
    make_request: Callable[[], requests.Response],
    operation_name: str = "request",
) -> requests.Response:
    """Execute a request with automatic retry on transient errors.

    Handles:
    - HTTP 429 (rate limit) with Retry-After header support
    - HTTP 5xx (server errors)
    - requests.exceptions.ReadTimeout
    - requests.exceptions.ConnectionError

    Parameters:
    -----------
    make_request: Callable[[], requests.Response]
        A function that makes the HTTP request and returns a Response
    operation_name: str
        Name of the operation for logging purposes

    Returns:
    --------
    requests.Response

    Raises:
    -------
    FlickrRateLimitError: If rate limit exceeded and max retries exhausted
    FlickrServerError: If server error and max retries exhausted
    FlickrTimeoutError: If timeout/connection error and max retries exhausted
    """
    # Apply proactive rate limiting before first attempt
    if _get_rate_limit_wait is not None:
        _get_rate_limit_wait()

    config = _get_config()
    max_retries = config["max_retries"]

    last_exception: Exception | None = None

    for attempt in range(max_retries + 1):
        try:
            resp = make_request()

            # Check for retryable HTTP status codes
            if resp.status_code == 429:
                # Rate limited
                retry_after = parse_retry_after(resp)
                content = resp.content.decode("utf8") if resp.content else "Too Many Requests"
                last_exception = FlickrRateLimitError(retry_after, content)

                if attempt >= max_retries:
                    logger.warning(
                        "%s: Rate limit exceeded, max retries (%d) exhausted",
                        operation_name,
                        max_retries,
                    )
                    raise last_exception

                delay = calculate_retry_delay(attempt, retry_after)
                logger.warning(
                    "%s: Rate limit exceeded (attempt %d/%d), retrying in %.1f seconds",
                    operation_name,
                    attempt + 1,
                    max_retries + 1,
                    delay,
                )
                time.sleep(delay)
                continue

            if 500 <= resp.status_code < 600:
                # Server error
                content = resp.content.decode("utf8") if resp.content else "Server Error"
                last_exception = FlickrServerError(resp.status_code, content)

                if attempt >= max_retries:
                    logger.warning(
                        "%s: Server error %d, max retries (%d) exhausted",
                        operation_name,
                        resp.status_code,
                        max_retries,
                    )
                    raise last_exception

                delay = calculate_retry_delay(attempt, None)
                logger.warning(
                    "%s: Server error %d (attempt %d/%d), retrying in %.1f seconds",
                    operation_name,
                    resp.status_code,
                    attempt + 1,
                    max_retries + 1,
                    delay,
                )
                time.sleep(delay)
                continue

            # Success or non-retryable error
            return resp

        except (requests.exceptions.ReadTimeout, requests.exceptions.Timeout) as e:
            last_exception = FlickrTimeoutError(str(e))

            if attempt >= max_retries:
                logger.warning(
                    "%s: Timeout, max retries (%d) exhausted",
                    operation_name,
                    max_retries,
                )
                raise last_exception from e

            delay = calculate_retry_delay(attempt, None)
            logger.warning(
                "%s: Timeout (attempt %d/%d), retrying in %.1f seconds",
                operation_name,
                attempt + 1,
                max_retries + 1,
                delay,
            )
            time.sleep(delay)

        except requests.exceptions.ConnectionError as e:
            last_exception = FlickrTimeoutError(f"Connection error: {e}")

            if attempt >= max_retries:
                logger.warning(
                    "%s: Connection error, max retries (%d) exhausted",
                    operation_name,
                    max_retries,
                )
                raise last_exception from e

            delay = calculate_retry_delay(attempt, None)
            logger.warning(
                "%s: Connection error (attempt %d/%d), retrying in %.1f seconds",
                operation_name,
                attempt + 1,
                max_retries + 1,
                delay,
            )
            time.sleep(delay)

    # Should not reach here, but just in case
    if last_exception is not None:
        raise last_exception
    raise FlickrTimeoutError("Unknown error during retry")
