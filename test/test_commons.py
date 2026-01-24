"""
Tests for Commons API methods.

flickr.commons.getInstitutions.
Uses example responses from the api-docs/ directory, converted from XML to JSON.
"""
import json
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler
from flickr_api.objects import CommonInstitution, CommonInstitutionUrl

from requests import Response

from test_utils import xml_to_flickr_json, load_api_doc


class TestCommonsMethods(unittest.TestCase):
    """Tests for CommonInstitution.getInstitutions"""

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
    def test_get_institutions(self, mock_post):
        """Test CommonInstitution.getInstitutions parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.commons.getInstitutions")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        institutions = CommonInstitution.getInstitutions()

        # Verify based on the example data - single institution
        self.assertEqual(len(institutions), 1)
        self.assertIsInstance(institutions[0], CommonInstitution)

        # Institution: nsid="123456@N01", date_launch="1232000000"
        institution = institutions[0]
        self.assertEqual(institution.id, "123456@N01")
        self.assertEqual(institution.nsid, "123456@N01")
        self.assertEqual(institution.date_launch, "1232000000")

        # Check name - note: clean_content converts {"_content": "..."} to just "..."
        self.assertEqual(institution.name, "Institution")

        # Check urls - list of CommonInstitutionUrl objects
        self.assertIsInstance(institution.urls, list)
        self.assertEqual(len(institution.urls), 3)
        self.assertIsInstance(institution.urls[0], CommonInstitutionUrl)

        # First url: type="site", url="http://example.com/"
        self.assertEqual(institution.urls[0].type, "site")
        self.assertEqual(institution.urls[0].url, "http://example.com/")

        # Second url: type="license"
        self.assertEqual(institution.urls[1].type, "license")
        self.assertEqual(institution.urls[1].url, "http://example.com/commons/license")

        # Third url: type="flickr"
        self.assertEqual(institution.urls[2].type, "flickr")
        self.assertEqual(institution.urls[2].url, "http://flickr.com/photos/institution")


if __name__ == "__main__":
    unittest.main()
