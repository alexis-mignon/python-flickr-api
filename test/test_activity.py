"""
Tests for Activity API methods.

flickr.activity.userComments and flickr.activity.userPhotos.
Uses example responses from the api-docs/ directory, converted from XML.
"""
import json
import os
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler
from flickr_api.objects import Activity, Photo, Photoset

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
            # Flickr API returns arrays for repeated elements,
            # single object otherwise
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


class TestActivityMethods(unittest.TestCase):
    """Tests for Activity.userPhotos and Activity.userComments"""

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
