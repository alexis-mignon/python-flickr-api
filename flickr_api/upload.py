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

from typing import Any

from .flickrerrors import FlickrError, FlickrAPIError
from .objects import Photo, UploadTicket
from .method_call import get_timeout
from . import auth
import os
from xml.etree import ElementTree as ET
import requests


UPLOAD_URL = "https://api.flickr.com/services/upload/"
REPLACE_URL = "https://api.flickr.com/services/replace/"


def format_dict(d):
    d_ = {}
    for k, v in d.items():
        if isinstance(v, bool):
            v = int(v)
        if isinstance(k, str):
            k = k.encode("utf8")
        # Convert to string first, then encode - bytes(int) doesn't work as expected
        # (bytes(0) gives b'', bytes(1) gives b'\x00', not b'0' or b'1')
        if not isinstance(v, bytes):
            v = str(v).encode("utf8")
        d_[k] = v
    return d_


def post(url, auth_handler, args, photo_file, photo_file_data=None):
    import time
    import hashlib
    import hmac
    import base64
    from urllib.parse import quote

    args = format_dict(args)
    args[b"api_key"] = (
        auth_handler.key.encode("utf8") if isinstance(auth_handler.key, str) else auth_handler.key
    )

    if photo_file_data is None:
        photo_file_data = open(photo_file, "rb")

    # Flickr's upload API requires OAuth parameters to be included as form
    # fields and the signature to cover all parameters (except photo).
    # We manually construct the OAuth signature for proper control.

    # Generate OAuth parameters
    oauth_params = {
        b"oauth_consumer_key": auth_handler.key.encode("utf8"),
        b"oauth_token": auth_handler.access_token_key.encode("utf8"),
        b"oauth_signature_method": b"HMAC-SHA1",
        b"oauth_timestamp": str(int(time.time())).encode("utf8"),
        b"oauth_nonce": base64.b64encode(os.urandom(16))
        .replace(b"+", b"")
        .replace(b"/", b"")
        .replace(b"=", b"")[:16],
        b"oauth_version": b"1.0",
    }

    # Combine all params for signing (args + oauth_params, but not photo)
    all_params = dict(args)
    all_params.update(oauth_params)

    # Sort and encode params for signature base string
    def percent_encode(s):
        if isinstance(s, bytes):
            s = s.decode("utf8")
        # OAuth requires uppercase percent encoding
        return quote(s, safe="")

    sorted_params = sorted(all_params.items())
    param_string = "&".join(percent_encode(k) + "=" + percent_encode(v) for k, v in sorted_params)

    # Create signature base string
    base_string = "&".join(["POST", percent_encode(url), percent_encode(param_string)])

    # Create signing key
    signing_key = (
        percent_encode(auth_handler.secret) + "&" + percent_encode(auth_handler.access_token_secret)
    )

    # Calculate signature
    signature = base64.b64encode(
        hmac.new(signing_key.encode("utf8"), base_string.encode("utf8"), hashlib.sha1).digest()
    )

    oauth_params[b"oauth_signature"] = signature

    # Combine all params for the form data
    all_params = dict(args)
    all_params.update(oauth_params)

    # Convert to string keys/values for requests
    form_data = {
        k.decode("utf8") if isinstance(k, bytes) else k: v.decode("utf8")
        if isinstance(v, bytes)
        else v
        for k, v in all_params.items()
    }

    files = {"photo": (os.path.basename(photo_file), photo_file_data.read())}

    resp = requests.post(url, data=form_data, files=files, timeout=get_timeout())
    data = resp.content

    if resp.status_code != 200:
        raise FlickrError("HTTP Error %i: %s" % (resp.status_code, resp.text))

    r = ET.fromstring(data)
    if r.get("stat") != "ok":
        err = r[0]
        raise FlickrAPIError(int(err.get("code")), err.get("msg"))
    return r


def upload(**args: Any) -> Photo | UploadTicket:
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
            A space-separated list of tags to apply to the photo.
        is_public, is_friend, is_family (optional)
            Set to "0" for no, "1" for yes. Specifies who can view the photo.
        safety_level (optional)
            Set to "1" for Safe, "2" for Moderate, or "3" for Restricted.
        content_type (optional)
            Set to "1" for Photo, "2" for Screenshot, or "3" for Other.
        hidden (optional)
            Set to "1" to keep the photo in global search results, "2" to hide
            from public searches.
        async
            set to 1 for async mode, 0 for sync mode
        asynchronous (optional)
            Alias to async for Python >= 3.6 where async is a keyword

    """
    if "asynchronous" in args:
        args["async"] = args["asynchronous"]
        del args["asynchronous"]
    if "async" not in args:
        args["async"] = False

    photo_file = args.pop("photo_file")
    if "photo_file_data" in args:
        photo_file_data = args.pop("photo_file_data")
    else:
        photo_file_data = None

    r = post(UPLOAD_URL, auth.AUTH_HANDLER, args, photo_file, photo_file_data)

    t = r[0]
    if t.tag == "photoid":
        return Photo(
            id=t.text,
            editurl="https://www.flickr.com/photos/upload/edit/?ids=" + t.text,
        )
    elif t.tag == "ticketid":
        return UploadTicket(id=t.text)
    else:
        raise FlickrError("Unexpected tag: %s" % t.tag)


def replace(**args: Any) -> Photo | UploadTicket:
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
        asynchronous (optional)
            Alias to async for Python >= 3.6 where async is a keyword

    """
    if "asynchronous" in args:
        args["async"] = args["asynchronous"]
        del args["asynchronous"]
    if "async" not in args:
        args["async"] = False
    if "photo" in args:
        args["photo_id"] = args.pop("photo").id

    photo_file = args.pop("photo_file")

    if "photo_file_data" in args:
        photo_file_data = args.pop("photo_file_data")
    else:
        photo_file_data = None

    r = post(REPLACE_URL, auth.AUTH_HANDLER, args, photo_file, photo_file_data)

    t = r[0]

    if t.tag == "photoid":
        return Photo(id=t.text)
    elif t.tag == "ticketid":
        return UploadTicket(id=t.text)
    else:
        raise FlickrError("Unexpected tag: %s" % t.tag)
