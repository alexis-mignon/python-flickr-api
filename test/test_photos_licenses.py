"""
Tests for License API methods.

Batch 13 (partial):
flickr.photos.licenses.getInfo

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


class TestLicenseMethods(unittest.TestCase):
    """Tests for License API methods"""

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
    def test_license_get_list(self, mock_post):
        """Test License.getList (flickr.photos.licenses.getInfo)"""
        api_doc = load_api_doc("flickr.photos.licenses.getInfo")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        licenses = f.License.getList()

        # Verify we got 17 licenses (0-16)
        self.assertEqual(len(licenses), 17)

        # Verify first license (All Rights Reserved)
        # Note: IDs "0" and "1" are converted to integers by xml_to_flickr_json
        l0 = licenses[0]
        self.assertIsInstance(l0, f.License)
        self.assertEqual(l0.id, 0)
        self.assertEqual(l0.name, "All Rights Reserved")
        self.assertEqual(
            l0.url,
            "https://www.flickrhelp.com/hc/en-us/articles/"
            "10710266545556-Using-Flickr-images-shared-by-other-members"
        )

        # Verify a Creative Commons license
        l1 = licenses[1]
        self.assertEqual(l1.id, 1)
        self.assertEqual(l1.name, "CC BY-NC-SA 2.0")
        self.assertEqual(
            l1.url,
            "https://creativecommons.org/licenses/by-nc-sa/2.0/"
        )

        # Verify CC BY 2.0
        l4 = licenses[4]
        self.assertEqual(l4.id, "4")
        self.assertEqual(l4.name, "CC BY 2.0")
        self.assertEqual(l4.url, "https://creativecommons.org/licenses/by/2.0/")

        # Verify Public Domain Dedication (CC0)
        l9 = licenses[9]
        self.assertEqual(l9.id, "9")
        self.assertEqual(l9.name, "Public Domain Dedication (CC0)")
        self.assertEqual(
            l9.url,
            "https://creativecommons.org/publicdomain/zero/1.0/"
        )

        # Verify last license (CC BY-NC-ND 4.0)
        l16 = licenses[16]
        self.assertEqual(l16.id, "16")
        self.assertEqual(l16.name, "CC BY-NC-ND 4.0")
        self.assertEqual(
            l16.url,
            "https://creativecommons.org/licenses/by-nc-nd/4.0/"
        )


    @patch.object(method_call.requests, "post")
    def test_photo_set_license(self, mock_post):
        """Test Photo.setLicence (flickr.photos.licenses.setLicense)"""
        # Empty response for setLicense operation
        json_data = {"stat": "ok"}
        resp = Response()
        resp.status_code = 200
        resp._content = json.dumps(json_data).encode("utf-8")
        mock_post.return_value = resp

        photo = f.Photo(id="12345678")

        # Test with license_id directly
        result = photo.setLicence(licence=4)
        self.assertIsNone(result)

        # Test with a License object
        license_obj = f.License(id=4, name="CC BY 2.0")
        result = photo.setLicence(licence=license_obj)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
