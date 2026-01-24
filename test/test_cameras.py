"""
Tests for Camera API methods.

flickr.cameras.getBrands and flickr.cameras.getBrandModels.
Uses example responses from the api-docs/ directory, converted from XML to JSON.
"""
import json
import os
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler

from requests import Response


def xml_to_flickr_json(xml_string):
    """
    Convert Flickr XML response format to the JSON format the API returns.

    Flickr's JSON format:
    - Element text content becomes "_content"
    - Attributes become properties
    - Repeated elements become arrays
    - Single elements stay as objects
    - If root is <rsp>, unwrap it to match JSON API format
    """
    # Clean up XML string
    xml_string = xml_string.strip()
    root = ET.fromstring(xml_string)

    def element_to_dict(elem):
        result = {}

        # Add attributes
        for key, value in elem.attrib.items():
            result[key] = value

        # Add text content if present
        if elem.text and elem.text.strip():
            result["_content"] = elem.text.strip()

        # Group children by tag name
        children_by_tag = {}
        for child in elem:
            tag = child.tag
            if tag not in children_by_tag:
                children_by_tag[tag] = []
            children_by_tag[tag].append(element_to_dict(child))

        # Add children to result
        for tag, children in children_by_tag.items():
            # Flickr API returns arrays for repeated elements, single object otherwise
            if len(children) == 1:
                result[tag] = children[0]
            else:
                result[tag] = children

        return result

    # Convert root element
    root_dict = element_to_dict(root)

    # If root is <rsp>, unwrap it (JSON API returns content directly without rsp wrapper)
    if root.tag == "rsp":
        return root_dict
    else:
        # Wrap in root tag name
        return {root.tag: root_dict}


def load_api_doc(method_name):
    """Load API documentation JSON file for a method."""
    api_docs_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "api-docs"
    )
    filepath = os.path.join(api_docs_dir, f"{method_name}.json")
    with open(filepath, "r") as f:
        return json.load(f)


class TestCameraMethods(unittest.TestCase):
    """Tests for Camera.Brand.getList and Camera.Brand.getModels"""

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
    def test_get_brands(self, mock_post):
        """Test Camera.Brand.getList parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.cameras.getBrands")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        brands = f.Camera.Brand.getList()

        # Verify based on the example data
        self.assertEqual(len(brands), 3)
        self.assertIsInstance(brands[0], f.Camera.Brand)

        # First brand: id="canon", text="Canon"
        self.assertEqual(brands[0].id, "canon")
        self.assertEqual(brands[0].text, "Canon")

        # Second brand: id="nikon", text="Nikon"
        self.assertEqual(brands[1].id, "nikon")
        self.assertEqual(brands[1].text, "Nikon")

        # Third brand: id="apple", text="Apple"
        self.assertEqual(brands[2].id, "apple")
        self.assertEqual(brands[2].text, "Apple")

    @patch.object(method_call.requests, "post")
    def test_get_brand_models(self, mock_post):
        """Test Camera.Brand.getModels parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.cameras.getBrandModels")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # Camera.Brand.getModels is an instance method
        brand = f.Camera.Brand(id="apple")
        models = brand.getModels()

        # Verify based on the example data - single camera
        self.assertEqual(len(models), 1)
        self.assertIsInstance(models[0], f.Camera)

        # Camera: id="iphone_9000", name="iPhone 9000"
        # Note: clean_content converts {"_content": "..."} to just "..."
        camera = models[0]
        self.assertEqual(camera.id, "iphone_9000")
        self.assertEqual(camera.name, "iPhone 9000")

        # Check details - nested dicts with _content are converted to strings
        self.assertEqual(camera.details["megapixels"], "22.0")
        self.assertEqual(camera.details["zoom"], "3.0")
        self.assertEqual(camera.details["lcd_size"], "40.5")
        self.assertEqual(camera.details["storage_type"], "Flash")

        # Check images - small and large URLs
        self.assertIn("small", camera.images)
        self.assertIn("large", camera.images)


if __name__ == "__main__":
    unittest.main()
