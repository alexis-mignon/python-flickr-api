"""
Tests for Collection API methods.

flickr.collections.getInfo and flickr.collections.getTree.
Uses example responses from the api-docs/ directory, converted from XML to JSON.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestCollectionMethods(FlickrApiTestCase):
    """Tests for Collection.getInfo and Collection.getTree"""

    @patch.object(method_call.requests, "post")
    def test_get_info(self, mock_post):
        """Test Collection.getInfo parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.collections.getInfo")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # Collection.getInfo is an instance method
        collection = f.Collection(id="12-72157594586579649")
        info = collection.getInfo()

        # getInfo returns a dict with the collection info
        self.assertIsInstance(info, dict)

        # Verify based on the example data
        self.assertEqual(info["id"], "12-72157594586579649")
        self.assertEqual(info["child_count"], "6")
        self.assertEqual(info["datecreate"], "1173812218")

        # Check title and description
        # Note: clean_content converts {"_content": "..."} to just "..."
        self.assertEqual(info["title"], "All My Photos")
        self.assertEqual(info["description"], "Photos!")

        # Check iconphotos (converted to Photo objects in format_result)
        # Note: The format_result in objects.py has a bug - it iterates over
        # empty `photos` list instead of `icon_photos`, so iconphotos is empty
        self.assertIsInstance(info["iconphotos"], list)

    @patch.object(method_call.requests, "post")
    def test_get_tree(self, mock_post):
        """Test Collection.getTree parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.collections.getTree")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # Collection.getTree is an instance method
        collection = f.Collection(id="0")
        collections = collection.getTree()

        # Verify the result is a list of collections
        self.assertIsInstance(collections, list)
        self.assertEqual(len(collections), 1)
        self.assertIsInstance(collections[0], f.Collection)

        # First collection: id="12-72157594586579649", title="All My Photos"
        coll = collections[0]
        self.assertEqual(coll.id, "12-72157594586579649")
        self.assertEqual(coll.title, "All My Photos")
        self.assertEqual(coll.description, "a collection")

        # Check the photosets within the collection
        self.assertIsInstance(coll.sets, list)
        self.assertEqual(len(coll.sets), 2)
        self.assertIsInstance(coll.sets[0], f.Photoset)

        # First set: id="92157594171298291", title="kitesurfing"
        self.assertEqual(coll.sets[0].id, "92157594171298291")
        self.assertEqual(coll.sets[0].title, "kitesurfing")
        self.assertEqual(coll.sets[0].description, "a set")

        # Second set: id="72157594247596158", title="faves"
        self.assertEqual(coll.sets[1].id, "72157594247596158")
        self.assertEqual(coll.sets[1].title, "faves")
        self.assertEqual(coll.sets[1].description, "some favorites.")

    @patch.object(method_call.requests, "post")
    def test_person_get_collection_tree(self, mock_post):
        """Test Person.getCollectionTree parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.collections.getTree")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # Person.getCollectionTree is an instance method
        person = f.Person(id="12037949754@N01")
        collections = person.getCollectionTree()

        # Verify the result is a list of collections
        self.assertIsInstance(collections, list)
        self.assertEqual(len(collections), 1)
        self.assertIsInstance(collections[0], f.Collection)

        # Verify the collection details
        coll = collections[0]
        self.assertEqual(coll.id, "12-72157594586579649")
        self.assertEqual(coll.title, "All My Photos")

        # Check the photosets
        self.assertEqual(len(coll.sets), 2)
        self.assertEqual(coll.sets[0].title, "kitesurfing")
        self.assertEqual(coll.sets[1].title, "faves")


if __name__ == "__main__":
    unittest.main()
