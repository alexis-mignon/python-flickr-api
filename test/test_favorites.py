"""
Tests for Favorites API methods.

flickr.favorites.add, flickr.favorites.getContext, flickr.favorites.getList,
flickr.favorites.getPublicList, and flickr.favorites.remove.
Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestFavoritesMethods(FlickrApiTestCase):
    """Tests for favorites-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_photo_add_to_favorites(self, mock_post):
        """Test Photo.addToFavorites (flickr.favorites.add)"""
        # This is a write operation with empty response
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.addToFavorites()

        # Write operations return None
        self.assertIsNone(result)

        # Verify the API was called
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_person_get_favorite_context(self, mock_post):
        """Test Person.getFavoriteContext (flickr.favorites.getContext)"""
        api_doc = load_api_doc("flickr.favorites.getContext")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="12345678@N01")
        photo = f.Photo(id="2981")
        prev_photo, next_photo = person.getFavoriteContext(photo=photo)

        # Verify prev photo
        self.assertIsInstance(prev_photo, f.Photo)
        self.assertEqual(prev_photo.id, "2980")
        self.assertEqual(prev_photo.secret, "973da1e709")
        self.assertEqual(prev_photo.title, "boo!")

        # Verify next photo
        self.assertIsInstance(next_photo, f.Photo)
        self.assertEqual(next_photo.id, "2985")
        self.assertEqual(next_photo.secret, "059b664012")
        self.assertEqual(next_photo.title, "Amsterdam Amstel")

    @patch.object(method_call.requests, "post")
    def test_photo_get_favorite_context(self, mock_post):
        """Test Photo.getFavoriteContext (flickr.favorites.getContext)"""
        api_doc = load_api_doc("flickr.favorites.getContext")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="2981")
        user = f.Person(id="12345678@N01")
        prev_photo, next_photo = photo.getFavoriteContext(user=user)

        # Verify prev photo
        self.assertIsInstance(prev_photo, f.Photo)
        self.assertEqual(prev_photo.id, "2980")

        # Verify next photo
        self.assertIsInstance(next_photo, f.Photo)
        self.assertEqual(next_photo.id, "2985")

    @patch.object(method_call.requests, "post")
    def test_person_get_favorites(self, mock_post):
        """Test Person.getFavorites (flickr.favorites.getList)"""
        api_doc = load_api_doc("flickr.favorites.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="47058503995@N01")
        favorites = person.getFavorites()

        # Verify we got 4 photos
        self.assertEqual(len(favorites), 4)
        self.assertIsInstance(favorites[0], f.Photo)

        # Check first photo
        self.assertEqual(favorites[0].id, "2636")
        self.assertEqual(favorites[0].secret, "a123456")
        self.assertEqual(favorites[0].title, "test_04")
        self.assertTrue(favorites[0].ispublic)
        self.assertFalse(favorites[0].isfriend)
        self.assertFalse(favorites[0].isfamily)

        # Check second photo (private but friend/family)
        self.assertEqual(favorites[1].id, "2635")
        self.assertEqual(favorites[1].title, "test_03")
        self.assertFalse(favorites[1].ispublic)
        self.assertTrue(favorites[1].isfriend)
        self.assertTrue(favorites[1].isfamily)

        # Check pagination info
        self.assertEqual(favorites.info.page, 2)
        self.assertEqual(favorites.info.pages, 89)
        self.assertEqual(favorites.info.perpage, 10)
        self.assertEqual(favorites.info.total, 881)

    @patch.object(method_call.requests, "post")
    def test_person_get_public_favorites(self, mock_post):
        """Test Person.getPublicFavorites (flickr.favorites.getPublicList)"""
        api_doc = load_api_doc("flickr.favorites.getPublicList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="47058503995@N01")
        favorites = person.getPublicFavorites()

        # Same response format as getList
        self.assertEqual(len(favorites), 4)
        self.assertIsInstance(favorites[0], f.Photo)
        self.assertEqual(favorites[0].id, "2636")
        self.assertEqual(favorites[2].id, "2633")
        self.assertEqual(favorites[3].id, "2610")

    @patch.object(method_call.requests, "post")
    def test_person_remove_from_favorites(self, mock_post):
        """Test Person.removeFromFavorites (flickr.favorites.remove)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        person = f.Person(id="12345678@N01")
        photo = f.Photo(id="12345")
        result = person.removeFromFavorites(photo=photo)

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_photo_remove_from_favorites(self, mock_post):
        """Test Photo.removeFromFavorites (flickr.favorites.remove)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.removeFromFavorites()

        self.assertIsNone(result)
        mock_post.assert_called_once()


if __name__ == "__main__":
    unittest.main()
