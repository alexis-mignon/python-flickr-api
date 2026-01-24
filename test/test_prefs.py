"""
Tests for prefs API methods.

Batch 20:
flickr.prefs.getContentType, flickr.prefs.getGeoPerms,
flickr.prefs.getHidden, flickr.prefs.getPrivacy,
flickr.prefs.getSafetyLevel

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPrefsMethods(FlickrApiTestCase):
    """Tests for prefs API methods"""

    @patch.object(method_call.requests, "post")
    def test_prefs_get_content_type(self, mock_post):
        """Test prefs.getContentType (flickr.prefs.getContentType)"""
        api_doc = load_api_doc("flickr.prefs.getContentType")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        content_type = f.prefs.getContentType()

        # Returns the content_type value directly
        self.assertEqual(content_type, 1)

    @patch.object(method_call.requests, "post")
    def test_prefs_get_geo_perms(self, mock_post):
        """Test prefs.getGeoPerms (flickr.prefs.getGeoPerms)"""
        api_doc = load_api_doc("flickr.prefs.getGeoPerms")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        geo_perms = f.prefs.getGeoPerms()

        # Returns the person dict with geoperms and importgeoexif
        self.assertIsInstance(geo_perms, dict)
        self.assertEqual(geo_perms["nsid"], "12037949754@N01")
        self.assertEqual(geo_perms["geoperms"], 1)
        self.assertEqual(geo_perms["importgeoexif"], 0)

    @patch.object(method_call.requests, "post")
    def test_prefs_get_hidden(self, mock_post):
        """Test prefs.getHidden (flickr.prefs.getHidden)"""
        api_doc = load_api_doc("flickr.prefs.getHidden")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        hidden = f.prefs.getHidden()

        # Returns a boolean (converted from the hidden value)
        self.assertIsInstance(hidden, bool)
        self.assertTrue(hidden)

    @patch.object(method_call.requests, "post")
    def test_prefs_get_privacy(self, mock_post):
        """Test prefs.getPrivacy (flickr.prefs.getPrivacy)"""
        api_doc = load_api_doc("flickr.prefs.getPrivacy")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        privacy = f.prefs.getPrivacy()

        # Returns the privacy level value (1 = Public)
        self.assertEqual(privacy, 1)

    @patch.object(method_call.requests, "post")
    def test_prefs_get_safety_level(self, mock_post):
        """Test prefs.getSafetyLevel (flickr.prefs.getSafetyLevel)"""
        api_doc = load_api_doc("flickr.prefs.getSafetyLevel")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        safety_level = f.prefs.getSafetyLevel()

        # Returns the safety_level value (1 = Safe)
        self.assertEqual(safety_level, 1)


if __name__ == "__main__":
    unittest.main()
