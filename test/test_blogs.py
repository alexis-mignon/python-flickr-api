"""
Tests for Blog API methods (flickr.blogs.getList, flickr.blogs.getServices,
flickr.blogs.postPhoto).

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


class TestBlogMethods(unittest.TestCase):
    """Tests for BlogService.getServices, BlogService.getList, and Blog.postPhoto"""

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
    def test_get_services(self, mock_post):
        """Test BlogService.getServices parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.blogs.getServices")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        services = f.BlogService.getServices()

        # Verify based on the example data
        self.assertEqual(len(services), 11)
        self.assertIsInstance(services[0], f.BlogService)

        # First service: id="beta.blogger.com", text="Blogger"
        # Note: _content is converted to "text" by clean_content() in method_call.py
        self.assertEqual(services[0].id, "beta.blogger.com")
        self.assertEqual(services[0].text, "Blogger")

        # Second service: id="Typepad", text="Typepad"
        self.assertEqual(services[1].id, "Typepad")
        self.assertEqual(services[1].text, "Typepad")

        # Last service: id="Twitter", text="Twitter"
        self.assertEqual(services[10].id, "Twitter")
        self.assertEqual(services[10].text, "Twitter")

    @patch.object(method_call.requests, "post")
    def test_get_list(self, mock_post):
        """Test BlogService.getList parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.blogs.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # BlogService.getList is an instance method, create a BlogService first
        service = f.BlogService(id="Typepad")
        blogs = service.getList()

        # Verify based on the example data
        self.assertEqual(len(blogs), 2)
        self.assertIsInstance(blogs[0], f.Blog)

        # First blog: id="73", name="Bloxus test", needspassword="0" -> False
        self.assertEqual(blogs[0].id, "73")
        self.assertEqual(blogs[0].name, "Bloxus test")
        self.assertEqual(blogs[0].needspassword, False)
        self.assertEqual(blogs[0].url, "http://remote.bloxus.com/")

        # Second blog: id="74", name="Manila Test", needspassword="1" -> True
        self.assertEqual(blogs[1].id, "74")
        self.assertEqual(blogs[1].name, "Manila Test")
        self.assertEqual(blogs[1].needspassword, True)
        self.assertEqual(blogs[1].url, "http://flickrtest1.userland.com/")

    @patch.object(method_call.requests, "post")
    def test_post_photo(self, mock_post):
        """Test Blog.postPhoto returns None for successful post"""
        # flickr.blogs.postPhoto has an empty response (write operation)
        # Create a minimal response with just stat="ok"
        mock_post.return_value = self._mock_response({})

        # Blog.postPhoto is an instance method, create a Blog first
        blog = f.Blog(id="73", name="Test Blog")
        result = blog.postPhoto(
            photo_id="12345",
            title="Test Post",
            description="Test post body"
        )

        # postPhoto returns None for successful write operations
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_blog_service_post_photo(self, mock_post):
        """Test BlogService.postPhoto returns None for successful post"""
        mock_post.return_value = self._mock_response({})

        service = f.BlogService(id="Typepad")
        result = service.postPhoto(
            photo_id="12345",
            title="Test Post",
            description="Test post body"
        )

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
