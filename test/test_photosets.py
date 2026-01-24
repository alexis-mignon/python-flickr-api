"""
Tests for Photoset API methods.

Batch 17:
flickr.photosets.addPhoto, flickr.photosets.comments.addComment,
flickr.photosets.comments.deleteComment, flickr.photosets.comments.editComment,
flickr.photosets.comments.getList, flickr.photosets.create, flickr.photosets.delete,
flickr.photosets.editMeta, flickr.photosets.editPhotos, flickr.photosets.getContext

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


class TestPhotosetMethods(unittest.TestCase):
    """Tests for Photoset API methods"""

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


if __name__ == "__main__":
    unittest.main()
