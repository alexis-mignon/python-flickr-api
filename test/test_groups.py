"""
Tests for Group API methods.

flickr.groups.getInfo, flickr.groups.search, flickr.groups.join,
flickr.groups.joinRequest, flickr.groups.leave, flickr.groups.members.getList,
flickr.groups.pools.add, flickr.groups.pools.getContext, flickr.groups.pools.getGroups,
flickr.groups.pools.getPhotos, flickr.groups.pools.remove
Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestGroupMethods(FlickrApiTestCase):
    """Tests for Group-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_group_get_info(self, mock_post):
        """Test Group.getInfo (flickr.groups.getInfo)"""
        api_doc = load_api_doc("flickr.groups.getInfo")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        group = f.Group(id="34427465497@N01")
        info = group.getInfo()

        # getInfo returns a dict of group attributes
        # Note: members/privacy are strings since getInfo returns raw dict,
        # not a Group object with converters applied
        self.assertEqual(info["id"], "34427465497@N01")
        self.assertEqual(info["name"], "GNEverybody")
        self.assertEqual(info["description"], "The group for GNE players")
        self.assertEqual(info["members"], "69")
        self.assertEqual(info["privacy"], "3")
        self.assertEqual(info["ispoolmoderated"], 0)

        # Verify throttle info
        self.assertIn("throttle", info)
        self.assertEqual(info["throttle"]["count"], "10")
        self.assertEqual(info["throttle"]["mode"], "month")

        # Verify restrictions info
        self.assertIn("restrictions", info)
        self.assertEqual(info["restrictions"]["photos_ok"], 1)
        self.assertEqual(info["restrictions"]["videos_ok"], 1)

    @patch.object(method_call.requests, "post")
    def test_group_search(self, mock_post):
        """Test Group.search (flickr.groups.search)"""
        api_doc = load_api_doc("flickr.groups.search")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        groups = f.Group.search(text="test")

        # Verify we got 5 groups
        self.assertEqual(len(groups), 5)

        # First group
        g1 = groups[0]
        self.assertIsInstance(g1, f.Group)
        self.assertEqual(g1.id, "3000@N02")
        self.assertEqual(g1.name, "Frito's Test Group")
        self.assertFalse(g1.eighteenplus)

        # Second group
        g2 = groups[1]
        self.assertEqual(g2.id, "32825757@N00")
        self.assertEqual(g2.name, "Free for All")

        # Verify pagination info
        self.assertEqual(groups.info.page, 1)
        self.assertEqual(groups.info.pages, 14)
        self.assertEqual(groups.info.total, 67)

    @patch.object(method_call.requests, "post")
    def test_group_join(self, mock_post):
        """Test Group.join (flickr.groups.join)"""
        # Empty response - method returns None
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="34427465497@N01")
        result = group.join()

        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_group_join_request(self, mock_post):
        """Test Group.joinRequest (flickr.groups.joinRequest)"""
        # Empty response - method returns None
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="34427465497@N01")
        result = group.joinRequest(message="Please let me join!")

        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_group_leave(self, mock_post):
        """Test Group.leave (flickr.groups.leave)"""
        # Empty response - method returns None
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="34427465497@N01")
        result = group.leave()

        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_group_get_members(self, mock_post):
        """Test Group.getMembers (flickr.groups.members.getList)"""
        api_doc = load_api_doc("flickr.groups.members.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        group = f.Group(id="34427465497@N01")
        members = group.getMembers()

        # Verify we got 4 members
        self.assertEqual(len(members), 4)

        # First member
        m1 = members[0]
        self.assertIsInstance(m1, f.Person)
        self.assertEqual(m1.id, "123456@N01")
        self.assertEqual(m1.username, "foo")
        # iconserver "1" is converted to int by xml_to_flickr_json
        self.assertEqual(m1.iconserver, 1)
        self.assertEqual(m1.iconfarm, 1)
        self.assertEqual(m1.membertype, "2")

        # Second member (admin) - iconserver "0" is converted to int
        m2 = members[1]
        self.assertEqual(m2.id, "118210@N07")
        self.assertEqual(m2.username, "kewlchops666")
        self.assertEqual(m2.iconserver, 0)
        self.assertEqual(m2.membertype, "4")

        # Fourth member (moderator)
        m4 = members[3]
        self.assertEqual(m4.id, "67783977@N00")
        self.assertEqual(m4.username, "fakedunstanp1")
        self.assertEqual(m4.membertype, "3")

        # Verify pagination info
        self.assertEqual(members.info.page, 1)
        self.assertEqual(members.info.pages, 1)
        self.assertEqual(members.info.perpage, 100)
        self.assertEqual(members.info.total, 33)

    @patch.object(method_call.requests, "post")
    def test_group_add_photo(self, mock_post):
        """Test Group.addPhoto (flickr.groups.pools.add)"""
        # Empty response - method returns None
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="34427465497@N01")
        result = group.addPhoto(photo_id="12345678")

        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_group_get_pool_context(self, mock_post):
        """Test Group.getPoolContext (flickr.groups.pools.getContext)"""
        # XML has two root elements, so wrap in a root to parse, then use JSON
        # Response: prevphoto and nextphoto elements
        json_response = {
            "prevphoto": {
                "id": "2980",
                "secret": "973da1e709",
                "title": "boo!",
                "url": "/photos/bees/2980/"
            },
            "nextphoto": {
                "id": "2985",
                "secret": "059b664012",
                "title": "Amsterdam Amstel",
                "url": "/photos/bees/2985/"
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        group = f.Group(id="34427465497@N01")
        prev_photo, next_photo = group.getPoolContext(photo_id="2983")

        # Verify previous photo
        self.assertIsInstance(prev_photo, f.Photo)
        self.assertEqual(prev_photo.id, "2980")
        self.assertEqual(prev_photo.secret, "973da1e709")
        self.assertEqual(prev_photo.title, "boo!")

        # Verify next photo
        self.assertIsInstance(next_photo, f.Photo)
        self.assertEqual(next_photo.id, "2985")
        self.assertEqual(next_photo.secret, "059b664012")
        self.assertEqual(next_photo.title, "Amsterdam Amstel")

    @patch.object(method_call.requests, "post")
    def test_group_get_groups(self, mock_post):
        """Test Group.getGroups (flickr.groups.pools.getGroups)"""
        api_doc = load_api_doc("flickr.groups.pools.getGroups")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        groups = f.Group.getGroups()

        # Verify we got 3 groups
        self.assertEqual(len(groups), 3)

        # First group - note: API uses 'nsid' for group id
        g1 = groups[0]
        self.assertIsInstance(g1, f.Group)
        self.assertEqual(g1.nsid, "33853651696@N01")
        self.assertEqual(g1.name, "Art and Literature Hoedown")
        self.assertEqual(g1.admin, 0)
        # privacy is converted to int by Group converters
        self.assertEqual(g1.privacy, 3)
        self.assertEqual(g1.photos, "2")
        # iconserver "1" is converted to int by xml_to_flickr_json
        self.assertEqual(g1.iconserver, 1)

        # Second group (admin)
        g2 = groups[1]
        self.assertEqual(g2.nsid, "34427465446@N01")
        self.assertEqual(g2.name, "FlickrIdeas")
        self.assertEqual(g2.admin, 1)

        # Verify pagination info
        self.assertEqual(groups.info.page, 1)
        self.assertEqual(groups.info.pages, 1)
        # Note: API uses per_page (not perpage), so it stays as string
        self.assertEqual(groups.info.per_page, "400")
        self.assertEqual(groups.info.total, 3)

    @patch.object(method_call.requests, "post")
    def test_group_get_photos(self, mock_post):
        """Test Group.getPhotos (flickr.groups.pools.getPhotos)"""
        api_doc = load_api_doc("flickr.groups.pools.getPhotos")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        group = f.Group(id="34427465497@N01")
        photos = group.getPhotos()

        # Verify we got 1 photo
        self.assertEqual(len(photos), 1)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2645")
        self.assertEqual(p1.owner.id, "12037949754@N01")
        self.assertEqual(p1.title, "36679_o")
        self.assertEqual(p1.secret, "a9f4a06091")
        self.assertEqual(p1.server, "2")
        self.assertTrue(p1.ispublic)
        self.assertFalse(p1.isfriend)
        self.assertFalse(p1.isfamily)
        self.assertEqual(p1.ownername, "Bees / ?")
        self.assertEqual(p1.dateadded, "1089918707")

        # Verify pagination info
        self.assertEqual(photos.info.page, 1)
        self.assertEqual(photos.info.pages, 1)
        self.assertEqual(photos.info.perpage, 1)
        self.assertEqual(photos.info.total, 1)

    @patch.object(method_call.requests, "post")
    def test_group_remove_photo(self, mock_post):
        """Test Group.removePhoto (flickr.groups.pools.remove)"""
        # Empty response - method returns None
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="34427465497@N01")
        result = group.removePhoto(photo_id="12345678")

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
