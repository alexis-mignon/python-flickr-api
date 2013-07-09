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
