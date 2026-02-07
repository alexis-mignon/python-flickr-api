"""Tests for shared retry logic in retry module."""

import unittest
from io import BytesIO
from unittest.mock import MagicMock, patch

import requests
from requests import Response
from requests.exceptions import ConnectionError, ReadTimeout

import flickr_api as f
from flickr_api import method_call
from flickr_api import retry as retry_module
from flickr_api.auth import AuthHandler
from flickr_api.flickrerrors import (
    FlickrRateLimitError,
    FlickrServerError,
    FlickrTimeoutError,
)


class TestRetryOnTimeout(unittest.TestCase):
    """Tests for retry on timeout exceptions."""

    def setUp(self):
        """Set up test fixtures."""
        auth_handler = AuthHandler(
            key="test",
            secret="test",
            access_token_key="test",
            access_token_secret="test",
        )
        f.set_auth_handler(auth_handler)
        self.original_config = method_call.get_retry_config()
        method_call.set_retry_config(max_retries=2, base_delay=0.01, max_delay=0.1)

    def tearDown(self):
        """Restore original config values."""
        method_call.set_retry_config(
            max_retries=self.original_config["max_retries"],
            base_delay=self.original_config["base_delay"],
            max_delay=self.original_config["max_delay"],
        )

    def _create_ok_response(self):
        """Create a mock successful response."""
        resp = Response()
        resp.status_code = 200
        resp._content = b'{"stat": "ok", "user": {"id": "123", "username": {"_content": "testuser"}}}'
        return resp

    @patch.object(method_call.requests, "post")
    @patch.object(retry_module.time, "sleep")
    def test_retries_on_read_timeout(self, mock_sleep, mock_post):
        """Retries on ReadTimeout and succeeds."""
        # First two calls timeout, third succeeds
        mock_post.side_effect = [
            ReadTimeout("Read timed out"),
            ReadTimeout("Read timed out"),
            self._create_ok_response(),
        ]

        # Should not raise - succeeds on third attempt
        f.Person.findByUserName("testuser")

        self.assertEqual(3, mock_post.call_count)
        self.assertEqual(2, mock_sleep.call_count)

    @patch.object(method_call.requests, "post")
    @patch.object(retry_module.time, "sleep")
    def test_raises_timeout_error_after_max_retries(self, mock_sleep, mock_post):
        """Raises FlickrTimeoutError after max retries exhausted."""
        mock_post.side_effect = ReadTimeout("Read timed out")

        with self.assertRaises(FlickrTimeoutError) as context:
            f.Person.findByUserName("testuser")

        self.assertIn("Read timed out", str(context.exception))
        # Initial attempt + 2 retries = 3 calls
        self.assertEqual(3, mock_post.call_count)


class TestRetryOnConnectionError(unittest.TestCase):
    """Tests for retry on connection errors."""

    def setUp(self):
        """Set up test fixtures."""
        auth_handler = AuthHandler(
            key="test",
            secret="test",
            access_token_key="test",
            access_token_secret="test",
        )
        f.set_auth_handler(auth_handler)
        self.original_config = method_call.get_retry_config()
        method_call.set_retry_config(max_retries=2, base_delay=0.01, max_delay=0.1)

    def tearDown(self):
        """Restore original config values."""
        method_call.set_retry_config(
            max_retries=self.original_config["max_retries"],
            base_delay=self.original_config["base_delay"],
            max_delay=self.original_config["max_delay"],
        )

    def _create_ok_response(self):
        """Create a mock successful response."""
        resp = Response()
        resp.status_code = 200
        resp._content = b'{"stat": "ok", "user": {"id": "123", "username": {"_content": "testuser"}}}'
        return resp

    @patch.object(method_call.requests, "post")
    @patch.object(retry_module.time, "sleep")
    def test_retries_on_connection_error(self, mock_sleep, mock_post):
        """Retries on ConnectionError and succeeds."""
        # First call fails with connection error, second succeeds
        mock_post.side_effect = [
            ConnectionError("Connection refused"),
            self._create_ok_response(),
        ]

        # Should not raise
        f.Person.findByUserName("testuser")

        self.assertEqual(2, mock_post.call_count)
        self.assertEqual(1, mock_sleep.call_count)

    @patch.object(method_call.requests, "post")
    @patch.object(retry_module.time, "sleep")
    def test_raises_timeout_error_on_connection_exhausted(self, mock_sleep, mock_post):
        """Raises FlickrTimeoutError after connection retries exhausted."""
        mock_post.side_effect = ConnectionError("Connection refused")

        with self.assertRaises(FlickrTimeoutError) as context:
            f.Person.findByUserName("testuser")

        self.assertIn("Connection error", str(context.exception))


