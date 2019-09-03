import unittest
from unittest.mock import MagicMock

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler

from requests import Response

from io import StringIO
from io import BytesIO

import inspect


class TestBytesResponse(unittest.TestCase):
    def test_bytes_response(self):
        from flickr_api import set_auth_handler
        auth_handler = AuthHandler(
            key='test',
            secret='test',
            access_token_key='test',
            access_token_secret='test')
        set_auth_handler(auth_handler)
        args = dict(photo_file='/tmp/test_file',
            photo_file_data=StringIO('000000'))

        module = inspect.getmodule(method_call)
        resp = Response()
        resp.status_code = 200
        resp.raw = BytesIO(b'[0,1]')
        module.requests.post = MagicMock(return_value=resp)
        payload = module.requests.post.return_value.json()
        self.assertEqual(type(payload), list)