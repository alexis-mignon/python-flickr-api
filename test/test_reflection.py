"""
Tests for Reflection API methods.

Batch 21:
flickr.reflection.getMethodInfo, flickr.reflection.getMethods

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


class TestReflectionMethods(unittest.TestCase):
    """Tests for Reflection API methods"""

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
    def test_reflection_get_method_info(self, mock_post):
        """Test Reflection.getMethodInfo (flickr.reflection.getMethodInfo)"""
        api_doc = load_api_doc("flickr.reflection.getMethodInfo")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.Reflection.getMethodInfo(method_name="flickr.fakeMethod")

        # Verify the result is a dict containing method info
        self.assertIsInstance(result, dict)
        self.assertEqual(result["name"], "flickr.fakeMethod")
        self.assertEqual(result["needslogin"], 1)

        # Description (library flattens _content to string)
        self.assertIn("description", result)
        self.assertEqual(result["description"], "A fake method")

        # Response example
        self.assertIn("response", result)
        self.assertEqual(result["response"], "xml-response-example")

        # Explanation
        self.assertIn("explanation", result)
        self.assertEqual(result["explanation"], "explanation of example response")

        # Arguments
        self.assertIn("arguments", result)
        arguments = result["arguments"]["argument"]
        self.assertEqual(len(arguments), 2)

        # First argument - api_key (library renames _content to text)
        arg1 = arguments[0]
        self.assertEqual(arg1["name"], "api_key")
        self.assertEqual(arg1["optional"], 0)
        self.assertIn("text", arg1)

        # Second argument - color
        arg2 = arguments[1]
        self.assertEqual(arg2["name"], "color")
        self.assertEqual(arg2["optional"], 1)

        # Errors
        self.assertIn("errors", result)
        errors = result["errors"]["error"]
        self.assertEqual(len(errors), 2)

        # First error - Photo not found
        err1 = errors[0]
        self.assertEqual(err1["code"], 1)
        self.assertEqual(err1["message"], "Photo not found")

        # Second error - Invalid API Key
        err2 = errors[1]
        self.assertEqual(err2["code"], "100")
        self.assertEqual(err2["message"], "Invalid API Key")

    @patch.object(method_call.requests, "post")
    def test_reflection_get_methods(self, mock_post):
        """Test Reflection.getMethods (flickr.reflection.getMethods)"""
        api_doc = load_api_doc("flickr.reflection.getMethods")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.Reflection.getMethods()

        # Verify the result is a list of method names (strings)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 4)

        # Verify method names from the example
        self.assertIn("flickr.blogs.getList", result)
        self.assertIn("flickr.blogs.postPhoto", result)
        self.assertIn("flickr.contacts.getList", result)
        self.assertIn("flickr.contacts.getPublicList", result)


if __name__ == "__main__":
    unittest.main()
