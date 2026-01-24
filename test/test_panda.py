"""
Tests for Panda API methods.

flickr.panda.getList, flickr.panda.getPhotos
Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPandaMethods(FlickrApiTestCase):
    """Tests for Panda-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_panda_get_list(self, mock_post):
        """Test Panda.getList (flickr.panda.getList)"""
        # The library expects panda names as strings in the list,
        # so we create the response format that matches Flickr's JSON API
        json_response = {
            "pandas": {
                "panda": [
                    {"_content": "ling ling"},
                    {"_content": "hsing hsing"},
                    {"_content": "wang wang"}
                ]
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        pandas = f.Panda.getList()

        # Verify we got 3 pandas
        self.assertEqual(len(pandas), 3)

        # First panda - clean_content extracts the string from {"_content": "..."}
        p1 = pandas[0]
        self.assertIsInstance(p1, f.Panda)
        self.assertEqual(p1.name, "ling ling")
        self.assertEqual(p1.id, "ling ling")

        # Second panda
        p2 = pandas[1]
        self.assertEqual(p2.name, "hsing hsing")

        # Third panda
        p3 = pandas[2]
        self.assertEqual(p3.name, "wang wang")

    @patch.object(method_call.requests, "post")
    def test_panda_get_photos(self, mock_post):
        """Test Panda.getPhotos (flickr.panda.getPhotos)"""
        api_doc = load_api_doc("flickr.panda.getPhotos")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        panda = f.Panda(name="ling ling", id="ling ling")
        photos = panda.getPhotos()

        # Verify we got 2 photos
        self.assertEqual(len(photos), 2)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "3313428913")
        self.assertEqual(p1.title, "Shorebirds at Pillar Point")
        self.assertEqual(p1.secret, "2cd3cb44cb")
        self.assertEqual(p1.server, "3609")
        self.assertEqual(p1.farm, "4")
        self.assertEqual(p1.owner.id, "72442527@N00")
        self.assertEqual(p1.ownername, "Pat Ulrich")

        # Second photo
        p2 = photos[1]
        self.assertEqual(p2.id, "3313713993")
        self.assertEqual(p2.title, "Battle of the sky")
        self.assertEqual(p2.secret, "3f7f51500f")
        self.assertEqual(p2.server, "3382")
        self.assertEqual(p2.owner.id, "10459691@N05")
        self.assertEqual(p2.ownername, "Sven Ericsson")

        # Verify pagination info
        self.assertEqual(photos.info.total, 120)
        self.assertEqual(photos.info.panda, "ling ling")
        self.assertEqual(photos.info.interval, "60000")
        self.assertEqual(photos.info.lastupdate, "1235765058272")


if __name__ == "__main__":
    unittest.main()
