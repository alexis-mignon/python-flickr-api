"""
Tests for Photoset API methods.

Batch 17:
flickr.photosets.addPhoto, flickr.photosets.comments.addComment,
flickr.photosets.comments.deleteComment, flickr.photosets.comments.editComment,
flickr.photosets.comments.getList, flickr.photosets.create, flickr.photosets.delete,
flickr.photosets.editMeta, flickr.photosets.editPhotos, flickr.photosets.getContext

Batch 18:
flickr.photosets.getInfo, flickr.photosets.getList, flickr.photosets.getPhotos,
flickr.photosets.orderSets, flickr.photosets.removePhoto, flickr.photosets.removePhotos,
flickr.photosets.reorderPhotos, flickr.photosets.setPrimaryPhoto

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPhotosetMethods(FlickrApiTestCase):
    """Tests for Photoset API methods"""

    @patch.object(method_call.requests, "post")
    def test_photoset_add_photo(self, mock_post):
        """Test Photoset.addPhoto (flickr.photosets.addPhoto)"""
        # Empty response for add operation
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        result = photoset.addPhoto(photo_id="12345")

        # Add operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_add_photo_with_object(self, mock_post):
        """Test Photoset.addPhoto with Photo object"""
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        photo = f.Photo(id="12345")
        result = photoset.addPhoto(photo=photo)

        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_add_comment(self, mock_post):
        """Test Photoset.addComment (flickr.photosets.comments.addComment)"""
        api_doc = load_api_doc("flickr.photosets.comments.addComment")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photoset = f.Photoset(id="12492")
        comment = photoset.addComment(comment_text="Nice set!")

        # Verify comment object is returned
        self.assertIsInstance(comment, f.Photoset.Comment)
        self.assertEqual(comment.id, "97777-12492-72057594037942601")
        # The photoset reference is set on the comment
        self.assertEqual(comment.photoset, photoset)

    @patch.object(method_call.requests, "post")
    def test_photoset_comment_delete(self, mock_post):
        """Test Photoset.Comment.delete (flickr.photosets.comments.deleteComment)"""
        # Empty response for delete operation
        mock_post.return_value = self._mock_response({})

        comment = f.Photoset.Comment(id="6065-109722179-72057594077818641")
        result = comment.delete()

        # Delete operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_comment_edit(self, mock_post):
        """Test Photoset.Comment.edit (flickr.photosets.comments.editComment)"""
        # Empty response for edit operation
        mock_post.return_value = self._mock_response({})

        comment = f.Photoset.Comment(id="6065-109722179-72057594077818641")
        result = comment.edit(comment_text="Updated comment text")

        # Edit operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_get_comments(self, mock_post):
        """Test Photoset.getComments (flickr.photosets.comments.getList)"""
        api_doc = load_api_doc("flickr.photosets.comments.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photoset = f.Photoset(id="109722179")
        comments = photoset.getComments()

        # Verify we got 1 comment
        self.assertEqual(len(comments), 1)

        # Verify comment details
        c1 = comments[0]
        self.assertIsInstance(c1, f.Photoset.Comment)
        self.assertEqual(c1.id, "6065-109722179-72057594077818641")
        self.assertEqual(c1.date_create, "1141841470")
        self.assertEqual(
            c1.permalink,
            "http://www.flickr.com/photos/straup/109722179/"
            "#comment72057594077818641"
        )
        self.assertEqual(
            c1.text,
            "Umm, I'm not sure, can I get back to you on that one?"
        )

        # Verify author is a Person object
        self.assertIsInstance(c1.author, f.Person)
        self.assertEqual(c1.author.id, "35468159852@N01")
        self.assertEqual(c1.author.username, "Rev Dan Catt")

    @patch.object(method_call.requests, "post")
    def test_photoset_get_comments_empty(self, mock_post):
        """Test Photoset.getComments with no comments"""
        json_response = {
            "comments": {
                "photoset_id": "109722179"
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        photoset = f.Photoset(id="109722179")
        comments = photoset.getComments()

        # Verify empty list returned
        self.assertEqual(len(comments), 0)

    @patch.object(method_call.requests, "post")
    def test_photoset_create(self, mock_post):
        """Test Photoset.create (flickr.photosets.create)"""
        api_doc = load_api_doc("flickr.photosets.create")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        primary_photo = f.Photo(id="98765")
        photoset = f.Photoset.create(
            title="My New Set",
            primary_photo=primary_photo
        )

        # Verify photoset object is returned
        self.assertIsInstance(photoset, f.Photoset)
        self.assertEqual(photoset.id, "1234")
        self.assertEqual(photoset.url, "http://www.flickr.com/photos/bees/sets/1234/")
        # Primary photo is set
        self.assertEqual(photoset.primary, primary_photo)

    @patch.object(method_call.requests, "post")
    def test_photoset_create_with_photo_id(self, mock_post):
        """Test Photoset.create with primary_photo_id"""
        api_doc = load_api_doc("flickr.photosets.create")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photoset = f.Photoset.create(
            title="My New Set",
            primary_photo_id="98765"
        )

        self.assertIsInstance(photoset, f.Photoset)
        self.assertEqual(photoset.id, "1234")
        # Primary photo is created from ID
        self.assertIsInstance(photoset.primary, f.Photo)
        self.assertEqual(photoset.primary.id, "98765")

    @patch.object(method_call.requests, "post")
    def test_photoset_delete(self, mock_post):
        """Test Photoset.delete (flickr.photosets.delete)"""
        # Empty response for delete operation
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        result = photoset.delete()

        # Delete operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_edit_meta(self, mock_post):
        """Test Photoset.editMeta (flickr.photosets.editMeta)"""
        # Empty response for editMeta operation
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        result = photoset.editMeta(title="New Title", description="New desc")

        # EditMeta operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_edit_photos(self, mock_post):
        """Test Photoset.editPhotos (flickr.photosets.editPhotos)"""
        # Empty response for editPhotos operation
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        result = photoset.editPhotos(
            primary_photo_id="12345",
            photo_ids=["12345", "67890", "11111"]
        )

        # EditPhotos operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_get_context(self, mock_post):
        """Test Photoset.getContext (flickr.photosets.getContext)"""
        # Construct JSON manually since API doc has two sibling XML elements
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

        photoset = f.Photoset(id="72157594042012345")
        prev_photo, next_photo = photoset.getContext(photo_id="2983")

        # Verify prev and next photos
        self.assertIsInstance(prev_photo, f.Photo)
        self.assertEqual(prev_photo.id, "2980")
        self.assertEqual(prev_photo.secret, "973da1e709")
        self.assertEqual(prev_photo.title, "boo!")
        self.assertEqual(prev_photo.url, "/photos/bees/2980/")

        self.assertIsInstance(next_photo, f.Photo)
        self.assertEqual(next_photo.id, "2985")
        self.assertEqual(next_photo.secret, "059b664012")
        self.assertEqual(next_photo.title, "Amsterdam Amstel")
        self.assertEqual(next_photo.url, "/photos/bees/2985/")

    @patch.object(method_call.requests, "post")
    def test_photoset_get_context_with_photo_object(self, mock_post):
        """Test Photoset.getContext with Photo object"""
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

        photoset = f.Photoset(id="72157594042012345")
        photo = f.Photo(id="2983")
        prev_photo, next_photo = photoset.getContext(photo=photo)

        self.assertIsInstance(prev_photo, f.Photo)
        self.assertIsInstance(next_photo, f.Photo)

    # Batch 18 tests

    @patch.object(method_call.requests, "post")
    def test_photoset_get_info(self, mock_post):
        """Test Photoset.getInfo (flickr.photosets.getInfo)"""
        api_doc = load_api_doc("flickr.photosets.getInfo")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photoset = f.Photoset(id="72157624618609504")
        info = photoset.getInfo()

        # getInfo returns updated attributes as a dict
        self.assertIsInstance(info, dict)
        self.assertEqual(info["id"], "72157624618609504")
        self.assertEqual(info["primary"], "4847770787")
        self.assertEqual(info["secret"], "6abd09a292")
        self.assertEqual(info["server"], "4153")
        self.assertEqual(info["farm"], "5")
        self.assertEqual(info["photos"], "55")
        self.assertEqual(info["count_views"], "523")
        self.assertEqual(info["count_comments"], 1)
        self.assertEqual(info["count_photos"], "43")
        self.assertEqual(info["count_videos"], "12")
        self.assertEqual(info["can_comment"], 1)
        self.assertEqual(info["date_create"], "1280530593")
        self.assertEqual(info["date_update"], "1308091378")
        # Title and description simplified by clean_content to strings
        self.assertEqual(info["title"], "Mah Kittehs")
        self.assertIn("Born on the 3rd of May", info["description"])
        # Owner is converted to Person
        self.assertIsInstance(info["owner"], f.Person)
        self.assertEqual(info["owner"].id, "34427469121@N01")

    @patch.object(method_call.requests, "post")
    def test_person_get_photosets(self, mock_post):
        """Test Person.getPhotosets (flickr.photosets.getList)"""
        api_doc = load_api_doc("flickr.photosets.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        person = f.Person(id="34427469121@N01")
        photosets = person.getPhotosets()

        # Verify we got 2 photosets
        self.assertEqual(len(photosets), 2)

        # First photoset
        ps1 = photosets[0]
        self.assertIsInstance(ps1, f.Photoset)
        self.assertEqual(ps1.id, "72157626216528324")
        self.assertEqual(ps1.primary, "5504567858")
        self.assertEqual(ps1.secret, "017804c585")
        self.assertEqual(ps1.server, "5174")
        self.assertEqual(ps1.farm, "6")
        self.assertEqual(ps1.photos, 22)
        self.assertEqual(ps1.videos, 0)
        self.assertEqual(ps1.count_views, "137")
        self.assertEqual(ps1.count_comments, 0)
        self.assertEqual(ps1.can_comment, 1)
        self.assertEqual(ps1.date_create, "1299514498")
        self.assertEqual(ps1.date_update, "1300335009")
        # Title/description simplified by clean_content to strings
        self.assertEqual(ps1.title, "Avis Blanche")
        self.assertEqual(ps1.description, "My Grandma's Recipe File.")

        # Second photoset
        ps2 = photosets[1]
        self.assertEqual(ps2.id, "72157624618609504")
        self.assertEqual(ps2.title, "Mah Kittehs")

        # Verify pagination info
        self.assertEqual(photosets.info.page, 1)
        self.assertEqual(photosets.info.pages, 1)
        self.assertEqual(photosets.info.perpage, 30)
        self.assertEqual(photosets.info.total, 2)

    @patch.object(method_call.requests, "post")
    def test_photoset_get_photos(self, mock_post):
        """Test Photoset.getPhotos (flickr.photosets.getPhotos)"""
        api_doc = load_api_doc("flickr.photosets.getPhotos")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photoset = f.Photoset(id="4")
        photos = photoset.getPhotos()

        # Verify we got 2 photos
        self.assertEqual(len(photos), 2)

        # First photo
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2484")
        self.assertEqual(p1.secret, "123456")
        # Server "1" gets converted to int by xml_to_flickr_json (0/1 conversion)
        self.assertEqual(p1.server, 1)
        self.assertEqual(p1.title, "my photo")
        self.assertEqual(p1.isprimary, 0)

        # Second photo (is primary)
        p2 = photos[1]
        self.assertEqual(p2.id, "2483")
        self.assertEqual(p2.title, "flickr rocks")
        self.assertEqual(p2.isprimary, 1)

        # Verify pagination info
        self.assertEqual(photos.info.page, 1)
        self.assertEqual(photos.info.pages, 1)
        self.assertEqual(photos.info.perpage, 500)
        self.assertEqual(photos.info.total, 2)

    @patch.object(method_call.requests, "post")
    def test_photoset_order_sets(self, mock_post):
        """Test Photoset.orderSets (flickr.photosets.orderSets)"""
        # Empty response for orderSets operation
        mock_post.return_value = self._mock_response({})

        result = f.Photoset.orderSets(
            photoset_ids=["72157594042012345", "72157594042012346"]
        )

        # OrderSets operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_order_sets_with_objects(self, mock_post):
        """Test Photoset.orderSets with Photoset objects"""
        mock_post.return_value = self._mock_response({})

        ps1 = f.Photoset(id="72157594042012345")
        ps2 = f.Photoset(id="72157594042012346")
        result = f.Photoset.orderSets(photosets=[ps1, ps2])

        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_remove_photo(self, mock_post):
        """Test Photoset.removePhoto (flickr.photosets.removePhoto)"""
        # Empty response for removePhoto operation
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        result = photoset.removePhoto(photo_id="12345")

        # RemovePhoto operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_remove_photo_with_object(self, mock_post):
        """Test Photoset.removePhoto with Photo object"""
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        photo = f.Photo(id="12345")
        result = photoset.removePhoto(photo=photo)

        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_remove_photos(self, mock_post):
        """Test Photoset.removePhotos (flickr.photosets.removePhotos)"""
        # Empty response for removePhotos operation
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        result = photoset.removePhotos(photo_ids=["12345", "67890"])

        # RemovePhotos operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_reorder_photos(self, mock_post):
        """Test Photoset.reorderPhotos (flickr.photosets.reorderPhotos)"""
        # Empty response for reorderPhotos operation
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        result = photoset.reorderPhotos(photo_ids=["12345", "67890", "11111"])

        # ReorderPhotos operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_set_primary_photo(self, mock_post):
        """Test Photoset.setPrimaryPhoto (flickr.photosets.setPrimaryPhoto)"""
        # Empty response for setPrimaryPhoto operation
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        result = photoset.setPrimaryPhoto(photo_id="12345")

        # SetPrimaryPhoto operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photoset_set_primary_photo_with_object(self, mock_post):
        """Test Photoset.setPrimaryPhoto with Photo object"""
        mock_post.return_value = self._mock_response({})

        photoset = f.Photoset(id="72157594042012345")
        photo = f.Photo(id="12345")
        result = photoset.setPrimaryPhoto(photo=photo)

        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
