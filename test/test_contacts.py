"""
Tests for Contact API methods.

flickr.contacts.getList, flickr.contacts.getListRecentlyUploaded, and
flickr.contacts.getTaggingSuggestions.
Uses example responses from the api-docs/ directory.
"""
import json
import os
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler

from requests import Response


def xml_to_flickr_json(xml_string):
    """
    Convert Flickr XML response format to the JSON format the API returns.

    Flickr's JSON format:
    - Element text content becomes "_content"
    - Attributes become properties
    - Repeated elements become arrays
    - Single elements stay as objects
    - If root is <rsp>, unwrap it to match JSON API format
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
            # Flickr returns arrays for repeated elements, single otherwise
            if len(children) == 1:
                result[tag] = children[0]
            else:
                result[tag] = children

        return result

    # Convert root element
    root_dict = element_to_dict(root)

    # If root is <rsp>, unwrap it (JSON API returns content directly)
    if root.tag == "rsp":
        return root_dict
    else:
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


class TestContactMethods(unittest.TestCase):
    """Tests for Contact.getList, Contact.getListRecentlyUploaded, and
    Contact.getTaggingSuggestions"""

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
    def test_get_list(self, mock_post):
        """Test Contact.getList parses the API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.contacts.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        contacts = f.Contact.getList()

        # Verify based on the example data - 3 contacts
        self.assertEqual(len(contacts), 3)
        self.assertIsInstance(contacts[0], f.Person)

        # First contact: Eric
        self.assertEqual(contacts[0].id, "12037949629@N01")
        self.assertEqual(contacts[0].username, "Eric")
        self.assertEqual(contacts[0].realname, "Eric Costello")
        self.assertEqual(contacts[0].friend, "1")
        self.assertEqual(contacts[0].family, "0")
        self.assertEqual(contacts[0].ignored, "1")

        # Second contact: neb
        self.assertEqual(contacts[1].id, "12037949631@N01")
        self.assertEqual(contacts[1].username, "neb")
        self.assertEqual(contacts[1].realname, "Ben Cerveny")
        self.assertEqual(contacts[1].friend, "0")
        self.assertEqual(contacts[1].family, "0")

        # Third contact: cal_abc
        self.assertEqual(contacts[2].id, "41578656547@N01")
        self.assertEqual(contacts[2].username, "cal_abc")
        self.assertEqual(contacts[2].realname, "Cal Henderson")
        self.assertEqual(contacts[2].friend, "1")
        self.assertEqual(contacts[2].family, "1")

        # Verify pagination info (Info class converts these to int)
        self.assertEqual(contacts.info.page, 1)
        self.assertEqual(contacts.info.pages, 1)
        self.assertEqual(contacts.info.total, 3)

    @patch.object(method_call.requests, "post")
    def test_get_list_recently_uploaded(self, mock_post):
        """Test Contact.getListRecentlyUploaded parses API response"""
        # The api-docs file has an empty response, so we create a sample
        # based on the similar getList response format
        json_response = {
            "contacts": {
                "page": "1",
                "pages": "1",
                "perpage": "1000",
                "total": "2",
                "contact": [
                    {
                        "nsid": "12345678@N01",
                        "username": "recentuser1",
                        "iconserver": "1",
                        "realname": "Recent User One",
                        "friend": "1",
                        "family": "0",
                        "photos_uploaded": "5",
                    },
                    {
                        "nsid": "87654321@N01",
                        "username": "recentuser2",
                        "iconserver": "2",
                        "realname": "Recent User Two",
                        "friend": "0",
                        "family": "1",
                        "photos_uploaded": "12",
                    },
                ]
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        contacts = f.Contact.getListRecentlyUploaded()

        # Verify results
        self.assertEqual(len(contacts), 2)
        self.assertIsInstance(contacts[0], f.Person)

        # First contact
        self.assertEqual(contacts[0].id, "12345678@N01")
        self.assertEqual(contacts[0].username, "recentuser1")
        self.assertEqual(contacts[0].photos_uploaded, "5")

        # Second contact
        self.assertEqual(contacts[1].id, "87654321@N01")
        self.assertEqual(contacts[1].username, "recentuser2")
        self.assertEqual(contacts[1].photos_uploaded, "12")

    @patch.object(method_call.requests, "post")
    def test_get_tagging_suggestions(self, mock_post):
        """Test Contact.getTaggingSuggestions parses API response correctly"""
        # Load example response from api-docs
        api_doc = load_api_doc("flickr.contacts.getTaggingSuggestions")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        contacts = f.Contact.getTaggingSuggestions()

        # Verify based on the example data - 1 contact
        self.assertEqual(len(contacts), 1)
        self.assertIsInstance(contacts[0], f.Person)

        # The contact: Hugo Haas
        self.assertEqual(contacts[0].id, "30135021@N05")
        self.assertEqual(contacts[0].username, "Hugo Haas")
        self.assertEqual(contacts[0].iconserver, "1")
        self.assertEqual(contacts[0].iconfarm, "1")
        self.assertEqual(contacts[0].friend, "0")
        self.assertEqual(contacts[0].family, "0")

        # Verify pagination info (Info class converts these to int)
        self.assertEqual(contacts.info.page, 1)
        self.assertEqual(contacts.info.pages, 1)
        self.assertEqual(contacts.info.total, 1)


if __name__ == "__main__":
    unittest.main()
