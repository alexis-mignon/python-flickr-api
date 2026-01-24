"""
Tests for URLs API methods.

Batch 24:
flickr.urls.getGroup, flickr.urls.getUserPhotos, flickr.urls.getUserProfile,
flickr.urls.lookupGallery, flickr.urls.lookupGroup, flickr.urls.lookupUser

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call
from flickr_api.objects import Gallery, Group, Person

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestUrlsMethods(FlickrApiTestCase):
    """Tests for URLs API methods"""

    @patch.object(method_call.requests, "post")
    def test_get_group_url(self, mock_post):
        """Test Group.getUrl (flickr.urls.getGroup)"""
        api_doc = load_api_doc("flickr.urls.getGroup")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        group = Group(id="48508120860@N01")
        result = group.getUrl()

        # Returns the URL string directly
        self.assertIsInstance(result, str)
        self.assertEqual(result, "http://www.flickr.com/groups/test1/")

    @patch.object(method_call.requests, "post")
    def test_get_user_photos_url(self, mock_post):
        """Test Person.getPhotosUrl (flickr.urls.getUserPhotos)"""
        api_doc = load_api_doc("flickr.urls.getUserPhotos")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = Person(id="12037949754@N01")
        result = person.getPhotosUrl()

        # Returns the URL string directly
        self.assertIsInstance(result, str)
        self.assertEqual(result, "http://www.flickr.com/photos/bees/")

    @patch.object(method_call.requests, "post")
    def test_get_user_profile_url(self, mock_post):
        """Test Person.getProfileUrl (flickr.urls.getUserProfile)"""
        api_doc = load_api_doc("flickr.urls.getUserProfile")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = Person(id="12037949754@N01")
        result = person.getProfileUrl()

        # Returns the URL string directly
        self.assertIsInstance(result, str)
        self.assertEqual(result, "http://www.flickr.com/people/bees/")

    @patch.object(method_call.requests, "post")
    def test_lookup_gallery(self, mock_post):
        """Test Gallery.getByUrl (flickr.urls.lookupGallery)"""
        api_doc = load_api_doc("flickr.urls.lookupGallery")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = Gallery.getByUrl(
            url="/photos/straup/galleries/72157617483228192"
        )

        # Returns a Gallery object
        self.assertIsInstance(result, Gallery)
        self.assertEqual(result.id, "6065-72157617483228192")
        self.assertEqual(
            result.url, "/photos/straup/galleries/72157617483228192"
        )
        # Owner is a Person object
        self.assertIsInstance(result.owner, Person)
        self.assertEqual(result.owner.id, "35034348999@N01")
        # Check other attributes
        self.assertEqual(result.primary_photo_id, "292882708")
        # count_photos and count_videos are converted to int by Gallery converter
        self.assertEqual(result.count_photos, 17)
        self.assertEqual(result.count_videos, 0)
        # Title is a plain string after clean_content transformation
        self.assertEqual(result.title,
                         "Cat Pictures I've Sent To Kevin Collins")

    @patch.object(method_call.requests, "post")
    def test_lookup_group(self, mock_post):
        """Test Group.getByUrl (flickr.urls.lookupGroup)"""
        api_doc = load_api_doc("flickr.urls.lookupGroup")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = Group.getByUrl(url="https://www.flickr.com/groups/central/")

        # Returns a Group object
        self.assertIsInstance(result, Group)
        self.assertEqual(result.id, "34427469792@N01")
        # groupname is converted to name by Group.getByUrl
        # and is a plain string after clean_content transformation
        self.assertEqual(result.name, "FlickrCentral")

    @patch.object(method_call.requests, "post")
    def test_lookup_user(self, mock_post):
        """Test Person.findByUrl (flickr.urls.lookupUser)"""
        api_doc = load_api_doc("flickr.urls.lookupUser")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = Person.findByUrl(url="https://www.flickr.com/people/stewart/")

        # Returns a Person object
        self.assertIsInstance(result, Person)
        self.assertEqual(result.id, "12037949632@N01")
        # Username is a plain string after clean_content transformation
        self.assertEqual(result.username, "Stewart")


if __name__ == "__main__":
    unittest.main()
