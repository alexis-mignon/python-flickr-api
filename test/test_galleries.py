"""
Tests for Gallery API methods.

flickr.galleries.addPhoto, create, editMeta, editPhoto, editPhotos,
getInfo, getList, getListForPhoto, and getPhotos.
Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestGalleryMethods(FlickrApiTestCase):
    """Tests for Gallery-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_gallery_add_photo(self, mock_post):
        """Test Gallery.addPhoto (flickr.galleries.addPhoto)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        gallery = f.Gallery(id="6065-72157617483228192")
        photo = f.Photo(id="12345")
        result = gallery.addPhoto(photo=photo)

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_gallery_create(self, mock_post):
        """Test Gallery.create (flickr.galleries.create)"""
        api_doc = load_api_doc("flickr.galleries.create")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        gallery = f.Gallery.create(
            title="My Gallery",
            description="A test gallery"
        )

        self.assertIsInstance(gallery, f.Gallery)
        self.assertEqual(gallery.id, "50736-72157623680420409")
        self.assertEqual(
            gallery.url,
            "http://www.flickr.com/photos/kellan/galleries/72157623680420409"
        )

    @patch.object(method_call.requests, "post")
    def test_gallery_edit_meta(self, mock_post):
        """Test Gallery.editMedia (flickr.galleries.editMeta)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        gallery = f.Gallery(id="6065-72157617483228192")
        result = gallery.editMedia(title="New Title", description="New desc")

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_gallery_edit_photo(self, mock_post):
        """Test Gallery.editPhoto (flickr.galleries.editPhoto)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        gallery = f.Gallery(id="6065-72157617483228192")
        photo = f.Photo(id="12345")
        result = gallery.editPhoto(photo=photo, comment="Updated comment")

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_gallery_edit_photos(self, mock_post):
        """Test Gallery.editPhotos (flickr.galleries.editPhotos)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        gallery = f.Gallery(id="6065-72157617483228192")
        primary_photo = f.Photo(id="111")
        result = gallery.editPhotos(
            primary_photo=primary_photo,
            photo_ids=["111", "222", "333"]
        )

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_gallery_get_info(self, mock_post):
        """Test Gallery.getInfo (flickr.galleries.getInfo)"""
        api_doc = load_api_doc("flickr.galleries.getInfo")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        gallery = f.Gallery(id="6065-72157617483228192")
        info = gallery.getInfo()

        # getInfo returns a dict of updated attributes (counts stay as strings)
        self.assertEqual(info["id"], "6065-72157617483228192")
        self.assertEqual(info["count_photos"], "17")
        self.assertEqual(info["count_videos"], 0)  # "0" converted to int
        self.assertEqual(
            info["title"],
            "Cat Pictures I've Sent To Kevin Collins"
        )

        # Verify owner is a Person
        self.assertIsInstance(info["owner"], f.Person)
        self.assertEqual(info["owner"].id, "35034348999@N01")

        # Verify primary_photo is a Photo
        self.assertIsInstance(info["primary_photo"], f.Photo)
        self.assertEqual(info["primary_photo"].id, "292882708")

    @patch.object(method_call.requests, "post")
    def test_gallery_get_photos(self, mock_post):
        """Test Gallery.getPhotos (flickr.galleries.getPhotos)"""
        api_doc = load_api_doc("flickr.galleries.getPhotos")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        gallery = f.Gallery(id="6065-72157617483228192")
        photos = gallery.getPhotos()

        # Verify we got 2 photos
        self.assertEqual(len(photos), 2)
        self.assertIsInstance(photos[0], f.Photo)

        # First photo
        self.assertEqual(photos[0].id, "2822546461")
        self.assertEqual(photos[0].title, "FOO")
        self.assertTrue(photos[0].ispublic)
        self.assertFalse(photos[0].isfriend)
        self.assertFalse(photos[0].isfamily)

        # Second photo
        self.assertEqual(photos[1].id, "2822544806")
        self.assertEqual(photos[1].title, "OOK")

        # Verify pagination info
        self.assertEqual(photos.info.page, 1)
        self.assertEqual(photos.info.pages, 1)
        self.assertEqual(photos.info.total, 2)

    @patch.object(method_call.requests, "post")
    def test_person_get_galleries(self, mock_post):
        """Test Person.getGalleries (flickr.galleries.getList)"""
        api_doc = load_api_doc("flickr.galleries.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="34427469121@N01")
        galleries = person.getGalleries()

        # Verify we got 2 galleries
        self.assertEqual(len(galleries), 2)

        # First gallery - Gallery objects with converters applied
        g1 = galleries[0]
        self.assertIsInstance(g1, f.Gallery)
        self.assertEqual(g1.id, "5704-72157622637971865")
        self.assertEqual(g1.title, "I like me some black & white")
        self.assertEqual(g1.description, "black and whites")
        self.assertEqual(g1.count_photos, 16)  # Converted to int by Gallery converter
        self.assertEqual(g1.count_videos, 2)   # Converted to int by Gallery converter
        self.assertIsInstance(g1.owner, f.Person)

        # Second gallery
        g2 = galleries[1]
        self.assertIsInstance(g2, f.Gallery)
        self.assertEqual(g2.id, "5704-72157622566655097")
        self.assertEqual(g2.title, "People Sleeping in Libraries")
        self.assertEqual(g2.count_photos, 18)  # Converted to int by Gallery converter

        # Verify pagination info
        self.assertEqual(galleries.info.total, 9)
        self.assertEqual(galleries.info.page, 1)

    @patch.object(method_call.requests, "post")
    def test_photo_get_galleries(self, mock_post):
        """Test Photo.getGalleries (flickr.galleries.getListForPhoto)"""
        api_doc = load_api_doc("flickr.galleries.getListForPhoto")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="2080242123")
        galleries = photo.getGalleries()

        # Verify we got 2 galleries
        self.assertEqual(len(galleries), 2)

        # First gallery - Gallery objects with converters applied
        g1 = galleries[0]
        self.assertIsInstance(g1, f.Gallery)
        self.assertEqual(g1.id, "9634-72157621980433950")
        self.assertEqual(g1.title, "Vivitar Ultra Wide & Slim Selection")
        self.assertEqual(g1.count_photos, 18)  # Converted to int by Gallery converter

        # Second gallery
        g2 = galleries[1]
        self.assertIsInstance(g2, f.Gallery)
        self.assertEqual(g2.id, "22342631-72157622254010831")
        self.assertEqual(g2.title, "Awesome Pics")

        # Verify pagination info
        self.assertEqual(galleries.info.total, 7)


if __name__ == "__main__":
    unittest.main()
