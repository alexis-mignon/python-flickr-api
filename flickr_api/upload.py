"""
    Upload API for Flickr.
    It is separated since it requires different treatments than
    the usual API.

    Two functions are provided:

    - upload
    - replace (presently not working)

    Author: Alexis Mignon (c)
    email: alexis.mignon@gmail.com
    Date:  06/08/2011

"""


from .flickrerrors import FlickrError, FlickrAPIError
from .objects import Photo, UploadTicket
from . import auth
from . import multipart
import os
from xml.etree import ElementTree as ET

UPLOAD_URL = "https://api.flickr.com/services/upload/"
REPLACE_URL = "https://api.flickr.com/services/replace/"


def format_dict(d):
    d_ = {}
    for k, v in d.iteritems():
        if isinstance(v, bool):
            v = int(v)
        elif isinstance(v, unicode):
            v = v.encode("utf8")
        if isinstance(k, unicode):
            k = k.encode("utf8")
        v = str(v)
        d_[k] = v
    return d_


def post(url, auth_handler, args, photo_file):
    args = format_dict(args)
    args["api_key"] = auth_handler.key

    params = auth_handler.complete_parameters(url, args).parameters

    fields = params.items()

    files = [("photo", os.path.basename(photo_file), open(photo_file).read())]

    r, data = multipart.posturl(url, fields, files)
    if r.status != 200:
        raise FlickrError("HTTP Error %i: %s" % (r.status, data))
    
    r = ET.fromstring(data)
    if r.get("stat") != 'ok':
        err = r[0]
        raise FlickrAPIError(int(err.get("code")), err.get("msg"))
    return r


def upload(**args):
    """
    Authentication:

        This method requires authentication with 'write' permission.

    Arguments:
        photo_file
            The file to upload.
        title (optional)
            The title of the photo.
        description (optional)
            A description of the photo. May contain some limited HTML.
        tags (optional)
            A space-seperated list of tags to apply to the photo.
        is_public, is_friend, is_family (optional)
            Set to 0 for no, 1 for yes. Specifies who can view the photo.
        safety_level (optional)
            Set to 1 for Safe, 2 for Moderate, or 3 for Restricted.
        content_type (optional)
            Set to 1 for Photo, 2 for Screenshot, or 3 for Other.
        hidden (optional)
            Set to 1 to keep the photo in global search results, 2 to hide
            from public searches.
        async
            set to 1 for async mode, 0 for sync mode

    """
    if "async" not in args:
        args["async"] = False

    photo_file = args.pop("photo_file")
    r = post(UPLOAD_URL, auth.AUTH_HANDLER, args, photo_file)

    t = r[0]
    if t.tag == 'photoid':
        return Photo(
            id=t.text,
            editurl='https://www.flickr.com/photos/upload/edit/?ids=' + t.text
        )
    elif t.tag == 'ticketid':
        return UploadTicket(id=t.text)
    else:
        raise FlickrError("Unexpected tag: %s" % t.tag)


def replace(**args):
    """
     Authentication:

        This method requires authentication with 'write' permission.

        For details of how to obtain authentication tokens and how to sign
        calls, see the authentication api spec. Note that the 'photo' parameter
        should not be included in the signature. All other POST parameters
        should be included when generating the signature.

    Arguments:

        photo_file
            The file to upload.
        photo_id
            The ID of the photo to replace.
        async (optional)
            Photos may be replaced in async mode, for applications that
            don't want to wait around for an upload to complete, leaving
            a socket connection open the whole time. Processing photos
            asynchronously is recommended. Please consult the documentation
            for details.

    """
    if "async" not in args:
        args["async"] = True
    if "photo" in args:
        args["photo_id"] = args.pop("photo").id

    photo_file = args.pop("photo_file")

    r = post(REPLACE_URL, auth.AUTH_HANDLER, args, photo_file)

    t = r[0]
    if t.tag == 'photoid':
        return Photo(id=t.text)
    elif t.tag == 'ticketid':
        return UploadTicket(id=t.text, secret=t.secret)
    else:
        raise FlickrError("Unexpected tag: %s" % t.tag)
