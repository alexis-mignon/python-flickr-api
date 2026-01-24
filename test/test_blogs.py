"""
Tests for Blog API methods (flickr.blogs.getList, flickr.blogs.getServices,
flickr.blogs.postPhoto).

Uses example responses from the api-docs/ directory, converted from XML to JSON.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestBlogMethods(FlickrApiTestCase):
    """Tests for BlogService.getServices, BlogService.getList, and Blog.postPhoto"""

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
