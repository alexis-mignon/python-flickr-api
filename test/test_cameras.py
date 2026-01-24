"""
Tests for Camera API methods.

flickr.cameras.getBrands and flickr.cameras.getBrandModels.
Uses example responses from the api-docs/ directory, converted from XML to JSON.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestCameraMethods(FlickrApiTestCase):
    """Tests for Camera.Brand.getList and Camera.Brand.getModels"""

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
