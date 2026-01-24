"""
Base test class for Flickr API tests.

Provides common setUp and _mock_response methods to eliminate code duplication
across test files.
"""
import json
import unittest

import flickr_api as f
from flickr_api.auth import AuthHandler

from requests import Response


class FlickrApiTestCase(unittest.TestCase):
    """Base test case for Flickr API tests.

    Provides:
    - setUp(): Configures a test auth handler
    - _mock_response(): Creates mock Response objects with JSON data
    """

    def setUp(self):
        """Set up auth handler for tests"""
        auth_handler = AuthHandler(
            key="test_key",
            secret="test_secret",
            access_token_key="test_token",
            access_token_secret="test_token_secret",
        )
        f.set_auth_handler(auth_handler)

    def _mock_response(self, json_data):
        """Create a mock Response object with the given JSON data"""
        json_data["stat"] = "ok"
        resp = Response()
        resp.status_code = 200
        resp._content = json.dumps(json_data).encode("utf-8")
        return resp
