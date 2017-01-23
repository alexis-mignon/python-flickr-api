"""
    Deals with multipart POST requests.

    The code is adapted from the recipe found at :
    http://code.activestate.com/recipes/146306/
    No author name was given.

    Author : Alexis Mignon (c)
    email  : alexis.mignon@gmail.Com
    Date   : 06/08/2011

"""

from six.moves import http_client, urllib
from six import binary_type, text_type
import mimetypes


def posturl(url, fields, files):
    urlparts = urllib.parse.urlsplit(url)
    return post_multipart(urlparts[1], urlparts[2], fields, files)


def post_multipart(host, selector, fields, files):
    """
    Post fields and files to an http host as multipart/form-data.
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be
    uploaded as files.

    Return the server's response page.
    """
    content_type, body = encode_multipart_formdata(fields, files)
    h = http_client.HTTPSConnection(host)
    headers = {"Content-Type": content_type, 'content-length': str(len(body))}
    h.request("POST", selector, headers=headers)
    h.send(body)
    r = h.getresponse()
    data = r.read()
    h.close()
    return r, data


def encode_multipart_formdata(fields, files):
    """
    fields is a sequence of (name, value) elements for regular form fields.
    files is a sequence of (name, filename, value) elements for data to be
    uploaded as files.

    Return (content_type, body) ready for httplib.HTTP instance
    """
    BOUNDARY = b'----------ThIs_Is_tHe_bouNdaRY_$'
    CRLF = b'\r\n'
    L = []
    for (key, value) in fields:
        if isinstance(key, binary_type):
            key = key.decode()
        if isinstance(value, text_type):
            value = value.encode("utf-8")
        L.append(b'--' + BOUNDARY)
        L.append(('Content-Disposition: form-data; name="%s"' % key).encode("utf-8"))
        L.append(b'')
        L.append(value)
    for (key, filename, value) in files:
        if isinstance(key, binary_type):
            key = key.decode()
        if isinstance(filename, binary_type):
            filename = filename.decode()
        L.append(b'--' + BOUNDARY)
        L.append(
            (
                'Content-Disposition: form-data; name="%s"; filename="%s"' %
                    (key, filename)
            ).encode("utf-8")
        )
        L.append(('Content-Type: %s' % get_content_type(filename)).encode("utf-8"))
        L.append(b'')
        L.append(value)
    L.append(b'--' + BOUNDARY + b'--')
    L.append(b'')
    body = CRLF.join(L)
    content_type = b'multipart/form-data; boundary=' + BOUNDARY
    return content_type, body


def get_content_type(filename):
    return mimetypes.guess_type(filename)[0] or 'application/octet-stream'
