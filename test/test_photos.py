"""
Tests for Photo API methods.

Batch 10:
flickr.photos.addTags, flickr.photos.delete, flickr.photos.getAllContexts,
flickr.photos.getContactsPhotos, flickr.photos.getContactsPublicPhotos,
flickr.photos.getContext, flickr.photos.getCounts, flickr.photos.getExif,
flickr.photos.getFavorites, flickr.photos.getInfo

Batch 11:
flickr.photos.getNotInSet, flickr.photos.getPerms, flickr.photos.getRecent,
flickr.photos.getSizes, flickr.photos.getUntagged, flickr.photos.getWithGeoData,
flickr.photos.getWithoutGeoData, flickr.photos.recentlyUpdated, flickr.photos.search

Batch 15:
flickr.photos.removeTag, flickr.photos.setContentType, flickr.photos.setDates,
flickr.photos.setMeta, flickr.photos.setPerms, flickr.photos.setSafetyLevel

Batch 16:
flickr.photos.setTags, flickr.photos.transform.rotate, flickr.photos.upload.checkTickets

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPhotoMethods(FlickrApiTestCase):
    """Tests for Photo-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_photo_add_tags(self, mock_post):
        """Test Photo.addTags (flickr.photos.addTags)"""
        # Empty response for write operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.addTags(tags="tag1, tag2")

        # Write operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_add_tags_list(self, mock_post):
        """Test Photo.addTags with list input (flickr.photos.addTags)"""
        # Empty response for write operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.addTags(tags=["tag1", "tag2", "tag3"])

        # Write operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_delete(self, mock_post):
        """Test Photo.delete (flickr.photos.delete)"""
        # Empty response for delete operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.delete()

        # Delete operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_get_all_contexts(self, mock_post):
        """Test Photo.getAllContexts (flickr.photos.getAllContexts)"""
        # XML has multiple root elements, so construct JSON manually
        # Based on api-docs response:
        # <set id="392" title="记忆群组" />
        # <pool id="34427465471@N01" title="FlickrDiscuss" />
        json_response = {
            "set": [{"id": "392", "title": "记忆群组"}],
            "pool": [{"id": "34427465471@N01", "title": "FlickrDiscuss"}]
        }

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="12345")
        photosets, pools = photo.getAllContexts()

        # Verify photosets
        self.assertEqual(len(photosets), 1)
        self.assertIsInstance(photosets[0], f.Photoset)
        self.assertEqual(photosets[0].id, "392")
        self.assertEqual(photosets[0].title, "记忆群组")

        # Verify pools (groups)
        self.assertEqual(len(pools), 1)
        self.assertIsInstance(pools[0], f.Group)
        self.assertEqual(pools[0].id, "34427465471@N01")
        self.assertEqual(pools[0].title, "FlickrDiscuss")

    @patch.object(method_call.requests, "post")
    def test_photo_get_contacts_photos(self, mock_post):
        """Test Photo.getContactsPhotos (flickr.photos.getContactsPhotos)"""
        # Based on api-docs response, construct JSON with proper structure
        json_response = {
            "photos": {
                "photo": [
                    {"id": "2801", "owner": "12037949629@N01", "secret": "123456",
                     "server": "1", "username": "Eric is the best", "title": "grease"},
                    {"id": "2499", "owner": "33853651809@N01", "secret": "123456",
                     "server": "1", "username": "cal18", "title": "36679_o"},
                    {"id": "2437", "owner": "12037951898@N01", "secret": "123456",
                     "server": "1", "username": "georgie parker", "title": "phoenix9_stewart"}
                ]
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="12345")
        photos = photo.getContactsPhotos()

        # Verify we got 3 photos
        self.assertEqual(len(photos), 3)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2801")
        self.assertEqual(p1.owner, "12037949629@N01")
        self.assertEqual(p1.secret, "123456")
        self.assertEqual(p1.server, "1")
        self.assertEqual(p1.username, "Eric is the best")
        self.assertEqual(p1.title, "grease")

        # Second photo
        p2 = photos[1]
        self.assertEqual(p2.id, "2499")
        self.assertEqual(p2.owner, "33853651809@N01")
        self.assertEqual(p2.username, "cal18")
        self.assertEqual(p2.title, "36679_o")

        # Third photo
        p3 = photos[2]
        self.assertEqual(p3.id, "2437")
        self.assertEqual(p3.owner, "12037951898@N01")
        self.assertEqual(p3.username, "georgie parker")
        self.assertEqual(p3.title, "phoenix9_stewart")

    @patch.object(method_call.requests, "post")
    def test_person_get_contacts_public_photos(self, mock_post):
        """Test Person.getContactsPublicPhotos (flickr.photos.getContactsPublicPhotos)"""
        api_doc = load_api_doc("flickr.photos.getContactsPublicPhotos")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="12037949754@N01")
        photos = person.getContactsPublicPhotos()

        # Verify we got 3 photos
        self.assertEqual(len(photos), 3)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2801")
        self.assertEqual(p1.owner.id, "12037949629@N01")
        self.assertEqual(p1.title, "grease")

        # Second photo
        p2 = photos[1]
        self.assertEqual(p2.id, "2499")
        self.assertEqual(p2.title, "36679_o")

        # Third photo
        p3 = photos[2]
        self.assertEqual(p3.id, "2437")
        self.assertEqual(p3.title, "phoenix9_stewart")

    @patch.object(method_call.requests, "post")
    def test_photo_get_context(self, mock_post):
        """Test Photo.getContext (flickr.photos.getContext)"""
        # XML has multiple root elements, construct JSON manually
        # Based on api-docs response:
        # <prevphoto id="2980" secret="973da1e709" title="boo!" url="/photos/bees/2980/" />
        # <nextphoto id="2985" secret="059b664012" title="Amsterdam Amstel" ... />
        json_response = {
            "prevphoto": {"id": "2980", "secret": "973da1e709",
                         "title": "boo!", "url": "/photos/bees/2980/"},
            "nextphoto": {"id": "2985", "secret": "059b664012",
                         "title": "Amsterdam Amstel", "url": "/photos/bees/2985/"}
        }

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="2982")
        prev_photo, next_photo = photo.getContext()

        # Verify prev photo
        self.assertIsInstance(prev_photo, f.Photo)
        self.assertEqual(prev_photo.id, "2980")
        self.assertEqual(prev_photo.secret, "973da1e709")
        self.assertEqual(prev_photo.title, "boo!")
        self.assertEqual(prev_photo.url, "/photos/bees/2980/")

        # Verify next photo
        self.assertIsInstance(next_photo, f.Photo)
        self.assertEqual(next_photo.id, "2985")
        self.assertEqual(next_photo.secret, "059b664012")
        self.assertEqual(next_photo.title, "Amsterdam Amstel")
        self.assertEqual(next_photo.url, "/photos/bees/2985/")

    @patch.object(method_call.requests, "post")
    def test_person_get_photo_counts(self, mock_post):
        """Test Person.getPhotoCounts (flickr.photos.getCounts)"""
        api_doc = load_api_doc("flickr.photos.getCounts")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="12037949754@N01")
        counts = person.getPhotoCounts(dates="1093566950,1093653350")

        # Verify we got 7 photocount entries
        self.assertEqual(len(counts), 7)

        # First entry - has 4 photos
        c1 = counts[0]
        self.assertEqual(c1["count"], "4")
        self.assertEqual(c1["fromdate"], "1093566950")
        self.assertEqual(c1["todate"], "1093653350")

        # Second entry - has 0 photos (note: "0" is converted to int 0 by xml_to_flickr_json)
        c2 = counts[1]
        self.assertEqual(c2["count"], 0)
        self.assertEqual(c2["fromdate"], "1093653350")
        self.assertEqual(c2["todate"], "1093739750")

        # Fourth entry - has 2 photos
        c4 = counts[3]
        self.assertEqual(c4["count"], "2")
        self.assertEqual(c4["fromdate"], "1093826150")
        self.assertEqual(c4["todate"], "1093912550")

    @patch.object(method_call.requests, "post")
    def test_photo_get_exif(self, mock_post):
        """Test Photo.getExif (flickr.photos.getExif)"""
        api_doc = load_api_doc("flickr.photos.getExif")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="4424", secret="06b8e43bc7")
        exif_data = photo.getExif()

        # Verify we got 3 EXIF entries
        self.assertEqual(len(exif_data), 3)

        # First entry - TIFF Manufacturer
        # Note: tagspaceid="1" is converted to int 1 by xml_to_flickr_json
        # Note: {"_content": "Canon"} is cleaned to just "Canon" by clean_content
        e1 = exif_data[0]
        self.assertIsInstance(e1, f.Photo.Exif)
        self.assertEqual(e1.tagspace, "TIFF")
        self.assertEqual(e1.tagspaceid, 1)
        self.assertEqual(e1.tag, "271")
        self.assertEqual(e1.label, "Manufacturer")
        self.assertEqual(e1.raw, "Canon")

        # Second entry - EXIF Aperture (has clean value)
        # Note: tagspaceid="0" is converted to int 0
        e2 = exif_data[1]
        self.assertEqual(e2.tagspace, "EXIF")
        self.assertEqual(e2.tagspaceid, 0)
        self.assertEqual(e2.tag, "33437")
        self.assertEqual(e2.label, "Aperture")
        self.assertEqual(e2.raw, "90/10")
        self.assertEqual(e2.clean, "f/9")

        # Third entry - GPS Longitude
        e3 = exif_data[2]
        self.assertEqual(e3.tagspace, "GPS")
        self.assertEqual(e3.tagspaceid, "3")
        self.assertEqual(e3.tag, "4")
        self.assertEqual(e3.label, "Longitude")

    @patch.object(method_call.requests, "post")
    def test_photo_get_favorites(self, mock_post):
        """Test Photo.getFavorites (flickr.photos.getFavorites)"""
        api_doc = load_api_doc("flickr.photos.getFavorites")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="1253576")
        persons = photo.getFavorites()

        # Verify we got 10 persons
        self.assertEqual(len(persons), 10)

        # First person
        p1 = persons[0]
        self.assertIsInstance(p1, f.Person)
        self.assertEqual(p1.id, "33939862@N00")
        self.assertEqual(p1.username, "Dementation")
        self.assertEqual(p1.favedate, "1166689690")

        # Second person
        p2 = persons[1]
        self.assertEqual(p2.id, "49485425@N00")
        self.assertEqual(p2.username, "indigenous_prodigy")
        self.assertEqual(p2.favedate, "1166573724")

        # Last person
        p10 = persons[9]
        self.assertEqual(p10.id, "54309070@N00")
        self.assertEqual(p10.username, "Shinayaker")
        self.assertEqual(p10.favedate, "1142584219")

        # Verify pagination info
        self.assertEqual(persons.info.page, 1)
        self.assertEqual(persons.info.pages, 3)
        self.assertEqual(persons.info.perpage, 10)
        self.assertEqual(persons.info.total, 27)

    @patch.object(method_call.requests, "post")
    def test_photo_get_info(self, mock_post):
        """Test Photo.getInfo (flickr.photos.getInfo)"""
        # Construct complete JSON response with all required fields
        # The library expects: usage, visibility, publiceditability, dates
        json_response = {
            "photo": {
                "id": "2733",
                "secret": "123456",
                "server": "12",
                "isfavorite": 0,
                "license": "3",
                "rotation": "90",
                "originalsecret": "1bc09ce34a",
                "originalformat": "png",
                "owner": {
                    "nsid": "12037949754@N01",
                    "username": "Bees",
                    "realname": "Cal Henderson",
                    "location": "Bedford, UK"
                },
                "title": {"_content": "orford_castle_taster"},
                "description": {"_content": "hello!"},
                "visibility": {"ispublic": 1, "isfriend": 0, "isfamily": 0},
                "dates": {
                    "posted": "1100897479",
                    "taken": "2004-11-19 12:51:19",
                    "takengranularity": 0,
                    "lastupdate": "1093022469"
                },
                "usage": {
                    "candownload": 1,
                    "canblog": 1,
                    "canprint": 1,
                    "canshare": 1
                },
                "publiceditability": {
                    "cancomment": 1,
                    "canaddmeta": 1
                },
                "comments": {"_content": "1"},
                "notes": {
                    "note": [{
                        "id": "313",
                        "author": "12037949754@N01",
                        "authorname": "Bees",
                        "x": "10",
                        "y": "10",
                        "w": "50",
                        "h": "50",
                        "_content": "foo"
                    }]
                },
                "tags": {
                    "tag": [
                        {"id": "1234", "author": "12037949754@N01",
                         "raw": "woo yay", "_content": "wooyay"},
                        {"id": "1235", "author": "12037949754@N01",
                         "raw": "hoopla", "_content": "hoopla"}
                    ]
                },
                "urls": {
                    "url": [{"type": "photopage",
                             "_content": "http://www.flickr.com/photos/bees/2733/"}]
                }
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="2733")
        photo.getInfo()

        # Verify basic photo info
        self.assertEqual(photo.id, "2733")
        self.assertEqual(photo.secret, "123456")
        self.assertEqual(photo.server, "12")
        self.assertFalse(photo.isfavorite)
        self.assertEqual(photo.license, "3")
        self.assertEqual(photo.rotation, "90")
        self.assertEqual(photo.originalsecret, "1bc09ce34a")
        self.assertEqual(photo.originalformat, "png")

        # Verify owner info
        self.assertIsInstance(photo.owner, f.Person)
        self.assertEqual(photo.owner.id, "12037949754@N01")
        self.assertEqual(photo.owner.username, "Bees")
        self.assertEqual(photo.owner.realname, "Cal Henderson")
        self.assertEqual(photo.owner.location, "Bedford, UK")

        # Verify title and description
        # Note: {"_content": "..."} is cleaned to just the string by clean_content
        self.assertEqual(photo.title, "orford_castle_taster")
        self.assertEqual(photo.description, "hello!")

        # Verify visibility (merged into photo)
        self.assertTrue(photo.ispublic)
        self.assertFalse(photo.isfriend)
        self.assertFalse(photo.isfamily)

        # Verify dates (merged into photo)
        # Note: posted and lastupdate are converted to int by dict_converter
        self.assertEqual(photo.posted, 1100897479)
        self.assertEqual(photo.taken, "2004-11-19 12:51:19")
        self.assertEqual(photo.takengranularity, 0)
        self.assertEqual(photo.lastupdate, 1093022469)

        # Verify usage (merged into photo)
        self.assertTrue(photo.candownload)
        self.assertTrue(photo.canblog)
        self.assertTrue(photo.canprint)
        self.assertTrue(photo.canshare)

        # Verify tags
        self.assertEqual(len(photo.tags), 2)
        self.assertIsInstance(photo.tags[0], f.Tag)
        self.assertEqual(photo.tags[0].id, "1234")
        self.assertIsInstance(photo.tags[0].author, f.Person)
        self.assertEqual(photo.tags[0].author.id, "12037949754@N01")
        self.assertEqual(photo.tags[0].raw, "woo yay")
        self.assertEqual(photo.tags[0].text, "wooyay")

        self.assertEqual(photo.tags[1].id, "1235")
        self.assertEqual(photo.tags[1].raw, "hoopla")
        self.assertEqual(photo.tags[1].text, "hoopla")

        # Verify notes
        self.assertEqual(len(photo.notes), 1)
        self.assertIsInstance(photo.notes[0], f.Photo.Note)
        self.assertEqual(photo.notes[0].id, "313")
        self.assertEqual(photo.notes[0].author, "12037949754@N01")
        self.assertEqual(photo.notes[0].authorname, "Bees")
        self.assertEqual(photo.notes[0].x, "10")
        self.assertEqual(photo.notes[0].y, "10")
        self.assertEqual(photo.notes[0].w, "50")
        self.assertEqual(photo.notes[0].h, "50")
        # Note: _content is renamed to text by clean_content
        self.assertEqual(photo.notes[0].text, "foo")


    @patch.object(method_call.requests, "post")
    def test_person_get_not_in_set_photos(self, mock_post):
        """Test Person.getNotInSetPhotos (flickr.photos.getNotInSet)"""
        api_doc = load_api_doc("flickr.photos.getNotInSet")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        # getNotInSetPhotos is a static method on Person
        photos = f.Person.getNotInSetPhotos()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo - public
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        # owner is converted to Person object by _extract_photo_list
        self.assertIsInstance(p1.owner, f.Person)
        self.assertEqual(p1.owner.id, "47058503995@N01")
        self.assertEqual(p1.secret, "a123456")
        self.assertEqual(p1.server, "2")
        self.assertEqual(p1.title, "test_04")
        self.assertTrue(p1.ispublic)
        self.assertFalse(p1.isfriend)
        self.assertFalse(p1.isfamily)

        # Second photo - private (friend & family)
        p2 = photos[1]
        self.assertEqual(p2.id, "2635")
        self.assertEqual(p2.title, "test_03")
        self.assertFalse(p2.ispublic)
        self.assertTrue(p2.isfriend)
        self.assertTrue(p2.isfamily)

        # Third photo
        p3 = photos[2]
        self.assertEqual(p3.id, "2633")
        self.assertEqual(p3.title, "test_01")

        # Fourth photo
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
    def test_photo_get_perms(self, mock_post):
        """Test Photo.getPerms (flickr.photos.getPerms)"""
        api_doc = load_api_doc("flickr.photos.getPerms")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="2733")
        perms = photo.getPerms()

        # Verify permissions response - returns raw dict
        self.assertEqual(perms["perms"]["id"], "2733")
        self.assertEqual(perms["perms"]["ispublic"], 1)
        self.assertEqual(perms["perms"]["isfriend"], 1)
        self.assertEqual(perms["perms"]["isfamily"], 0)
        self.assertEqual(perms["perms"]["permcomment"], 0)
        self.assertEqual(perms["perms"]["permaddmeta"], 1)

    @patch.object(method_call.requests, "post")
    def test_photo_get_recent(self, mock_post):
        """Test Photo.getRecent (flickr.photos.getRecent)"""
        api_doc = load_api_doc("flickr.photos.getRecent")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photos = f.Photo.getRecent()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        # owner is converted to Person object by _extract_photo_list
        self.assertIsInstance(p1.owner, f.Person)
        self.assertEqual(p1.owner.id, "47058503995@N01")
        self.assertEqual(p1.secret, "a123456")
        self.assertEqual(p1.title, "test_04")
        self.assertTrue(p1.ispublic)

        # Verify pagination info
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.pages, 89)
        self.assertEqual(photos.info.perpage, 10)
        self.assertEqual(photos.info.total, 881)

    @patch.object(method_call.requests, "post")
    def test_photo_get_sizes(self, mock_post):
        """Test Photo.getSizes (flickr.photos.getSizes)"""
        api_doc = load_api_doc("flickr.photos.getSizes")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="567229075")
        sizes = photo.getSizes()

        # Verify sizes dict is keyed by label
        self.assertIn("Square", sizes)
        self.assertIn("Large Square", sizes)
        self.assertIn("Thumbnail", sizes)
        self.assertIn("Small", sizes)
        self.assertIn("Small 320", sizes)
        self.assertIn("Medium", sizes)
        self.assertIn("Medium 640", sizes)
        self.assertIn("Medium 800", sizes)
        self.assertIn("Large", sizes)
        self.assertIn("Original", sizes)

        # Verify Square size details
        square = sizes["Square"]
        self.assertEqual(square["label"], "Square")
        self.assertEqual(square["width"], "75")
        self.assertEqual(square["height"], "75")
        self.assertIn("farm2.staticflickr.com", square["source"])
        self.assertEqual(square["media"], "photo")

        # Verify Large size
        large = sizes["Large"]
        self.assertEqual(large["width"], "1024")
        self.assertEqual(large["height"], "768")

        # Verify Original size
        original = sizes["Original"]
        self.assertEqual(original["width"], "2400")
        self.assertEqual(original["height"], "1800")

    @patch.object(method_call.requests, "post")
    def test_photo_get_untagged(self, mock_post):
        """Test Photo.getUntagged (flickr.photos.getUntagged)"""
        api_doc = load_api_doc("flickr.photos.getUntagged")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photos = f.Photo.getUntagged()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        self.assertEqual(p1.title, "test_04")

        # Verify pagination info
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.pages, 89)

    @patch.object(method_call.requests, "post")
    def test_photo_get_with_geo_data(self, mock_post):
        """Test Photo.getWithGeoData (flickr.photos.getWithGeoData)"""
        api_doc = load_api_doc("flickr.photos.getWithGeoData")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photos = f.Photo.getWithGeoData()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        self.assertEqual(p1.title, "test_04")

        # Verify pagination info
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.pages, 89)

    @patch.object(method_call.requests, "post")
    def test_photo_get_without_geo_data(self, mock_post):
        """Test Photo.getWithoutGeoData (flickr.photos.getWithoutGeoData)"""
        api_doc = load_api_doc("flickr.photos.getWithoutGeoData")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photos = f.Photo.getWithoutGeoData()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        self.assertEqual(p1.title, "test_04")

        # Verify pagination info
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.pages, 89)

    @patch.object(method_call.requests, "post")
    def test_photo_recently_updated(self, mock_post):
        """Test Photo.recentlyUpdated (flickr.photos.recentlyUpdated)"""
        api_doc = load_api_doc("flickr.photos.recentlyUpdated")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photos = f.Photo.recentlyUpdated(min_date="1150000000")

        # Verify we got 2 photos
        self.assertEqual(len(photos), 2)

        # First photo - has lastupdate field
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "169885459")
        self.assertIsInstance(p1.owner, f.Person)
        self.assertEqual(p1.owner.id, "35034348999@N01")
        self.assertEqual(p1.secret, "c85114c195")
        self.assertEqual(p1.server, "46")
        self.assertEqual(p1.title, "Doubting Michael")
        self.assertTrue(p1.ispublic)
        # lastupdate is converted to int by the library
        self.assertEqual(p1.lastupdate, 1150755888)

        # Second photo - title has quotes in it (from &quot; in XML)
        p2 = photos[1]
        self.assertEqual(p2.id, "85022332")
        self.assertEqual(
            p2.title,
            "\"Do you think we're allowed to tape stuff to the walls?\""
        )
        self.assertEqual(p2.lastupdate, 1150564974)

        # Verify pagination info
        self.assertEqual(photos.info.page, 1)
        self.assertEqual(photos.info.pages, 1)
        self.assertEqual(photos.info.perpage, 100)
        self.assertEqual(photos.info.total, 2)

    @patch.object(method_call.requests, "post")
    def test_photo_search(self, mock_post):
        """Test Photo.search (flickr.photos.search)"""
        api_doc = load_api_doc("flickr.photos.search")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photos = f.Photo.search(tags="test")

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
        # owner is converted to Person object by _extract_photo_list
        self.assertIsInstance(p1.owner, f.Person)
        self.assertEqual(p1.owner.id, "47058503995@N01")
        self.assertEqual(p1.secret, "a123456")
        self.assertEqual(p1.title, "test_04")
        self.assertTrue(p1.ispublic)

        # Second photo - private
        p2 = photos[1]
        self.assertEqual(p2.id, "2635")
        self.assertEqual(p2.title, "test_03")
        self.assertFalse(p2.ispublic)
        self.assertTrue(p2.isfriend)
        self.assertTrue(p2.isfamily)

        # Verify pagination info
        self.assertEqual(photos.info.page, 2)
        self.assertEqual(photos.info.pages, 89)
        self.assertEqual(photos.info.perpage, 10)
        self.assertEqual(photos.info.total, 881)

    # Batch 15 tests

    @patch.object(method_call.requests, "post")
    def test_tag_remove(self, mock_post):
        """Test Tag.remove (flickr.photos.removeTag)"""
        # Empty response for remove operation
        mock_post.return_value = self._mock_response({})

        tag = f.Tag(id="12345-67890")
        result = tag.remove()

        # Remove returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_content_type(self, mock_post):
        """Test Photo.setContentType (flickr.photos.setContentType)"""
        # Empty response (library ignores response content)
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="14814")
        result = photo.setContentType(content_type=3)

        # setContentType returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_dates(self, mock_post):
        """Test Photo.setDates (flickr.photos.setDates)"""
        # Empty response for set operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.setDates(date_taken="2024-01-15 10:30:00")

        # setDates returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_dates_with_granularity(self, mock_post):
        """Test Photo.setDates with granularity (flickr.photos.setDates)"""
        # Empty response for set operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.setDates(
            date_taken="2024-01-15 10:30:00",
            date_taken_granularity=0
        )

        # setDates returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_meta(self, mock_post):
        """Test Photo.setMeta (flickr.photos.setMeta)"""
        # Empty response for set operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.setMeta(title="New Title", description="New description")

        # setMeta returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_meta_title_only(self, mock_post):
        """Test Photo.setMeta with title only (flickr.photos.setMeta)"""
        # Empty response for set operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.setMeta(title="New Title")

        # setMeta returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_perms(self, mock_post):
        """Test Photo.setPerms (flickr.photos.setPerms)"""
        # Empty response (library ignores response content)
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.setPerms(is_public=1, is_friend=1, is_family=0)

        # setPerms returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_perms_with_comments(self, mock_post):
        """Test Photo.setPerms with comment perms (flickr.photos.setPerms)"""
        # Empty response (library ignores response content)
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.setPerms(
            is_public=0,
            is_friend=1,
            is_family=1,
            perm_comment=1,
            perm_addmeta=2
        )

        # setPerms returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_safety_level(self, mock_post):
        """Test Photo.setSafetyLevel (flickr.photos.setSafetyLevel)"""
        # Empty response (library ignores response content)
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="14814")
        result = photo.setSafetyLevel(safety_level=2)

        # setSafetyLevel returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_set_safety_level_with_hidden(self, mock_post):
        """Test Photo.setSafetyLevel with hidden (flickr.photos.setSafetyLevel)"""
        # Empty response (library ignores response content)
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="14814")
        result = photo.setSafetyLevel(safety_level=3, hidden=1)

        # setSafetyLevel returns None
        self.assertIsNone(result)

    # Batch 16 tests

    @patch.object(method_call.requests, "post")
    def test_photo_set_tags(self, mock_post):
        """Test Photo.setTags (flickr.photos.setTags)"""
        # Empty response for set operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345")
        result = photo.setTags(tags="landscape sunset mountain")

        # setTags returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_rotate(self, mock_post):
        """Test Photo.rotate (flickr.photos.transform.rotate)"""
        # Response based on api-docs: <photoid secret="abcdef" originalsecret="abcdef">1234</photoid>
        # After clean_content processing, _content becomes "text" when other keys exist
        json_response = {
            "photo_id": {
                "text": "1234",
                "secret": "abcdef",
                "originalsecret": "abcdef"
            }
        }
        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="1234")
        result = photo.rotate(degrees=90)

        # rotate returns a new Photo object with updated secret
        self.assertIsInstance(result, f.Photo)
        self.assertEqual(result.id, "1234")
        self.assertEqual(result.secret, "abcdef")

    @patch.object(method_call.requests, "post")
    def test_photo_rotate_180(self, mock_post):
        """Test Photo.rotate 180 degrees (flickr.photos.transform.rotate)"""
        json_response = {
            "photo_id": {
                "text": "5678",
                "secret": "newsecret123",
                "originalsecret": "newsecret123"
            }
        }
        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="5678")
        result = photo.rotate(degrees=180)

        self.assertIsInstance(result, f.Photo)
        self.assertEqual(result.id, "5678")
        self.assertEqual(result.secret, "newsecret123")

    @patch.object(method_call.requests, "post")
    def test_photo_check_upload_tickets(self, mock_post):
        """Test Photo.checkUploadTickets (flickr.photos.upload.checkTickets)"""
        # Response based on api-docs uploader/ticket structure
        json_response = {
            "uploader": {
                "ticket": [
                    {"id": "128", "complete": 1, "photoid": "2995"},
                    {"id": "129", "complete": 0},
                    {"id": "130", "complete": "2"},
                    {"id": "131", "invalid": 1}
                ]
            }
        }
        mock_post.return_value = self._mock_response(json_response)

        tickets = f.Photo.checkUploadTickets(["128", "129", "130", "131"])

        # Verify we got 4 upload tickets
        self.assertEqual(len(tickets), 4)

        # First ticket - complete with photo id
        t1 = tickets[0]
        self.assertIsInstance(t1, f.UploadTicket)
        self.assertEqual(t1.id, "128")
        self.assertEqual(t1.complete, 1)
        self.assertEqual(t1.photoid, "2995")

        # Second ticket - not complete yet
        t2 = tickets[1]
        self.assertEqual(t2.id, "129")
        self.assertEqual(t2.complete, 0)

        # Third ticket - complete status 2 (failed)
        t3 = tickets[2]
        self.assertEqual(t3.id, "130")
        self.assertEqual(t3.complete, "2")

        # Fourth ticket - invalid
        t4 = tickets[3]
        self.assertEqual(t4.id, "131")
        self.assertEqual(t4.invalid, 1)

    @patch.object(method_call.requests, "post")
    def test_photo_check_upload_tickets_single(self, mock_post):
        """Test Photo.checkUploadTickets with single ticket
        (flickr.photos.upload.checkTickets)"""
        # When only one ticket, response may not be a list
        json_response = {
            "uploader": {
                "ticket": {"id": "128", "complete": 1, "photoid": "2995"}
            }
        }
        mock_post.return_value = self._mock_response(json_response)

        tickets = f.Photo.checkUploadTickets(["128"])

        # Verify we got 1 upload ticket (library wraps single item in list)
        self.assertEqual(len(tickets), 1)

        t1 = tickets[0]
        self.assertIsInstance(t1, f.UploadTicket)
        self.assertEqual(t1.id, "128")
        self.assertEqual(t1.complete, 1)
        self.assertEqual(t1.photoid, "2995")


if __name__ == "__main__":
    unittest.main()
