"""
Tests for Group discussion API methods.

flickr.groups.discuss.replies.add, delete, edit, getInfo, getList
flickr.groups.discuss.topics.add, getInfo, getList
Uses example responses from the api-docs/ directory.
"""
import unittest
from unittest.mock import patch

import flickr_api as f
from flickr_api import method_call

from base_test import FlickrApiTestCase
from test_utils import xml_to_flickr_json, load_api_doc


class TestGroupDiscussMethods(FlickrApiTestCase):
    """Tests for Group discussion-related API methods"""

    # Topic methods

    @patch.object(method_call.requests, "post")
    def test_group_add_discuss_topic(self, mock_post):
        """Test Group.addDiscussTopic (flickr.groups.discuss.topics.add)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="46744914@N00")
        result = group.addDiscussTopic(
            subject="Test Topic",
            message="This is a test message"
        )

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_topic_get_info(self, mock_post):
        """Test Group.Topic.getInfo (flickr.groups.discuss.topics.getInfo)"""
        api_doc = load_api_doc("flickr.groups.discuss.topics.getInfo")
        # Response is wrapped in <wrapper> tags, extract inner content
        response_xml = api_doc["response"]
        # Remove wrapper tags
        inner_xml = response_xml.replace("<wrapper>", "").replace("</wrapper>", "")
        json_response = xml_to_flickr_json(inner_xml)

        mock_post.return_value = self._mock_response(json_response)

        group = f.Group(id="46744914@N00")
        topic = f.Group.Topic(id="72157607082559966", group=group)
        info = topic.getInfo()

        # Returns formatted topic dict
        self.assertEqual(info["id"], "72157607082559966")
        self.assertEqual(info["subject"], "Who's still around?")
        self.assertEqual(info["count_replies"], 1)
        self.assertEqual(info["is_sticky"], 0)
        self.assertEqual(info["is_locked"], 0)
        self.assertEqual(info["message"], "Is anyone still around in this group?")

        # Author should be a Person object
        self.assertIsInstance(info["author"], f.Person)
        self.assertEqual(info["author"].id, "30134652@N05")
        self.assertEqual(info["author"].role, "admin")
        self.assertFalse(info["author"].is_pro)

    @patch.object(method_call.requests, "post")
    def test_group_get_discuss_topics(self, mock_post):
        """Test Group.getDiscussTopics (flickr.groups.discuss.topics.getList)"""
        api_doc = load_api_doc("flickr.groups.discuss.topics.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        group = f.Group(id="46744914@N00")
        topics = group.getDiscussTopics()

        # Verify we got 2 topics
        self.assertEqual(len(topics), 2)

        # First topic
        t1 = topics[0]
        self.assertIsInstance(t1, f.Group.Topic)
        self.assertEqual(t1.id, "72157625038324579")
        self.assertEqual(t1.subject, "A long time ago in a galaxy far, far away...")
        self.assertEqual(t1.count_replies, "8")

        # Author should be a Person
        self.assertIsInstance(t1.author, f.Person)
        self.assertEqual(t1.author.id, "53930889@N04")
        self.assertEqual(t1.author.role, "member")

        # Second topic
        t2 = topics[1]
        self.assertEqual(t2.id, "72157629635119774")
        self.assertEqual(t2.subject, "Where The Fish Are")

        # Verify pagination info
        self.assertEqual(topics.info.total, 4621)
        self.assertEqual(topics.info.page, 1)
        self.assertEqual(topics.info.pages, 2310)

    # Reply methods

    @patch.object(method_call.requests, "post")
    def test_topic_add_reply(self, mock_post):
        """Test Group.Topic.addReply (flickr.groups.discuss.replies.add)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="46744914@N00")
        topic = f.Group.Topic(id="72157625038324579", group=group)
        result = topic.addReply(message="This is a test reply")

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_reply_get_info(self, mock_post):
        """Test Group.Topic.Reply.getInfo (flickr.groups.discuss.replies.getInfo)"""
        api_doc = load_api_doc("flickr.groups.discuss.replies.getInfo")
        # Response is wrapped in <wrapper> tags
        response_xml = api_doc["response"]
        inner_xml = response_xml.replace("<wrapper>", "").replace("</wrapper>", "")
        json_response = xml_to_flickr_json(inner_xml)

        mock_post.return_value = self._mock_response(json_response)

        group = f.Group(id="46744914@N00")
        topic = f.Group.Topic(id="72157607082559966", group=group)
        reply = f.Group.Topic.Reply(id="72157607082559968", topic=topic)
        info = reply.getInfo()

        # Returns formatted reply dict
        self.assertEqual(info["id"], "72157607082559968")
        self.assertEqual(info["authorname"], "JAMAL'S ACCOUNT")
        self.assertEqual(info["can_edit"], 1)
        self.assertEqual(info["can_delete"], 1)
        self.assertEqual(info["message"], "...well, too bad.")

        # Author should be a Person object
        self.assertIsInstance(info["author"], f.Person)
        self.assertEqual(info["author"].id, "30134652@N05")
        self.assertEqual(info["author"].role, "admin")
        self.assertFalse(info["author"].is_pro)

    @patch.object(method_call.requests, "post")
    def test_topic_get_replies(self, mock_post):
        """Test Group.Topic.getReplies (flickr.groups.discuss.replies.getList)"""
        api_doc = load_api_doc("flickr.groups.discuss.replies.getList")
        json_response = xml_to_flickr_json(api_doc["response"])

        mock_post.return_value = self._mock_response(json_response)

        group = f.Group(id="46744914@N00")
        topic = f.Group.Topic(id="72157625038324579", group=group)
        replies = topic.getReplies()

        # Verify we got 3 replies
        self.assertEqual(len(replies), 3)

        # First reply
        r1 = replies[0]
        self.assertIsInstance(r1, f.Group.Topic.Reply)
        self.assertEqual(r1.id, "72157625163054214")
        self.assertIn("giant furry space monsters", r1.message)

        # Author should be a Person
        self.assertIsInstance(r1.author, f.Person)
        self.assertEqual(r1.author.id, "41380738@N05")
        self.assertEqual(r1.author.role, "member")

        # Second reply
        r2 = replies[1]
        self.assertEqual(r2.id, "72157625163539300")
        self.assertIn("Trekkie", r2.message)

        # Third reply
        r3 = replies[2]
        self.assertEqual(r3.id, "72157625040116805")
        self.assertIn("scale of 1 to 10", r3.message)

        # Verify pagination info
        self.assertEqual(replies.info.total, 8)
        self.assertEqual(replies.info.page, 1)
        self.assertEqual(replies.info.pages, 2)

    @patch.object(method_call.requests, "post")
    def test_reply_delete(self, mock_post):
        """Test Group.Topic.Reply.delete (flickr.groups.discuss.replies.delete)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="46744914@N00")
        topic = f.Group.Topic(id="72157625038324579", group=group)
        reply = f.Group.Topic.Reply(id="72157607082559968", topic=topic)
        result = reply.delete()

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_reply_edit(self, mock_post):
        """Test Reply.edit (flickr.groups.discuss.replies.edit)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="46744914@N00")
        topic = f.Group.Topic(id="72157625038324579", group=group)
        reply = f.Group.Topic.Reply(id="72157607082559968", topic=topic)
        result = reply.edit(message="Updated reply message")

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_topic_delete_reply(self, mock_post):
        """Test Topic.deleteReply (flickr.groups.discuss.replies.delete)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="46744914@N00")
        topic = f.Group.Topic(id="72157625038324579", group=group)
        reply = f.Group.Topic.Reply(id="72157607082559968", topic=topic)
        result = topic.deleteReply(reply=reply)

        self.assertIsNone(result)
        mock_post.assert_called_once()

    @patch.object(method_call.requests, "post")
    def test_topic_edit_reply(self, mock_post):
        """Test Topic.editReply (flickr.groups.discuss.replies.edit)"""
        # Write operation with empty response
        mock_post.return_value = self._mock_response({})

        group = f.Group(id="46744914@N00")
        topic = f.Group.Topic(id="72157625038324579", group=group)
        reply = f.Group.Topic.Reply(id="72157607082559968", topic=topic)
        result = topic.editReply(reply=reply, message="Updated message")

        self.assertIsNone(result)
        mock_post.assert_called_once()


if __name__ == "__main__":
    unittest.main()
