"""
Tests for Photo.Suggestion API methods.

Batch 14:
flickr.photos.suggestions.approveSuggestion

Batch 15:
flickr.photos.suggestions.getList, flickr.photos.suggestions.rejectSuggestion,
flickr.photos.suggestions.removeSuggestion, flickr.photos.suggestions.suggestLocation

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase


class TestPhotoSuggestionMethods(FlickrApiTestCase):
    """Tests for Photo.Suggestion API methods"""

    @patch.object(method_call.requests, "post")
    def test_photo_suggestion_approve(self, mock_post):
        """Test Photo.Suggestion.approve (flickr.photos.suggestions.approveSuggestion)"""  # noqa: E501
        # Empty response for approve operation
        mock_post.return_value = self._mock_response({})

        suggestion = f.Photo.Suggestion(id="12345")
        result = suggestion.approve()

        # Approve returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_get_suggestions(self, mock_post):
        """Test Photo.getSuggestions (flickr.photos.suggestions.getList)"""
        # Construct JSON response with suggestions
        json_response = {
            "suggestions": {
                "photo_id": "12345",
                "suggestion": [
                    {
                        "id": "1001",
                        "photo_id": "12345",
                        "suggested_by": "12037949754@N01",
                        "status": 0,
                        "date_suggested": "1234567890",
                        "latitude": "37.792",
                        "longitude": "-122.394",
                        "accuracy": "16",
                        "note": "This is Golden Gate Park"
                    },
                    {
                        "id": "1002",
                        "photo_id": "12345",
                        "suggested_by": "33853651809@N01",
                        "status": 0,
                        "date_suggested": "1234568000",
                        "latitude": "37.788",
                        "longitude": "-122.407",
                        "accuracy": "15"
                    }
                ],
                "total": "2"
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="12345")
        suggestions = photo.getSuggestions()

        # Verify we got 2 suggestions
        self.assertEqual(len(suggestions), 2)

        # First suggestion
        s1 = suggestions[0]
        self.assertIsInstance(s1, f.Photo.Suggestion)
        self.assertEqual(s1.id, "1001")
        # photo_id is converted to Photo object
        self.assertIsInstance(s1.photo, f.Photo)
        self.assertEqual(s1.photo.id, "12345")
        # suggested_by is converted to Person object
        self.assertIsInstance(s1.suggested_by, f.Person)
        self.assertEqual(s1.suggested_by.id, "12037949754@N01")
        self.assertEqual(s1.status, 0)
        self.assertEqual(s1.latitude, "37.792")
        self.assertEqual(s1.longitude, "-122.394")
        self.assertEqual(s1.accuracy, "16")
        self.assertEqual(s1.note, "This is Golden Gate Park")

        # Second suggestion (no note)
        s2 = suggestions[1]
        self.assertEqual(s2.id, "1002")
        self.assertEqual(s2.suggested_by.id, "33853651809@N01")
        self.assertEqual(s2.latitude, "37.788")
        self.assertEqual(s2.longitude, "-122.407")

    @patch.object(method_call.requests, "post")
    def test_photo_suggestion_reject(self, mock_post):
        """Test Photo.Suggestion.reject (flickr.photos.suggestions.rejectSuggestion)"""  # noqa: E501
        # Empty response for reject operation
        mock_post.return_value = self._mock_response({})

        suggestion = f.Photo.Suggestion(id="12345")
        result = suggestion.reject()

        # Reject returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_suggestion_remove(self, mock_post):
        """Test Photo.Suggestion.remove (flickr.photos.suggestions.removeSuggestion)"""  # noqa: E501
        # Empty response for remove operation
        mock_post.return_value = self._mock_response({})

        suggestion = f.Photo.Suggestion(id="12345")
        result = suggestion.remove()

        # Remove returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_suggest_location(self, mock_post):
        """Test Photo.suggestLocation (flickr.photos.suggestions.suggestLocation)"""  # noqa: E501
        # Response with suggestion info
        json_response = {
            "suggestions": {
                "suggestion": [
                    {
                        "id": "2001",
                        "photo_id": "98765",
                        "suggested_by": "12037949754@N01",
                        "status": 0,
                        "date_suggested": "1234567890",
                        "latitude": "37.792",
                        "longitude": "-122.394",
                        "accuracy": "16"
                    }
                ],
                "total": "1"
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="98765")
        suggestions = photo.suggestLocation(lat=37.792, lon=-122.394)

        # Verify we got the suggestion back
        self.assertEqual(len(suggestions), 1)

        s1 = suggestions[0]
        self.assertIsInstance(s1, f.Photo.Suggestion)
        self.assertEqual(s1.id, "2001")
        self.assertEqual(s1.latitude, "37.792")
        self.assertEqual(s1.longitude, "-122.394")


if __name__ == "__main__":
    unittest.main()
