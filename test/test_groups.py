"""
Tests for Group API methods.

flickr.groups.getInfo, flickr.groups.search
Uses example responses from the api-docs/ directory.
"""
import json
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler

from requests import Response

from test_utils import xml_to_flickr_json, load_api_doc


class TestGroupMethods(unittest.TestCase):
    """Tests for Group-related API methods"""

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
    def test_group_get_info(self, mock_post):
        """Test Group.getInfo (flickr.groups.getInfo)"""
        api_doc = load_api_doc("flickr.groups.getInfo")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        group = f.Group(id="34427465497@N01")
        info = group.getInfo()

        # getInfo returns a dict of group attributes
        # Note: members/privacy are strings since getInfo returns raw dict,
        # not a Group object with converters applied
        self.assertEqual(info["id"], "34427465497@N01")
        self.assertEqual(info["name"], "GNEverybody")
        self.assertEqual(info["description"], "The group for GNE players")
        self.assertEqual(info["members"], "69")
        self.assertEqual(info["privacy"], "3")
        self.assertEqual(info["ispoolmoderated"], 0)

        # Verify throttle info
        self.assertIn("throttle", info)
        self.assertEqual(info["throttle"]["count"], "10")
        self.assertEqual(info["throttle"]["mode"], "month")

        # Verify restrictions info
        self.assertIn("restrictions", info)
        self.assertEqual(info["restrictions"]["photos_ok"], 1)
        self.assertEqual(info["restrictions"]["videos_ok"], 1)

    @patch.object(method_call.requests, "post")
    def test_group_search(self, mock_post):
        """Test Group.search (flickr.groups.search)"""
        api_doc = load_api_doc("flickr.groups.search")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        groups = f.Group.search(text="test")

        # Verify we got 5 groups
        self.assertEqual(len(groups), 5)

        # First group
        g1 = groups[0]
        self.assertIsInstance(g1, f.Group)
        self.assertEqual(g1.id, "3000@N02")
        self.assertEqual(g1.name, "Frito's Test Group")
        self.assertFalse(g1.eighteenplus)

        # Second group
        g2 = groups[1]
        self.assertEqual(g2.id, "32825757@N00")
        self.assertEqual(g2.name, "Free for All")

        # Verify pagination info
        self.assertEqual(groups.info.page, 1)
        self.assertEqual(groups.info.pages, 14)
        self.assertEqual(groups.info.total, 67)


if __name__ == "__main__":
    unittest.main()
