"""
Tests for Tag API methods.

Uses example responses from the api-docs/ directory, converted from XML to JSON.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestTagMethods(FlickrApiTestCase):
    """Tests for Tag API methods"""

    @patch.object(method_call.requests, "post")
    def test_get_hot_list(self, mock_post):
        """Test Tag.getHotList parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.tags.getHotList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        tags = f.Tag.getHotList()

        # Verify based on the example data
        # Note: _content is converted to "text" by clean_content() in method_call.py
        self.assertEqual(len(tags), 6)
        self.assertIsInstance(tags[0], f.Tag)
        # First tag: score="20", northerncalifornia
        self.assertEqual(tags[0].score, "20")
        self.assertEqual(tags[0].text, "northerncalifornia")
        # Second tag: score="18", top20
        self.assertEqual(tags[1].score, "18")
        self.assertEqual(tags[1].text, "top20")
        # Last tag: score="4", jan06
        self.assertEqual(tags[5].score, "4")
        self.assertEqual(tags[5].text, "jan06")

    @patch.object(method_call.requests, "post")
    def test_get_list_user(self, mock_post):
        """Test Tag.getListUser parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.tags.getListUser")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        tags = f.Tag.getListUser(user_id="12037949754@N01")

        # Verify based on the example data
        # Note: Tags with only _content become strings after clean_content(),
        # so we access via .text attribute
        self.assertEqual(len(tags), 5)
        self.assertIsInstance(tags[0], f.Tag)
        # Tags from example: gull, tag1, tag2, tags, test
        self.assertEqual(tags[0].text, "gull")
        self.assertEqual(tags[1].text, "tag1")
        self.assertEqual(tags[2].text, "tag2")
        self.assertEqual(tags[3].text, "tags")
        self.assertEqual(tags[4].text, "test")

    @patch.object(method_call.requests, "post")
    def test_get_list_user_popular(self, mock_post):
        """Test Tag.getListUserPopular parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.tags.getListUserPopular")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        tags = f.Tag.getListUserPopular(user_id="12037949754@N01")

        # Verify based on the example data
        # Note: _content is converted to "text" by clean_content() in method_call.py
        self.assertEqual(len(tags), 5)
        self.assertIsInstance(tags[0], f.Tag)
        # First tag: count="10", bar
        self.assertEqual(tags[0].text, "bar")
        self.assertEqual(tags[0].count, 10)  # count is converted to int by Tag
        # Second tag: count="11", foo
        self.assertEqual(tags[1].text, "foo")
        self.assertEqual(tags[1].count, 11)
        # Third tag: count="147", gull (highest count)
        self.assertEqual(tags[2].text, "gull")
        self.assertEqual(tags[2].count, 147)

    @patch.object(method_call.requests, "post")
    def test_get_clusters(self, mock_post):
        """Test Tag.getClusters parses the API response correctly"""
        api_doc = load_api_doc("flickr.tags.getClusters")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        clusters = f.Tag.getClusters(tag="cows")

        # Verify based on the example data
        # Two clusters: farm/animals/cattle and green/landscape/countryside
        self.assertEqual(len(clusters), 2)
        self.assertIsInstance(clusters[0], f.Tag.Cluster)

        # First cluster has total="3" (string) and tags: farm, animals, cattle
        self.assertEqual(clusters[0].total, "3")
        self.assertEqual(len(clusters[0].tags), 3)
        self.assertIsInstance(clusters[0].tags[0], f.Tag)
        self.assertEqual(clusters[0].tags[0].text, "farm")
        self.assertEqual(clusters[0].tags[1].text, "animals")
        self.assertEqual(clusters[0].tags[2].text, "cattle")

        # Second cluster has total="3" (string) and tags: green, landscape, countryside
        self.assertEqual(clusters[1].total, "3")
        self.assertEqual(clusters[1].tags[0].text, "green")
        self.assertEqual(clusters[1].tags[1].text, "landscape")
        self.assertEqual(clusters[1].tags[2].text, "countryside")

    @patch.object(method_call.requests, "post")
    def test_cluster_get_photos(self, mock_post):
        """Test Tag.Cluster.getPhotos parses the API response correctly"""
        # The api-doc has empty response, so create a mock response
        json_response = {
            "photos": {
                "page": 1,
                "pages": 1,
                "perpage": 24,
                "total": 2,
                "photo": [
                    {
                        "id": "12345",
                        "owner": "12037949754@N01",
                        "secret": "abc123",
                        "server": "1234",
                        "farm": 1,
                        "title": "Cow Photo 1",
                    },
                    {
                        "id": "67890",
                        "owner": "98765432100@N01",
                        "secret": "def456",
                        "server": "5678",
                        "farm": 2,
                        "title": "Cow Photo 2",
                    },
                ],
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        cluster = f.Tag.Cluster(tag="cows", id="farm-animals-cattle")
        photos = cluster.getPhotos()

        # Verify photos are returned
        self.assertEqual(len(photos), 2)
        self.assertIsInstance(photos[0], f.Photo)
        self.assertEqual(photos[0].id, "12345")
        self.assertEqual(photos[0].title, "Cow Photo 1")
        self.assertIsInstance(photos[0].owner, f.Person)
        self.assertEqual(photos[0].owner.id, "12037949754@N01")

        self.assertEqual(photos[1].id, "67890")
        self.assertEqual(photos[1].title, "Cow Photo 2")

    @patch.object(method_call.requests, "post")
    def test_get_list_photo(self, mock_post):
        """Test Photo.getTags parses the API response correctly"""
        api_doc = load_api_doc("flickr.tags.getListPhoto")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="2619")
        tags = photo.getTags()

        # Verify based on example data
        # Two tags: tag1 (id=156) and tag2 (id=157)
        self.assertEqual(len(tags), 2)
        self.assertIsInstance(tags[0], f.Tag)

        self.assertEqual(tags[0].id, "156")
        self.assertEqual(tags[0].author, "12037949754@N01")
        self.assertEqual(tags[0].authorname, "Bees")
        self.assertEqual(tags[0].raw, "tag 1")
        self.assertEqual(tags[0].text, "tag1")

        self.assertEqual(tags[1].id, "157")
        self.assertEqual(tags[1].author, "12037949754@N01")
        self.assertEqual(tags[1].authorname, "Bees")
        self.assertEqual(tags[1].raw, "tag 2")
        self.assertEqual(tags[1].text, "tag2")

    @patch.object(method_call.requests, "post")
    def test_get_list_user_raw(self, mock_post):
        """Test Tag.getListUserRaw parses the API response correctly"""
        api_doc = load_api_doc("flickr.tags.getListUserRaw")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.Tag.getListUserRaw()

        # Verify based on example data
        # One tag with clean="foo" and raws: ["foo", "Foo", "f:oo"]
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result[0], dict)
        self.assertEqual(result[0]["clean"], "foo")
        self.assertEqual(len(result[0]["raws"]), 3)
        self.assertEqual(result[0]["raws"][0], "foo")
        self.assertEqual(result[0]["raws"][1], "Foo")
        self.assertEqual(result[0]["raws"][2], "f:oo")

    @patch.object(method_call.requests, "post")
    def test_get_related(self, mock_post):
        """Test Tag.getRelated parses the API response correctly"""
        api_doc = load_api_doc("flickr.tags.getRelated")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        related = f.Tag.getRelated(tag="london")

        # Verify based on example data
        # Related tags: england, thames, tube, bigben, uk
        self.assertEqual(len(related), 5)
        # getRelated returns raw strings (not Tag objects)
        self.assertEqual(related[0], "england")
        self.assertEqual(related[1], "thames")
        self.assertEqual(related[2], "tube")
        self.assertEqual(related[3], "bigben")
        self.assertEqual(related[4], "uk")


if __name__ == "__main__":
    unittest.main()
