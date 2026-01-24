"""
Tests for Photo.Comment API methods.

Batch 12:
flickr.photos.comments.addComment, flickr.photos.comments.deleteComment,
flickr.photos.comments.editComment, flickr.photos.comments.getList,
flickr.photos.comments.getRecentForContacts

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPhotoCommentMethods(FlickrApiTestCase):
    """Tests for Photo.Comment-related API methods"""

    @patch.object(method_call.requests, "post")
    def test_photo_add_comment(self, mock_post):
        """Test Photo.addComment (flickr.photos.comments.addComment)"""
        api_doc = load_api_doc("flickr.photos.comments.addComment")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="109722179")
        comment = photo.addComment(comment_text="Test comment")

        # Verify comment object is returned
        self.assertIsInstance(comment, f.Photo.Comment)
        self.assertEqual(comment.id, "97777-72057594037941949-72057594037942602")
        # The photo reference is set on the comment
        self.assertEqual(comment.photo, photo)

    @patch.object(method_call.requests, "post")
    def test_photo_comment_delete(self, mock_post):
        """Test Photo.Comment.delete (flickr.photos.comments.deleteComment)"""
        # Empty response for delete operation
        mock_post.return_value = self._mock_response({})

        comment = f.Photo.Comment(id="97777-72057594037941949-72057594037942602")
        result = comment.delete()

        # Delete operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_comment_edit(self, mock_post):
        """Test Photo.Comment.edit (flickr.photos.comments.editComment)"""
        # Empty response for edit operation
        mock_post.return_value = self._mock_response({})

        comment = f.Photo.Comment(id="97777-72057594037941949-72057594037942602")
        result = comment.edit(comment_text="Updated comment text")

        # Edit operation returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_get_comments(self, mock_post):
        """Test Photo.getComments (flickr.photos.comments.getList)"""
        api_doc = load_api_doc("flickr.photos.comments.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="109722179")
        comments = photo.getComments()

        # Verify we got 1 comment
        self.assertEqual(len(comments), 1)

        # Verify comment details
        c1 = comments[0]
        self.assertIsInstance(c1, f.Photo.Comment)
        self.assertEqual(c1.id, "6065-109722179-72057594077818641")
        self.assertEqual(c1.datecreate, "1141841470")
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

        # Verify photo reference is set
        self.assertEqual(c1.photo, photo)

    @patch.object(method_call.requests, "post")
    def test_photo_get_comments_empty(self, mock_post):
        """Test Photo.getComments with no comments"""
        # Response with no comments
        json_response = {
            "comments": {
                "photo_id": "109722179"
            }
        }

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="109722179")
        comments = photo.getComments()

        # Verify empty list returned
        self.assertEqual(len(comments), 0)

    @patch.object(method_call.requests, "post")
    def test_photo_comment_get_recent_for_contacts(self, mock_post):
        """Test Photo.Comment.getRecentForContacts
        (flickr.photos.comments.getRecentForContacts)"""
        api_doc = load_api_doc("flickr.photos.comments.getRecentForContacts")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photos = f.Photo.Comment.getRecentForContacts()

        # Verify we got 4 photos
        self.assertEqual(len(photos), 4)

        # First photo - public
        p1 = photos[0]
        self.assertIsInstance(p1, f.Photo)
        self.assertEqual(p1.id, "2636")
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
        self.assertEqual(p2.owner.id, "47058503995@N01")
        self.assertEqual(p2.title, "test_03")
        self.assertFalse(p2.ispublic)
        self.assertTrue(p2.isfriend)
        self.assertTrue(p2.isfamily)

        # Third photo
        p3 = photos[2]
        self.assertEqual(p3.id, "2633")
        self.assertEqual(p3.title, "test_01")

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


if __name__ == "__main__":
    unittest.main()
