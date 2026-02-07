"""Base Exception classes"""


class FlickrError(Exception):
    """Base Exception class"""

    pass


class FlickrAPIError(FlickrError):
    """Exception for Flickr API Errors

    Parameters:
    -----------
    code: int
        Error code
    message: str
        Error message
    """

    code: int
    message: str

    def __init__(self, code: int, message: str) -> None:
        """Constructor

        Parameters:
        -----------
        code: int
            Error code
        message: str
            Error message
        """
        FlickrError.__init__(self, "%i : %s" % (code, message))
        self.code = code
        self.message = message


class FlickrServerError(FlickrError):
    """Exception for Flickr Server Errors

    These are exceptions that happen on the HTTP layer with 5XX status codes.

    Parameters:
    -----------
    status_code: int
        HTTP Status code
    content: str
        error content message
    """

    status_code: int
    content: str

    def __init__(self, status_code: int, content: str) -> None:
        """Constructor

        Parameters:
        -----------
        status_code: int
            HTTP Status code
        content: str
            error content message
        """
        FlickrError.__init__(self, "HTTP Server Error %i: %s" % (status_code, content))
        self.status_code = status_code
        self.content = content


class FlickrRateLimitError(FlickrError):
    """Exception for Flickr Rate Limit Errors (HTTP 429)

    Raised when the API rate limit has been exceeded. Contains retry
    information to help callers implement backoff strategies.

    Parameters:
    -----------
    retry_after: float | None
        Seconds to wait before retrying, from Retry-After header (if provided)
    content: str
        error content message
    """

    retry_after: float | None
    content: str

    def __init__(self, retry_after: float | None, content: str) -> None:
        """Constructor

        Parameters:
        -----------
        retry_after: float | None
            Seconds to wait before retrying (from Retry-After header, if available)
        content: str
            error content message
        """
        if retry_after:
            msg = f"Rate limit exceeded. Retry after {retry_after} seconds: {content}"
        else:
            msg = f"Rate limit exceeded: {content}"
        FlickrError.__init__(self, msg)
        self.retry_after = retry_after
        self.content = content


class FlickrTimeoutError(FlickrError):
    """Exception for request timeout or connection errors.

    Raised when a request times out or fails due to connection issues
    and max retries have been exhausted.

    Parameters:
    -----------
    message: str
        Error message describing the timeout/connection issue
    """

    message: str

    def __init__(self, message: str) -> None:
        """Constructor

        Parameters:
        -----------
        message: str
            Error message describing the timeout/connection issue
        """
        FlickrError.__init__(self, f"Request failed: {message}")
        self.message = message
