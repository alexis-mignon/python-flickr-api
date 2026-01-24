"""
Tests for Contact API methods.

flickr.contacts.getList, flickr.contacts.getListRecentlyUploaded,
flickr.contacts.getTaggingSuggestions, and flickr.contacts.getPublicList.
Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestContactMethods(FlickrApiTestCase):
    """Tests for Contact.getList, Contact.getListRecentlyUploaded, and
    Contact.getTaggingSuggestions"""

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

        # First contact: Eric (0/1 values are converted to int)
        self.assertEqual(contacts[0].id, "12037949629@N01")
        self.assertEqual(contacts[0].username, "Eric")
        self.assertEqual(contacts[0].realname, "Eric Costello")
        self.assertEqual(contacts[0].friend, 1)
        self.assertEqual(contacts[0].family, 0)
        self.assertEqual(contacts[0].ignored, 1)

        # Second contact: neb
        self.assertEqual(contacts[1].id, "12037949631@N01")
        self.assertEqual(contacts[1].username, "neb")
        self.assertEqual(contacts[1].realname, "Ben Cerveny")
        self.assertEqual(contacts[1].friend, 0)
        self.assertEqual(contacts[1].family, 0)

        # Third contact: cal_abc
        self.assertEqual(contacts[2].id, "41578656547@N01")
        self.assertEqual(contacts[2].username, "cal_abc")
        self.assertEqual(contacts[2].realname, "Cal Henderson")
        self.assertEqual(contacts[2].friend, 1)
        self.assertEqual(contacts[2].family, 1)

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

        # The contact: Hugo Haas (0/1 values are converted to int)
        self.assertEqual(contacts[0].id, "30135021@N05")
        self.assertEqual(contacts[0].username, "Hugo Haas")
        self.assertEqual(contacts[0].iconserver, 1)
        self.assertEqual(contacts[0].iconfarm, 1)
        self.assertEqual(contacts[0].friend, 0)
        self.assertEqual(contacts[0].family, 0)

        # Verify pagination info (Info class converts these to int)
        self.assertEqual(contacts.info.page, 1)
        self.assertEqual(contacts.info.pages, 1)
        self.assertEqual(contacts.info.total, 1)

    @patch.object(method_call.requests, "post")
    def test_get_public_contacts(self, mock_post):
        """Test Person.getPublicContacts (flickr.contacts.getPublicList)"""
        api_doc = load_api_doc("flickr.contacts.getPublicList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # Create a person and get their public contacts
        person = f.Person(id="12345678@N01")
        contacts = person.getPublicContacts()

        # Verify based on the example data - 3 contacts
        self.assertEqual(len(contacts), 3)
        self.assertIsInstance(contacts[0], f.Person)

        # First contact: Eric
        self.assertEqual(contacts[0].id, "12037949629@N01")
        self.assertEqual(contacts[0].username, "Eric")
        self.assertEqual(contacts[0].iconserver, 1)
        self.assertEqual(contacts[0].ignored, 1)

        # Second contact: neb
        self.assertEqual(contacts[1].id, "12037949631@N01")
        self.assertEqual(contacts[1].username, "neb")
        self.assertEqual(contacts[1].ignored, 0)

        # Third contact: cal_abc
        self.assertEqual(contacts[2].id, "41578656547@N01")
        self.assertEqual(contacts[2].username, "cal_abc")
        self.assertEqual(contacts[2].ignored, 0)

        # Verify pagination info
        self.assertEqual(contacts.info.page, 1)
        self.assertEqual(contacts.info.pages, 1)
        self.assertEqual(contacts.info.total, 3)


if __name__ == "__main__":
    unittest.main()
