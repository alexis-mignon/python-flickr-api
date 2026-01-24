"""
Tests for Photo People API methods.

Batch 14:
flickr.photos.people.add
flickr.photos.people.delete
flickr.photos.people.deleteCoords
flickr.photos.people.editCoords
flickr.photos.people.getList

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPhotoPeopleMethods(FlickrApiTestCase):
    """Tests for Photo People API methods"""

    @patch.object(method_call.requests, "post")
    def test_photo_add_person(self, mock_post):
        """Test Photo.addPerson (flickr.photos.people.add)"""
        # Empty response for add operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345678")
        result = photo.addPerson(user_id="87944415@N00")

        # Add returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_add_person_with_coords(self, mock_post):
        """Test Photo.addPerson with coordinates (flickr.photos.people.add)"""
        # Empty response for add operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345678")
        result = photo.addPerson(
            user_id="87944415@N00",
            person_x=50, person_y=50, person_w=100, person_h=100
        )

        # Add returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_delete_person(self, mock_post):
        """Test Photo.deletePerson (flickr.photos.people.delete)"""
        # Empty response for delete operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345678")
        result = photo.deletePerson(user_id="87944415@N00")

        # Delete returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_delete_person_coords(self, mock_post):
        """Test Photo.deletePersonCoords (flickr.photos.people.deleteCoords)"""
        # Empty response for deleteCoords operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345678")
        result = photo.deletePersonCoords(user_id="87944415@N00")

        # DeleteCoords returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_edit_person_coords(self, mock_post):
        """Test Photo.editPersonCoords (flickr.photos.people.editCoords)"""
        # Empty response for editCoords operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345678")
        result = photo.editPersonCoords(
            user_id="87944415@N00",
            person_x=100, person_y=100, person_w=150, person_h=150
        )

        # EditCoords returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_get_people(self, mock_post):
        """Test Photo.getPeople (flickr.photos.people.getList)"""
        api_doc = load_api_doc("flickr.photos.people.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="12345678")
        people = photo.getPeople()

        # Verify we got a list of people
        self.assertIsInstance(people, list)
        self.assertEqual(len(people), 1)

        # Verify person attributes
        person = people[0]
        self.assertIsInstance(person, f.Person)
        self.assertEqual(person.id, "87944415@N00")
        self.assertEqual(person.username, "hitherto")
        self.assertEqual(person.iconserver, 1)
        self.assertEqual(person.iconfarm, 1)
        self.assertEqual(person.realname, "Simon Batistoni")
        self.assertEqual(person.added_by, "12037949754@N01")
        self.assertEqual(person.x, "50")
        self.assertEqual(person.y, "50")
        self.assertEqual(person.w, "100")
        self.assertEqual(person.h, "100")
        self.assertEqual(person.photo, photo)


if __name__ == "__main__":
    unittest.main()