class TestRetryOnServerError(unittest.TestCase):
    """Tests for retry on HTTP 5xx server errors."""

    def setUp(self):
        """Set up test fixtures."""
        auth_handler = AuthHandler(
            key="test",
            secret="test",
            access_token_key="test",
            access_token_secret="test",
        )
        f.set_auth_handler(auth_handler)
        self.original_config = method_call.get_retry_config()
        method_call.set_retry_config(max_retries=2, base_delay=0.01, max_delay=0.1)

    def tearDown(self):
        """Restore original config values."""
        method_call.set_retry_config(
            max_retries=self.original_config["max_retries"],
            base_delay=self.original_config["base_delay"],
            max_delay=self.original_config["max_delay"],
        )

    def _create_ok_response(self):
        """Create a mock successful response."""
        resp = Response()
        resp.status_code = 200
        resp._content = b'{"stat": "ok", "user": {"id": "123", "username": {"_content": "testuser"}}}'
        return resp

    def _create_5xx_response(self, status_code=500):
        """Create a mock 5xx response."""
        resp = Response()
        resp.status_code = status_code
        resp._content = b"Internal Server Error"
        return resp

    @patch.object(method_call.requests, "post")
    @patch.object(retry_module.time, "sleep")
    def test_retries_on_500_error(self, mock_sleep, mock_post):
        """Retries on HTTP 500 and succeeds."""
        mock_post.side_effect = [
            self._create_5xx_response(500),
            self._create_ok_response(),
        ]

        f.Person.findByUserName("testuser")

        self.assertEqual(2, mock_post.call_count)
        self.assertEqual(1, mock_sleep.call_count)

    @patch.object(method_call.requests, "post")
    @patch.object(retry_module.time, "sleep")
    def test_retries_on_502_error(self, mock_sleep, mock_post):
        """Retries on HTTP 502 Bad Gateway."""
        mock_post.side_effect = [
            self._create_5xx_response(502),
            self._create_ok_response(),
        ]

        f.Person.findByUserName("testuser")
        self.assertEqual(2, mock_post.call_count)

    @patch.object(method_call.requests, "post")
    @patch.object(retry_module.time, "sleep")
    def test_retries_on_503_error(self, mock_sleep, mock_post):
        """Retries on HTTP 503 Service Unavailable."""
        mock_post.side_effect = [
            self._create_5xx_response(503),
            self._create_ok_response(),
        ]

        f.Person.findByUserName("testuser")
        self.assertEqual(2, mock_post.call_count)

    @patch.object(method_call.requests, "post")
    @patch.object(retry_module.time, "sleep")
    def test_raises_server_error_after_max_retries(self, mock_sleep, mock_post):
        """Raises FlickrServerError after max retries exhausted."""
        mock_post.return_value = self._create_5xx_response(500)

        with self.assertRaises(FlickrServerError) as context:
            f.Person.findByUserName("testuser")

        self.assertEqual(500, context.exception.status_code)


class TestUploadRetry(unittest.TestCase):
    """Tests for upload retry behavior."""

    def setUp(self):
        """Set up test fixtures."""
        auth_handler = AuthHandler(
            key="test",
            secret="test",
            access_token_key="test",
            access_token_secret="test",
        )
        f.set_auth_handler(auth_handler)
        self.original_config = method_call.get_retry_config()
        method_call.set_retry_config(max_retries=2, base_delay=0.01, max_delay=0.1)

    def tearDown(self):
        """Restore original config values."""
        method_call.set_retry_config(
            max_retries=self.original_config["max_retries"],
            base_delay=self.original_config["base_delay"],
            max_delay=self.original_config["max_delay"],
        )

    def _create_ok_upload_response(self):
        """Create a mock successful upload response."""
        resp = Response()
        resp.status_code = 200
        resp._content = b'<?xml version="1.0" encoding="utf-8" ?><rsp stat="ok"><photoid>12345</photoid></rsp>'
        return resp

    @patch("flickr_api.upload.requests.post")
    @patch.object(retry_module.time, "sleep")
    def test_upload_retries_on_timeout(self, mock_sleep, mock_post):
        """Upload retries on ReadTimeout."""
        from flickr_api import upload
        from io import StringIO

        mock_post.side_effect = [
            ReadTimeout("Read timed out"),
            self._create_ok_upload_response(),
        ]

        result = upload(photo_file="/tmp/test.jpg", photo_file_data=StringIO("test"))

        self.assertEqual(2, mock_post.call_count)
        self.assertEqual("12345", result.id)

    @patch("flickr_api.upload.requests.post")
    @patch.object(retry_module.time, "sleep")
    def test_upload_raises_timeout_error_after_max_retries(self, mock_sleep, mock_post):
        """Upload raises FlickrTimeoutError after max retries."""
        from flickr_api import upload
        from io import StringIO

        mock_post.side_effect = ReadTimeout("Read timed out")

        with self.assertRaises(FlickrTimeoutError):
            upload(photo_file="/tmp/test.jpg", photo_file_data=StringIO("test"))


class TestFlickrTimeoutError(unittest.TestCase):
    """Tests for FlickrTimeoutError exception."""

    def test_error_message(self):
        """Error message is properly formatted."""
        error = FlickrTimeoutError("Read timed out after 10 seconds")
        self.assertEqual("Read timed out after 10 seconds", error.message)
        self.assertIn("Request failed", str(error))
        self.assertIn("Read timed out", str(error))


if __name__ == "__main__":
    unittest.main()
