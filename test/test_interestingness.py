"""
Tests for Interestingness API methods.

flickr.interestingness.getList
Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestInterestingnessMethods(FlickrApiTestCase):
    """Tests for Interestingness-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_photo_get_interesting(self, mock_post):
        """Test Photo.getInteresting (flickr.interestingness.getList)"""
        api_doc = load_api_doc("flickr.interestingness.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photos = f.Photo.getInteresting()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo (public)
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        self.assertEqual(p1.owner.id, "47058503995@N01")
        self.assertEqual(p1.secret, "a123456")
        self.assertEqual(p1.server, "2")
        self.assertEqual(p1.title, "test_04")
        self.assertTrue(p1.ispublic)
        self.assertFalse(p1.isfriend)
        self.assertFalse(p1.isfamily)

        # Second photo (private, friends/family visible)
        p2 = photos[1]
        self.assertEqual(p2.id, "2635")
        self.assertEqual(p2.title, "test_03")
        self.assertFalse(p2.ispublic)
        self.assertTrue(p2.isfriend)
        self.assertTrue(p2.isfamily)

        # Fourth photo (different owner)
        p4 = photos[3]
        self.assertEqual(p4.id, "2610")
        self.assertEqual(p4.owner.id, "12037949754@N01")
        self.assertEqual(p4.title, "00_tall")

        # Verify pagination info
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.pages, 89)
        self.assertEqual(photos.info.perpage, 10)
        self.assertEqual(photos.info.total, 881)


if __name__ == "__main__":
    unittest.main()
