"""
Tests for Stats API methods.

Batch 21:
flickr.stats.getCSVFiles, flickr.stats.getCollectionDomains,
flickr.stats.getCollectionReferrers, flickr.stats.getCollectionStats,
flickr.stats.getPhotoDomains, flickr.stats.getPhotoReferrers,
flickr.stats.getPhotosetDomains, flickr.stats.getPhotosetReferrers

Uses example responses from the api-docs/ directory.
"""
import json
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler

from requests import Response

from test_utils import xml_to_flickr_json, load_api_doc


class TestStatsMethods(unittest.TestCase):
    """Tests for Stats API methods"""

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
    def test_stats_get_csv_files(self, mock_post):
        """Test stats.getCSVFiles (flickr.stats.getCSVFiles)"""
        api_doc = load_api_doc("flickr.stats.getCSVFiles")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.stats.getCSVFiles()

        # Verify the result is a list of CSV file dicts
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

        # First CSV - daily
        csv1 = result[0]
        self.assertIn("href", csv1)
        self.assertIn("type", csv1)
        self.assertIn("date", csv1)
        self.assertEqual(csv1["type"], "daily")
        self.assertEqual(csv1["date"], "2010-04-01")
        self.assertIn("72157623902771865", csv1["href"])

        # Second CSV - monthly
        csv2 = result[1]
        self.assertEqual(csv2["type"], "monthly")
        self.assertEqual(csv2["date"], "2010-04-01")

        # Third CSV - daily
        csv3 = result[2]
        self.assertEqual(csv3["type"], "daily")
        self.assertEqual(csv3["date"], "2010-03-01")

    @patch.object(method_call.requests, "post")
    def test_stats_get_collection_domains(self, mock_post):
        """Test stats.getCollectionDomains (flickr.stats.getCollectionDomains)"""
        api_doc = load_api_doc("flickr.stats.getCollectionDomains")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.stats.getCollectionDomains(date="2010-01-01")

        # Verify it's a FlickrList with Domain objects
        self.assertIsInstance(result, f.FlickrList)
        self.assertEqual(len(result), 3)

        # First domain - yahoo
        d1 = result[0]
        self.assertIsInstance(d1, f.stats.Domain)
        self.assertEqual(d1.name, "images.search.yahoo.com")
        self.assertEqual(d1.views, "127")

        # Second domain - flickr
        d2 = result[1]
        self.assertEqual(d2.name, "flickr.com")
        self.assertEqual(d2.views, "122")

        # Third domain - google
        d3 = result[2]
        self.assertEqual(d3.name, "images.google.com")
        self.assertEqual(d3.views, "70")

        # Verify pagination info
        self.assertEqual(result.info.page, 1)
        self.assertEqual(result.info.perpage, 25)
        self.assertEqual(result.info.pages, 1)
        self.assertEqual(result.info.total, 3)

    @patch.object(method_call.requests, "post")
    def test_stats_get_collection_referrers(self, mock_post):
        """Test stats.getCollectionReferrers
        (flickr.stats.getCollectionReferrers)"""
        api_doc = load_api_doc("flickr.stats.getCollectionReferrers")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.stats.getCollectionReferrers(
            date="2010-01-01",
            domain="flickr.com"
        )

        # Verify it's a FlickrList with Referrer objects
        self.assertIsInstance(result, f.FlickrList)
        self.assertEqual(len(result), 3)

        # First referrer - flickr.com homepage
        r1 = result[0]
        self.assertIsInstance(r1, f.stats.Referrer)
        self.assertEqual(r1.url, "http://flickr.com/")
        self.assertEqual(r1.views, 11)

        # Second referrer - photos/friends
        r2 = result[1]
        self.assertEqual(r2.url, "http://flickr.com/photos/friends/")
        self.assertEqual(r2.views, 8)

        # Third referrer - search with searchterm
        r3 = result[2]
        self.assertEqual(r3.url, "http://flickr.com/search/?q=stats+api")
        self.assertEqual(r3.views, 2)
        self.assertEqual(r3.searchterm, "stats api")

        # Verify pagination info
        self.assertEqual(result.info.page, 1)
        self.assertEqual(result.info.perpage, 25)
        self.assertEqual(result.info.pages, 1)
        self.assertEqual(result.info.total, 3)
        self.assertEqual(result.info.name, "flickr.com")

    @patch.object(method_call.requests, "post")
    def test_collection_get_stats(self, mock_post):
        """Test Collection.getStats (flickr.stats.getCollectionStats)"""
        api_doc = load_api_doc("flickr.stats.getCollectionStats")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # Create a collection and get stats
        collection = f.Collection(id="12345678-12345678901234567")
        result = collection.getStats(date="2010-01-01")

        # Verify the result is an integer (view count)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 24)

    @patch.object(method_call.requests, "post")
    def test_stats_get_photo_domains(self, mock_post):
        """Test stats.getPhotoDomains (flickr.stats.getPhotoDomains)"""
        api_doc = load_api_doc("flickr.stats.getPhotoDomains")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.stats.getPhotoDomains(date="2010-01-01")

        # Verify it's a FlickrList with Domain objects
        self.assertIsInstance(result, f.FlickrList)
        self.assertEqual(len(result), 3)

        # First domain - yahoo
        d1 = result[0]
        self.assertIsInstance(d1, f.stats.Domain)
        self.assertEqual(d1.name, "images.search.yahoo.com")
        self.assertEqual(d1.views, "127")

        # Second domain - flickr
        d2 = result[1]
        self.assertEqual(d2.name, "flickr.com")
        self.assertEqual(d2.views, "122")

        # Third domain - google
        d3 = result[2]
        self.assertEqual(d3.name, "images.google.com")
        self.assertEqual(d3.views, "70")

        # Verify pagination info
        self.assertEqual(result.info.page, 1)
        self.assertEqual(result.info.perpage, 25)
        self.assertEqual(result.info.pages, 1)
        self.assertEqual(result.info.total, 3)

    @patch.object(method_call.requests, "post")
    def test_stats_get_photo_referrers(self, mock_post):
        """Test stats.getPhotoReferrers (flickr.stats.getPhotoReferrers)"""
        api_doc = load_api_doc("flickr.stats.getPhotoReferrers")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.stats.getPhotoReferrers(
            date="2010-01-01",
            domain="flickr.com"
        )

        # Verify it's a FlickrList with Referrer objects
        self.assertIsInstance(result, f.FlickrList)
        self.assertEqual(len(result), 3)

        # First referrer - flickr.com homepage
        r1 = result[0]
        self.assertIsInstance(r1, f.stats.Referrer)
        self.assertEqual(r1.url, "http://flickr.com/")
        self.assertEqual(r1.views, 11)

        # Second referrer - photos/friends
        r2 = result[1]
        self.assertEqual(r2.url, "http://flickr.com/photos/friends/")
        self.assertEqual(r2.views, 8)

        # Third referrer - search with searchterm
        r3 = result[2]
        self.assertEqual(r3.url, "http://flickr.com/search/?q=stats+api")
        self.assertEqual(r3.views, 2)
        self.assertEqual(r3.searchterm, "stats api")

        # Verify pagination info
        self.assertEqual(result.info.page, 1)
        self.assertEqual(result.info.perpage, 25)
        self.assertEqual(result.info.pages, 1)
        self.assertEqual(result.info.total, 3)
        self.assertEqual(result.info.name, "flickr.com")

    @patch.object(method_call.requests, "post")
    def test_stats_get_photoset_domains(self, mock_post):
        """Test stats.getPhotosetDomains (flickr.stats.getPhotosetDomains)"""
        api_doc = load_api_doc("flickr.stats.getPhotosetDomains")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.stats.getPhotosetDomains(date="2010-01-01")

        # Verify it's a FlickrList with Domain objects
        self.assertIsInstance(result, f.FlickrList)
        self.assertEqual(len(result), 3)

        # First domain - yahoo
        d1 = result[0]
        self.assertIsInstance(d1, f.stats.Domain)
        self.assertEqual(d1.name, "images.search.yahoo.com")
        self.assertEqual(d1.views, "127")

        # Second domain - flickr
        d2 = result[1]
        self.assertEqual(d2.name, "flickr.com")
        self.assertEqual(d2.views, "122")

        # Third domain - google
        d3 = result[2]
        self.assertEqual(d3.name, "images.google.com")
        self.assertEqual(d3.views, "70")

        # Verify pagination info
        self.assertEqual(result.info.page, 1)
        self.assertEqual(result.info.perpage, 25)
        self.assertEqual(result.info.pages, 1)
        self.assertEqual(result.info.total, 3)

    @patch.object(method_call.requests, "post")
    def test_stats_get_photoset_referrers(self, mock_post):
        """Test stats.getPhotosetReferrers (flickr.stats.getPhotosetReferrers)"""
        api_doc = load_api_doc("flickr.stats.getPhotosetReferrers")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        result = f.stats.getPhotosetReferrers(
            date="2010-01-01",
            domain="flickr.com"
        )

        # Verify it's a FlickrList with Referrer objects
        self.assertIsInstance(result, f.FlickrList)
        self.assertEqual(len(result), 3)

        # First referrer - flickr.com homepage
        r1 = result[0]
        self.assertIsInstance(r1, f.stats.Referrer)
        self.assertEqual(r1.url, "http://flickr.com/")
        self.assertEqual(r1.views, 11)

        # Second referrer - photos/friends
        r2 = result[1]
        self.assertEqual(r2.url, "http://flickr.com/photos/friends/")
        self.assertEqual(r2.views, 8)

        # Third referrer - search with searchterm
        r3 = result[2]
        self.assertEqual(r3.url, "http://flickr.com/search/?q=stats+api")
        self.assertEqual(r3.views, 2)
        self.assertEqual(r3.searchterm, "stats api")

        # Verify pagination info
        self.assertEqual(result.info.page, 1)
        self.assertEqual(result.info.perpage, 25)
        self.assertEqual(result.info.pages, 1)
        self.assertEqual(result.info.total, 3)
        self.assertEqual(result.info.name, "flickr.com")


if __name__ == "__main__":
    unittest.main()
