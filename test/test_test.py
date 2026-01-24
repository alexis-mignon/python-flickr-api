"""
Tests for test API methods.

Batch 24:
flickr.test.echo, flickr.test.login, flickr.test.null

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call
from flickr_api.objects import Person

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestTestMethods(FlickrApiTestCase):
    """Tests for test API methods"""

    @patch.object(method_call.requests, "post")
    def test_echo(self, mock_post):
        """Test test.echo (flickr.test.echo)"""
        # flickr.test.echo response has multiple root elements which isn't
        # valid XML, so we create the JSON response directly
        # Note: clean_content() transforms {"_content": "val"} to "val"
        json_response = {
            "method": {"_content": "echo"},
            "foo": {"_content": "bar"}
        }

        mock_post.return_value = self._mock_response(json_response)

        result = f.test.echo()

        # Returns the raw response dict (after clean_content transformation)
        self.assertIsInstance(result, dict)
        # The response has method=echo and foo=bar (as plain strings)
        self.assertIn("method", result)
        self.assertEqual(result["method"], "echo")
        self.assertIn("foo", result)
        self.assertEqual(result["foo"], "bar")

    @patch.object(method_call.requests, "post")
    def test_login(self, mock_post):
        """Test test.login (flickr.test.login)"""
        api_doc = load_api_doc("flickr.test.login")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.test.login()

        # Returns a Person object
        self.assertIsInstance(result, Person)
        self.assertEqual(result.id, "12037949754@N01")
        # Username is a plain string after clean_content transformation
        self.assertEqual(result.username, "Bees")

    @patch.object(method_call.requests, "post")
    def test_null(self, mock_post):
        """Test test.null (flickr.test.null)"""
        # flickr.test.null returns an empty response
        mock_post.return_value = self._mock_response({})

        result = f.test.null()

        # Returns None for empty response
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
