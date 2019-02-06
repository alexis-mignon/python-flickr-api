""" Base Exception classes

"""


class FlickrError(Exception):
    """Base Exception class
    """
    pass


class FlickrAPIError(FlickrError):
    """ Exception for Flickr API Errors

    Parameters:
    -----------
    code: int
        Error code
    message: str
        Error message
    """
    def __init__(self, code, message):
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
    """ Exception for Flickr Server Errors

    These are exceptions that happen on the HTTP layer with 5XX status codes.

    Parameters:
    -----------
    status_code: int
        HTTP Status code
    content: str
        error content message
    """
    def __init__(self, status_code, content):
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
