"""
Tests for Photo geo-related API methods.

Batch 13 (partial):
flickr.photos.geo.batchCorrectLocation, flickr.photos.geo.correctLocation,
flickr.photos.geo.getLocation, flickr.photos.geo.getPerms,
flickr.photos.geo.photosForLocation, flickr.photos.geo.removeLocation,
flickr.photos.geo.setContext, flickr.photos.geo.setLocation,
flickr.photos.geo.setPerms

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call
from flickr_api.objects import Location, PhotoGeoPerms

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPhotoGeoMethods(FlickrApiTestCase):
    """Tests for Photo geo-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_person_batch_correct_location(self, mock_post):
        """Test Person.batchCorrectLocation
        (flickr.photos.geo.batchCorrectLocation)"""
        # Empty response for batch correction operation
        mock_post.return_value = self._mock_response({})

        person = f.Person(id="12345678@N00")
        result = person.batchCorrectLocation(
            lat=-17.685895,
            lon=-63.36914,
            accuracy=6,
            place_id="WM3JEXSbBZqqRtGA"
        )

        # Batch correction returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_correct_location(self, mock_post):
        """Test Photo.correctLocation (flickr.photos.geo.correctLocation)"""
        # Empty response for correct location operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.correctLocation(place_id="WM3JEXSbBZqqRtGA")

        # Correct location returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_get_location(self, mock_post):
        """Test Photo.getLocation (flickr.photos.geo.getLocation)"""
        api_doc = load_api_doc("flickr.photos.geo.getLocation")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="123")
        location = photo.getLocation()

        # Verify Location object is returned
        self.assertIsInstance(location, Location)
        self.assertEqual(location.latitude, -17.685895)
        self.assertEqual(location.longitude, -63.36914)
        self.assertEqual(location.accuracy, 6)

        # Verify photo reference is set
        self.assertEqual(location.photo, photo)

    @patch.object(method_call.requests, "post")
    def test_photo_get_geo_perms(self, mock_post):
        """Test Photo.getGeoPerms (flickr.photos.geo.getPerms)"""
        api_doc = load_api_doc("flickr.photos.geo.getPerms")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="10592")
        perms = photo.getGeoPerms()

        # Verify PhotoGeoPerms object is returned
        self.assertIsInstance(perms, PhotoGeoPerms)
        self.assertEqual(perms.id, "10592")
        self.assertFalse(perms.ispublic)
        self.assertFalse(perms.iscontact)
        self.assertFalse(perms.isfriend)
        self.assertTrue(perms.isfamily)

    @patch.object(method_call.requests, "post")
    def test_photo_photos_for_location(self, mock_post):
        """Test Photo.photosForLocation (flickr.photos.geo.photosForLocation)"""
        api_doc = load_api_doc("flickr.photos.geo.photosForLocation")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photos = f.Photo.photosForLocation(lat=-17.685895, lon=-63.36914)

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo - public
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        self.assertIsInstance(p1.owner, f.Person)
        self.assertEqual(p1.owner.id, "47058503995@N01")
        self.assertEqual(p1.secret, "a123456")
        self.assertEqual(p1.server, "2")
        self.assertEqual(p1.title, "test_04")
        self.assertTrue(p1.ispublic)
        self.assertFalse(p1.isfriend)
        self.assertFalse(p1.isfamily)

        # Second photo - private (friend & family)
        p2 = photos[1]
        self.assertEqual(p2.id, "2635")
        self.assertEqual(p2.owner.id, "47058503995@N01")
        self.assertEqual(p2.title, "test_03")
        self.assertFalse(p2.ispublic)
        self.assertTrue(p2.isfriend)
        self.assertTrue(p2.isfamily)

        # Third photo
        p3 = photos[2]
        self.assertEqual(p3.id, "2633")
        self.assertEqual(p3.title, "test_01")

        # Fourth photo - different owner
        p4 = photos[3]
        self.assertEqual(p4.id, "2610")
        self.assertEqual(p4.owner.id, "12037949754@N01")
        self.assertEqual(p4.title, "00_tall")

        # Verify pagination info
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.pages, 89)
        self.assertEqual(photos.info.perpage, 10)
        self.assertEqual(photos.info.total, 881)

    @patch.object(method_call.requests, "post")
    def test_photo_remove_location(self, mock_post):
        """Test Photo.removeLocation (flickr.photos.geo.removeLocation)"""
        # Empty response for remove location operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.removeLocation()

        # Remove location returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_context(self, mock_post):
        """Test Photo.setContext (flickr.photos.geo.setContext)"""
        # Empty response for set context operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        # context: 0=not defined, 1=indoors, 2=outdoors
        result = photo.setContext(context=2)

        # Set context returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_location(self, mock_post):
        """Test Photo.setLocation (flickr.photos.geo.setLocation)"""
        # Empty response for set location operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.setLocation(lat=-17.685895, lon=-63.36914, accuracy=6)

        # Set location returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_geo_perms(self, mock_post):
        """Test Photo.setGeoPerms (flickr.photos.geo.setPerms)"""
        # Empty response for set geo perms operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.setGeoPerms(
            is_public=0,
            is_contact=0,
            is_friend=0,
            is_family=1
        )

        # Set geo perms returns None
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
