"""
Tests for MachineTag API methods.

flickr.machinetags.getNamespaces, flickr.machinetags.getPairs,
flickr.machinetags.getPredicates, flickr.machinetags.getRecentValues,
flickr.machinetags.getValues
Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestMachineTagMethods(FlickrApiTestCase):
    """Tests for MachineTag-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_machinetag_get_namespaces(self, mock_post):
        """Test MachineTag.getNamespaces (flickr.machinetags.getNamespaces)"""
        api_doc = load_api_doc("flickr.machinetags.getNamespaces")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        namespaces = f.MachineTag.getNamespaces()

        # Verify we got 5 namespaces
        self.assertEqual(len(namespaces), 5)

        # First namespace - aero
        ns1 = namespaces[0]
        self.assertIsInstance(ns1, f.MachineTag.Namespace)
        self.assertEqual(ns1.usage, "6538")
        self.assertEqual(ns1.predicates, "13")
        self.assertEqual(ns1.text, "aero")

        # Second namespace - flickr
        ns2 = namespaces[1]
        self.assertEqual(ns2.usage, "9072")
        self.assertEqual(ns2.predicates, "24")
        self.assertEqual(ns2.text, "flickr")

        # Third namespace - geo
        ns3 = namespaces[2]
        self.assertEqual(ns3.usage, "670270")
        self.assertEqual(ns3.predicates, "35")
        self.assertEqual(ns3.text, "geo")

        # Fifth namespace - upcoming
        ns5 = namespaces[4]
        self.assertEqual(ns5.usage, "50449")
        self.assertEqual(ns5.predicates, "4")
        self.assertEqual(ns5.text, "upcoming")

        # Verify pagination info
        self.assertEqual(namespaces.info.page, 1)
        self.assertEqual(namespaces.info.pages, 1)
        self.assertEqual(namespaces.info.total, 5)
        self.assertEqual(namespaces.info.perpage, 500)

    @patch.object(method_call.requests, "post")
    def test_machinetag_get_pairs(self, mock_post):
        """Test MachineTag.getPairs (flickr.machinetags.getPairs)"""
        api_doc = load_api_doc("flickr.machinetags.getPairs")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        pairs = f.MachineTag.getPairs()

        # Verify we got 4 pairs
        self.assertEqual(len(pairs), 4)

        # First pair - aero:airline
        p1 = pairs[0]
        self.assertIsInstance(p1, f.MachineTag.Pair)
        self.assertEqual(p1.namespace, "aero")
        self.assertEqual(p1.predicate, "airline")
        self.assertEqual(p1.usage, "1093")
        self.assertEqual(p1.text, "aero:airline")

        # Second pair - aero:icao
        p2 = pairs[1]
        self.assertEqual(p2.namespace, "aero")
        self.assertEqual(p2.predicate, "icao")
        self.assertEqual(p2.usage, "4")
        self.assertEqual(p2.text, "aero:icao")

        # Third pair - aero:model
        p3 = pairs[2]
        self.assertEqual(p3.namespace, "aero")
        self.assertEqual(p3.predicate, "model")
        self.assertEqual(p3.usage, "1026")

        # Fourth pair - aero:tail
        p4 = pairs[3]
        self.assertEqual(p4.predicate, "tail")
        self.assertEqual(p4.usage, "1048")

        # Verify pagination info
        self.assertEqual(pairs.info.page, 1)
        self.assertEqual(pairs.info.pages, 3)
        self.assertEqual(pairs.info.total, 1228)
        self.assertEqual(pairs.info.perpage, 500)

    @patch.object(method_call.requests, "post")
    def test_machinetag_get_predicates(self, mock_post):
        """Test MachineTag.getPredicates (flickr.machinetags.getPredicates)"""
        api_doc = load_api_doc("flickr.machinetags.getPredicates")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        predicates = f.MachineTag.getPredicates()

        # Verify we got 3 predicates
        self.assertEqual(len(predicates), 3)

        # First predicate - elbow
        pred1 = predicates[0]
        self.assertIsInstance(pred1, f.MachineTag.Predicate)
        self.assertEqual(pred1.usage, "20")
        self.assertEqual(pred1.namespaces, 1)
        self.assertEqual(pred1.text, "elbow")

        # Second predicate - face
        pred2 = predicates[1]
        self.assertEqual(pred2.usage, "52")
        self.assertEqual(pred2.namespaces, "2")
        self.assertEqual(pred2.text, "face")

        # Third predicate - hand
        pred3 = predicates[2]
        self.assertEqual(pred3.usage, "10")
        self.assertEqual(pred3.namespaces, 1)
        self.assertEqual(pred3.text, "hand")

        # Verify pagination info
        self.assertEqual(predicates.info.page, 1)
        self.assertEqual(predicates.info.pages, 1)
        self.assertEqual(predicates.info.total, 3)
        self.assertEqual(predicates.info.perpage, 500)

    @patch.object(method_call.requests, "post")
    def test_machinetag_get_recent_values(self, mock_post):
        """Test MachineTag.getRecentValues (flickr.machinetags.getRecentValues)"""
        api_doc = load_api_doc("flickr.machinetags.getRecentValues")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        values = f.MachineTag.getRecentValues()

        # Verify we got 1 value
        self.assertEqual(len(values), 1)

        # First value
        v1 = values[0]
        self.assertIsInstance(v1, f.MachineTag.Value)
        self.assertEqual(v1.usage, "4")
        self.assertEqual(v1.namespace, "taxonomy")
        self.assertEqual(v1.predicate, "common")
        self.assertEqual(v1.first_added, "1244232796")
        self.assertEqual(v1.last_added, "1244232796")
        self.assertEqual(v1.text, "maui chaff flower")

        # Verify pagination info
        self.assertEqual(values.info.page, 1)
        self.assertEqual(values.info.pages, 1)
        self.assertEqual(values.info.total, 500)
        self.assertEqual(values.info.perpage, 500)
        # Response also includes namespace and predicate filters
        self.assertEqual(values.info.namespace, "taxonomy")
        self.assertEqual(values.info.predicate, "common")

    @patch.object(method_call.requests, "post")
    def test_machinetag_get_values(self, mock_post):
        """Test MachineTag.getValues (flickr.machinetags.getValues)"""
        api_doc = load_api_doc("flickr.machinetags.getValues")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        values = f.MachineTag.getValues(namespace="upcoming", predicate="event")

        # Verify we got 3 values
        self.assertEqual(len(values), 3)

        # First value
        v1 = values[0]
        self.assertIsInstance(v1, f.MachineTag.Value)
        self.assertEqual(v1.usage, "3")
        self.assertEqual(v1.text, "123")

        # Second value
        v2 = values[1]
        self.assertEqual(v2.usage, 1)
        self.assertEqual(v2.text, "456")

        # Third value
        v3 = values[2]
        self.assertEqual(v3.usage, "147")
        self.assertEqual(v3.text, "789")

        # Verify pagination info
        self.assertEqual(values.info.page, 1)
        self.assertEqual(values.info.pages, 1)
        self.assertEqual(values.info.total, 3)
        self.assertEqual(values.info.perpage, 500)
        # Response also includes namespace and predicate filters
        self.assertEqual(values.info.namespace, "upcoming")
        self.assertEqual(values.info.predicate, "event")


if __name__ == "__main__":
    unittest.main()
