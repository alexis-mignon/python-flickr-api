"""
Tests for Tag.getHotList, Tag.getListUser, and Tag.getListUserPopular.

Uses example responses from the api-docs/ directory, converted from XML to JSON.
"""
import json
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler

from requests import Response

from test_utils import xml_to_flickr_json, load_api_doc


class TestTagMethods(unittest.TestCase):
    """Tests for Tag.getHotList, Tag.getListUser, and Tag.getListUserPopular"""

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

    @patch.object(method_call.requests, "post")
    def test_get_hot_list(self, mock_post):
        """Test Tag.getHotList parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.tags.getHotList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        tags = f.Tag.getHotList()

        # Verify based on the example data
        # Note: _content is converted to "text" by clean_content() in method_call.py
        self.assertEqual(len(tags), 6)
        self.assertIsInstance(tags[0], f.Tag)
        # First tag: score="20", northerncalifornia
        self.assertEqual(tags[0].score, "20")
        self.assertEqual(tags[0].text, "northerncalifornia")
        # Second tag: score="18", top20
        self.assertEqual(tags[1].score, "18")
        self.assertEqual(tags[1].text, "top20")
        # Last tag: score="4", jan06
        self.assertEqual(tags[5].score, "4")
        self.assertEqual(tags[5].text, "jan06")

    @patch.object(method_call.requests, "post")
    def test_get_list_user(self, mock_post):
        """Test Tag.getListUser parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.tags.getListUser")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        tags = f.Tag.getListUser(user_id="12037949754@N01")

        # Verify based on the example data
        # Note: Tags with only _content become strings after clean_content(),
        # so we access via .text attribute
        self.assertEqual(len(tags), 5)
        self.assertIsInstance(tags[0], f.Tag)
        # Tags from example: gull, tag1, tag2, tags, test
        self.assertEqual(tags[0].text, "gull")
        self.assertEqual(tags[1].text, "tag1")
        self.assertEqual(tags[2].text, "tag2")
        self.assertEqual(tags[3].text, "tags")
        self.assertEqual(tags[4].text, "test")

    @patch.object(method_call.requests, "post")
    def test_get_list_user_popular(self, mock_post):
        """Test Tag.getListUserPopular parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.tags.getListUserPopular")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        tags = f.Tag.getListUserPopular(user_id="12037949754@N01")

        # Verify based on the example data
        # Note: _content is converted to "text" by clean_content() in method_call.py
        self.assertEqual(len(tags), 5)
        self.assertIsInstance(tags[0], f.Tag)
        # First tag: count="10", bar
        self.assertEqual(tags[0].text, "bar")
        self.assertEqual(tags[0].count, 10)  # count is converted to int by Tag
        # Second tag: count="11", foo
        self.assertEqual(tags[1].text, "foo")
        self.assertEqual(tags[1].count, 11)
        # Third tag: count="147", gull (highest count)
        self.assertEqual(tags[2].text, "gull")
        self.assertEqual(tags[2].count, 147)


if __name__ == "__main__":
    unittest.main()
