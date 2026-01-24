"""
Tests for Photo.Suggestion API methods.

Batch 14:
flickr.photos.suggestions.approveSuggestion

Uses example responses from the api-docs/ directory.
"""
import json
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler

from requests import Response


class TestPhotoSuggestionMethods(unittest.TestCase):
    """Tests for Photo.Suggestion API methods"""

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
    def test_photo_suggestion_approve(self, mock_post):
        """Test Photo.Suggestion.approve (flickr.photos.suggestions.approveSuggestion)"""  # noqa: E501
        # Empty response for approve operation
        mock_post.return_value = self._mock_response({})

        suggestion = f.Photo.Suggestion(id="12345")
        result = suggestion.approve()

        # Approve returns None
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
