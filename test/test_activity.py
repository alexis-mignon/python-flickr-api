"""
Tests for Activity API methods.

flickr.activity.userComments and flickr.activity.userPhotos.
Uses example responses from the api-docs/ directory, converted from XML.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call
from flickr_api.objects import Activity, Photo, Photoset

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestActivityMethods(FlickrApiTestCase):
    """Tests for Activity.userPhotos and Activity.userComments"""

    @patch.object(method_call.requests, "post")
    def test_user_photos(self, mock_post):
        """Test Activity.userPhotos parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.activity.userPhotos")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        activities = Activity.userPhotos()

        # Verify the result is a list with 2 items
        self.assertEqual(len(activities), 2)

        # First activity: photoset with id="395"
        activity1 = activities[0]
        self.assertIsInstance(activity1, Activity)
        self.assertIsInstance(activity1.item, Photoset)
        self.assertEqual(activity1.item.id, "395")
        self.assertEqual(activity1.item.title, "A set of photos")
        self.assertEqual(activity1.item.owner, "12037949754@N01")

        # First activity has 1 event (comment)
        self.assertEqual(len(activity1.events), 1)
        event1 = activity1.events[0]
        self.assertIsInstance(event1, Photoset.Comment)
        self.assertEqual(event1.text, "yay")
        self.assertEqual(event1.user.id, "12037949754@N01")
        self.assertEqual(event1.user.username, "Bees")
        self.assertEqual(event1.dateadded, "1144086424")

        # Second activity: photo with id="10289"
        activity2 = activities[1]
        self.assertIsInstance(activity2, Activity)
        self.assertIsInstance(activity2.item, Photo)
        self.assertEqual(activity2.item.id, "10289")
        self.assertEqual(activity2.item.title, "A photo")
        self.assertEqual(activity2.item.owner, "12037949754@N01")

        # Second activity has 2 events (comment and note)
        self.assertEqual(len(activity2.events), 2)

        # First event is a comment
        event2_1 = activity2.events[0]
        self.assertIsInstance(event2_1, Photo.Comment)
        self.assertEqual(event2_1.text, "test")
        self.assertEqual(event2_1.user.id, "12037949754@N01")
        self.assertEqual(event2_1.user.username, "Bees")
        self.assertEqual(event2_1.dateadded, "1133806604")

        # Second event is a note
        event2_2 = activity2.events[1]
        self.assertIsInstance(event2_2, Photo.Note)
        self.assertEqual(event2_2.text, "nice")
        self.assertEqual(event2_2.user.id, "12037949754@N01")
        self.assertEqual(event2_2.user.username, "Bees")
        self.assertEqual(event2_2.dateadded, "1118785229")

    @patch.object(method_call.requests, "post")
    def test_user_comments(self, mock_post):
        """Test Activity.userComments parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.activity.userComments")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        activities = Activity.userComments()

        # Verify the result is a list with 2 items
        self.assertEqual(len(activities), 2)

        # First activity: photoset with id="395"
        activity1 = activities[0]
        self.assertIsInstance(activity1, Activity)
        self.assertIsInstance(activity1.item, Photoset)
        self.assertEqual(activity1.item.id, "395")
        self.assertEqual(activity1.item.title, "A set of photos")

        # First activity has 1 event (comment)
        self.assertEqual(len(activity1.events), 1)
        event1 = activity1.events[0]
        self.assertIsInstance(event1, Photoset.Comment)
        self.assertEqual(event1.text, "yay")

        # Second activity: photo with id="10289"
        activity2 = activities[1]
        self.assertIsInstance(activity2, Activity)
        self.assertIsInstance(activity2.item, Photo)
        self.assertEqual(activity2.item.id, "10289")
        self.assertEqual(activity2.item.title, "A photo")

        # Second activity has 2 events (comment and note)
        self.assertEqual(len(activity2.events), 2)
        self.assertIsInstance(activity2.events[0], Photo.Comment)
        self.assertIsInstance(activity2.events[1], Photo.Note)


if __name__ == "__main__":
    unittest.main()
