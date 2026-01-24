"""
Tests for Photo.Note API methods.

Batch 14:
flickr.photos.notes.add
flickr.photos.notes.delete
flickr.photos.notes.edit

Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestPhotoNoteMethods(FlickrApiTestCase):
    """Tests for Photo.Note API methods"""

    @patch.object(method_call.requests, "post")
    def test_photo_add_note(self, mock_post):
        """Test Photo.addNote (flickr.photos.notes.add)"""
        api_doc = load_api_doc("flickr.photos.notes.add")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        photo = f.Photo(id="12345678")
        note = photo.addNote(
            note_x=100, note_y=100, note_w=50, note_h=50,
            note_text="Test note"
        )

        # Verify we got a Note object back
        self.assertIsInstance(note, f.Photo.Note)
        self.assertEqual(note.id, "1234")
        self.assertEqual(note.photo, photo)

    @patch.object(method_call.requests, "post")
    def test_photo_note_delete(self, mock_post):
        """Test Photo.Note.delete (flickr.photos.notes.delete)"""
        # Empty response for delete operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345678")
        note = f.Photo.Note(id="1234", photo=photo)
        result = note.delete()

        # Delete returns None
        self.assertIsNone(result)

    @patch.object(method_call.requests, "post")
    def test_photo_note_edit(self, mock_post):
        """Test Photo.Note.edit (flickr.photos.notes.edit)"""
        # Empty response for edit operation
        mock_post.return_value = self._mock_response({})

        photo = f.Photo(id="12345678")
        note = f.Photo.Note(id="1234", photo=photo)
        result = note.edit(
            note_x=150, note_y=150, note_w=75, note_h=75,
            note_text="Updated note"
        )

        # Edit returns None
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
