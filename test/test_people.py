"""
Tests for People API methods.

flickr.people.findByEmail, flickr.people.findByUsername, flickr.people.getGroups,
flickr.people.getInfo, flickr.people.getLimits, flickr.people.getPhotos,
flickr.people.getPhotosOf, flickr.people.getPublicGroups, flickr.people.getPublicPhotos,
flickr.people.getUploadStatus
Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPeopleMethods(FlickrApiTestCase):
    """Tests for People-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_person_find_by_email(self, mock_post):
        """Test Person.findByEmail (flickr.people.findByEmail)"""
        api_doc = load_api_doc("flickr.people.findByEmail")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person.findByEmail(find_email="test@example.com")

        self.assertIsInstance(person, f.Person)
        self.assertEqual(person.id, "12037949632@N01")
        self.assertEqual(person.username, "Stewart")

    @patch.object(method_call.requests, "post")
    def test_person_find_by_username(self, mock_post):
        """Test Person.findByUserName (flickr.people.findByUsername)"""
        api_doc = load_api_doc("flickr.people.findByUsername")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person.findByUserName(username="Stewart")

        self.assertIsInstance(person, f.Person)
        self.assertEqual(person.id, "12037949632@N01")
        self.assertEqual(person.username, "Stewart")

    @patch.object(method_call.requests, "post")
    def test_group_get_member_groups(self, mock_post):
        """Test Group.getMemberGroups (flickr.people.getGroups)"""
        api_doc = load_api_doc("flickr.people.getGroups")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        groups = f.Group.getMemberGroups(user_id="12037949754@N01")

        # Verify we got 4 groups
        self.assertEqual(len(groups), 4)

        # First group
        g1 = groups[0]
        self.assertIsInstance(g1, f.Group)
        self.assertEqual(g1.nsid, "17274427@N00")
        self.assertEqual(g1.name, "Cream of the Crop - Please read the rules")
        self.assertEqual(g1.admin, 0)
        self.assertFalse(g1.eighteenplus)
        self.assertFalse(g1.invitation_only)
        self.assertEqual(g1.members, 11935)
        self.assertEqual(g1.pool_count, "12522")

        # Second group - Apple
        g2 = groups[1]
        self.assertEqual(g2.nsid, "20083316@N00")
        self.assertEqual(g2.name, "Apple")
        self.assertEqual(g2.members, 11776)

        # Third group - FlickrCentral
        g3 = groups[2]
        self.assertEqual(g3.nsid, "34427469792@N01")
        self.assertEqual(g3.name, "FlickrCentral")
        self.assertEqual(g3.members, 168055)
        self.assertEqual(g3.pool_count, "5280930")

        # Fourth group - Typography
        g4 = groups[3]
        self.assertEqual(g4.nsid, "37718678610@N01")
        self.assertEqual(g4.name, "Typography and Lettering")

    @patch.object(method_call.requests, "post")
    def test_person_get_info(self, mock_post):
        """Test Person.getInfo (flickr.people.getInfo)"""
        api_doc = load_api_doc("flickr.people.getInfo")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="12037949754@N01")
        person.getInfo()

        # Person object is updated with info
        self.assertEqual(person.id, "12037949754@N01")
        self.assertEqual(person.username, "bees")
        self.assertEqual(person.realname, "Cal Henderson")
        self.assertEqual(person.location, "Vancouver, Canada")
        self.assertEqual(person.photosurl, "http://www.flickr.com/photos/bees/")
        self.assertEqual(person.profileurl, "http://www.flickr.com/people/bees/")
        self.assertFalse(person.ispro)
        self.assertEqual(person.iconserver, "122")
        self.assertEqual(person.iconfarm, 1)

        # Photos info is stored in photos_info
        self.assertEqual(person.photos_info["firstdate"], "1071510391")
        self.assertEqual(person.photos_info["firstdatetaken"], "1900-09-02 09:11:24")
        self.assertEqual(person.photos_info["count"], "449")

    @patch.object(method_call.requests, "post")
    def test_person_get_limits(self, mock_post):
        """Test Person.getLimits (flickr.people.getLimits)"""
        api_doc = load_api_doc("flickr.people.getLimits")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="30135021@N05")
        limits = person.getLimits()

        # Returns the raw response dict
        self.assertIn("person", limits)
        self.assertEqual(limits["person"]["nsid"], "30135021@N05")

        # Check photos limits
        self.assertIn("photos", limits["person"])
        self.assertEqual(limits["person"]["photos"]["maxdisplaypx"], "1024")
        self.assertEqual(limits["person"]["photos"]["maxupload"], "15728640")

        # Check videos limits
        self.assertIn("videos", limits["person"])
        self.assertEqual(limits["person"]["videos"]["maxduration"], "90")
        self.assertEqual(limits["person"]["videos"]["maxupload"], "157286400")

    @patch.object(method_call.requests, "post")
    def test_person_get_photos(self, mock_post):
        """Test Person.getPhotos (flickr.people.getPhotos)"""
        api_doc = load_api_doc("flickr.people.getPhotos")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="47058503995@N01")
        photos = person.getPhotos()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        self.assertEqual(p1.owner.id, "47058503995@N01")
        self.assertEqual(p1.secret, "a123456")
        self.assertEqual(p1.server, "2")
        self.assertEqual(p1.title, "test_04")
        self.assertTrue(p1.ispublic)
        self.assertFalse(p1.isfriend)
        self.assertFalse(p1.isfamily)

        # Second photo - has friend/family access
        p2 = photos[1]
        self.assertEqual(p2.id, "2635")
        self.assertEqual(p2.title, "test_03")
        self.assertFalse(p2.ispublic)
        self.assertTrue(p2.isfriend)
        self.assertTrue(p2.isfamily)

        # Fourth photo - different owner
        p4 = photos[3]
        self.assertEqual(p4.id, "2610")
        self.assertEqual(p4.owner.id, "12037949754@N01")
        self.assertEqual(p4.title, "00_tall")

        # Verify pagination info
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.pages, 89)
        self.assertEqual(photos.info.perpage, 10)
        self.assertEqual(photos.info.total, 881)

    @patch.object(method_call.requests, "post")
    def test_person_get_photos_of(self, mock_post):
        """Test Person.getPhotosOf (flickr.people.getPhotosOf)"""
        api_doc = load_api_doc("flickr.people.getPhotosOf")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="12037949754@N01")
        photos = person.getPhotosOf()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        self.assertEqual(p1.owner.id, "47058503995@N01")
        self.assertEqual(p1.title, "test_04")

        # Second photo
        p2 = photos[1]
        self.assertEqual(p2.id, "2635")
        self.assertEqual(p2.title, "test_03")

        # Verify pagination info (uses has_next_page instead of pages/total)
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.perpage, 10)
        self.assertEqual(photos.info.has_next_page, 1)

    @patch.object(method_call.requests, "post")
    def test_person_get_public_groups(self, mock_post):
        """Test Person.getPublicGroups (flickr.people.getPublicGroups)"""
        api_doc = load_api_doc("flickr.people.getPublicGroups")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="12037949754@N01")
        groups = person.getPublicGroups()

        # Verify we got 3 groups
        self.assertEqual(len(groups), 3)

        # First group - FlickrCentral
        g1 = groups[0]
        self.assertIsInstance(g1, f.Group)
        self.assertEqual(g1.id, "34427469792@N01")
        self.assertEqual(g1.name, "FlickrCentral")
        self.assertEqual(g1.admin, 0)
        self.assertFalse(g1.eighteenplus)
        self.assertFalse(g1.invitation_only)

        # Second group - admin
        g2 = groups[1]
        self.assertEqual(g2.id, "37114057624@N01")
        self.assertEqual(g2.name, "Cal's Test Group")
        self.assertEqual(g2.admin, 1)
        self.assertTrue(g2.invitation_only)

        # Third group - 18+
        g3 = groups[2]
        self.assertEqual(g3.id, "34955637532@N01")
        self.assertEqual(g3.name, "18+ Group")
        self.assertTrue(g3.eighteenplus)

    @patch.object(method_call.requests, "post")
    def test_person_get_public_photos(self, mock_post):
        """Test Person.getPublicPhotos (flickr.people.getPublicPhotos)"""
        api_doc = load_api_doc("flickr.people.getPublicPhotos")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="47058503995@N01")
        photos = person.getPublicPhotos()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        self.assertEqual(p1.owner.id, "47058503995@N01")
        self.assertEqual(p1.title, "test_04")

        # Second photo
        p2 = photos[1]
        self.assertEqual(p2.id, "2635")
        self.assertEqual(p2.title, "test_03")

        # Verify pagination info
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.pages, 89)
        self.assertEqual(photos.info.perpage, 10)
        self.assertEqual(photos.info.total, 881)

    @patch.object(method_call.requests, "post")
    def test_person_get_upload_status(self, mock_post):
        """Test Person.getUploadStatus (flickr.people.getUploadStatus)"""
        api_doc = load_api_doc("flickr.people.getUploadStatus")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        status = f.Person.getUploadStatus()

        # Returns the user dict
        self.assertEqual(status["id"], "12037949754@N01")
        self.assertTrue(status["ispro"])
        self.assertEqual(status["username"], "Bees")

        # Check bandwidth info
        self.assertIn("bandwidth", status)
        self.assertEqual(status["bandwidth"]["maxbytes"], "2147483648")
        self.assertEqual(status["bandwidth"]["maxkb"], "2097152")
        self.assertEqual(status["bandwidth"]["usedbytes"], "383724")
        self.assertEqual(status["bandwidth"]["usedkb"], "374")
        self.assertEqual(status["bandwidth"]["remainingbytes"], "2147099924")
        self.assertEqual(status["bandwidth"]["remainingkb"], "2096777")

        # Check filesize info
        self.assertIn("filesize", status)
        self.assertEqual(status["filesize"]["maxbytes"], "10485760")
        self.assertEqual(status["filesize"]["maxkb"], "10240")

        # Check sets info
        self.assertIn("sets", status)
        self.assertEqual(status["sets"]["created"], "27")
        self.assertEqual(status["sets"]["remaining"], "lots")

        # Check videos info
        self.assertIn("videos", status)
        self.assertEqual(status["videos"]["uploaded"], "5")
        self.assertEqual(status["videos"]["remaining"], "lots")


if __name__ == "__main__":
    unittest.main()
