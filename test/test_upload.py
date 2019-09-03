import unittest
from unittest.mock import MagicMock

from flickr_api import upload
from flickr_api.auth import AuthHandler
from flickr_api.flickrerrors import FlickrError

from requests import Response

from io import StringIO
from io import BytesIO

import inspect


class TestUpload(unittest.TestCase):
    def test_upload_not_200(self):
        from flickr_api import set_auth_handler
        auth_handler = AuthHandler(
            key="test",
            secret="test",
            access_token_key="test",
            access_token_secret="test")
        set_auth_handler(auth_handler)
        args = dict(
            photo_file='/tmp/test_file', photo_file_data=StringIO("000000"))

        module = inspect.getmodule(upload)
        resp = Response()
        resp.status_code = 404
        resp.raw = BytesIO("Not Found".encode("utf-8"))
        module.requests.post = MagicMock(return_value=resp)

        with self.assertRaises(FlickrError) as context:
            upload(**args)

        print(context.exception)
        self.assertEqual("HTTP Error 404: Not Found", str(context.exception))
