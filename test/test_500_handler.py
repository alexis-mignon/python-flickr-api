import unittest
from unittest.mock import MagicMock

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler
from flickr_api.flickrerrors import FlickrServerError

from requests import Response

from io import StringIO
from io import BytesIO

import inspect


class Test5XXHandler(unittest.TestCase):
    def test_call_5XX(self):
        from flickr_api import set_auth_handler
        auth_handler = AuthHandler(
            key="test",
            secret="test",
            access_token_key="test",
            access_token_secret="test")
        set_auth_handler(auth_handler)
        args = dict(
            photo_file='/tmp/test_file', photo_file_data=StringIO("000000"))

        module = inspect.getmodule(method_call)
        resp = Response()
        resp.status_code = 502
        resp.raw = BytesIO("Bad Gateway".encode("utf-8"))
        module.requests.post = MagicMock(return_value=resp)

        with self.assertRaises(FlickrServerError) as context:
            f.Person.findByUserName("tomquirkphoto")

        print(context.exception)
        self.assertEqual("HTTP Server Error 502: Bad Gateway",
                          str(context.exception))
