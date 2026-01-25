"""Tests for rate limit handling in method_call module."""

import unittest
from io import BytesIO
from unittest.mock import MagicMock, patch

from requests import Response

import flickr_api as f
from flickr_api import method_call
from flickr_api.auth import AuthHandler
from flickr_api.flickrerrors import FlickrRateLimitError


class TestRateLimitConfig(unittest.TestCase):
    """Tests for rate limit configuration functions."""

    def setUp(self):
        """Save original config values."""
        self.original_config = method_call.get_retry_config()

    def tearDown(self):
        """Restore original config values."""
        method_call.set_retry_config(
            max_retries=self.original_config["max_retries"],
            base_delay=self.original_config["base_delay"],
            max_delay=self.original_config["max_delay"],
        )

    def test_get_retry_config_returns_defaults(self):
        """get_retry_config returns default values."""
        config = method_call.get_retry_config()
        self.assertIn("max_retries", config)
        self.assertIn("base_delay", config)
        self.assertIn("max_delay", config)
        self.assertEqual(3, config["max_retries"])
        self.assertEqual(1.0, config["base_delay"])
        self.assertEqual(60.0, config["max_delay"])

    def test_set_retry_config_updates_values(self):
        """set_retry_config updates configuration."""
        method_call.set_retry_config(max_retries=5, base_delay=2.0, max_delay=120.0)
        config = method_call.get_retry_config()
        self.assertEqual(5, config["max_retries"])
        self.assertEqual(2.0, config["base_delay"])
        self.assertEqual(120.0, config["max_delay"])

    def test_set_retry_config_partial_update(self):
        """set_retry_config can update individual values."""
        method_call.set_retry_config(max_retries=10)
        config = method_call.get_retry_config()
        self.assertEqual(10, config["max_retries"])
        # Other values unchanged
        self.assertEqual(1.0, config["base_delay"])
        self.assertEqual(60.0, config["max_delay"])


class TestCalculateRetryDelay(unittest.TestCase):
    """Tests for _calculate_retry_delay function."""

    def setUp(self):
        """Save and set known config values."""
        self.original_config = method_call.get_retry_config()
        method_call.set_retry_config(base_delay=1.0, max_delay=60.0)

    def tearDown(self):
        """Restore original config values."""
        method_call.set_retry_config(
            max_retries=self.original_config["max_retries"],
            base_delay=self.original_config["base_delay"],
            max_delay=self.original_config["max_delay"],
        )

    def test_uses_retry_after_when_provided(self):
        """Uses Retry-After value when available."""
        delay = method_call._calculate_retry_delay(attempt=0, retry_after=10.0)
        self.assertEqual(10.0, delay)

    def test_caps_retry_after_at_max_delay(self):
        """Caps Retry-After at max_delay."""
        delay = method_call._calculate_retry_delay(attempt=0, retry_after=120.0)
        self.assertEqual(60.0, delay)  # max_delay

    def test_exponential_backoff_without_retry_after(self):
        """Uses exponential backoff when Retry-After not provided."""
        # attempt 0: 1 * 2^0 = 1
        delay = method_call._calculate_retry_delay(attempt=0, retry_after=None)
        self.assertEqual(1.0, delay)

        # attempt 1: 1 * 2^1 = 2
        delay = method_call._calculate_retry_delay(attempt=1, retry_after=None)
        self.assertEqual(2.0, delay)

        # attempt 2: 1 * 2^2 = 4
        delay = method_call._calculate_retry_delay(attempt=2, retry_after=None)
        self.assertEqual(4.0, delay)

    def test_exponential_backoff_capped_at_max_delay(self):
        """Exponential backoff is capped at max_delay."""
        # attempt 10: 1 * 2^10 = 1024, but capped at 60
        delay = method_call._calculate_retry_delay(attempt=10, retry_after=None)
        self.assertEqual(60.0, delay)


class TestParseRetryAfter(unittest.TestCase):
    """Tests for _parse_retry_after function."""

    def test_parses_numeric_value(self):
        """Parses numeric Retry-After header."""
        resp = Response()
        resp.headers["Retry-After"] = "30"
        result = method_call._parse_retry_after(resp)
        self.assertEqual(30.0, result)

    def test_parses_float_value(self):
        """Parses float Retry-After header."""
        resp = Response()
        resp.headers["Retry-After"] = "30.5"
        result = method_call._parse_retry_after(resp)
        self.assertEqual(30.5, result)

    def test_returns_none_when_header_missing(self):
        """Returns None when Retry-After header is missing."""
        resp = Response()
        result = method_call._parse_retry_after(resp)
        self.assertIsNone(result)

    def test_returns_none_for_invalid_value(self):
        """Returns None for non-numeric Retry-After header."""
        resp = Response()
        resp.headers["Retry-After"] = "invalid"
        result = method_call._parse_retry_after(resp)
        self.assertIsNone(result)


class TestRateLimitHandling(unittest.TestCase):
    """Tests for rate limit handling in call_api."""

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
        # Disable retries for most tests
        method_call.set_retry_config(max_retries=0)

    def tearDown(self):
        """Restore original config values."""
        method_call.set_retry_config(
            max_retries=self.original_config["max_retries"],
            base_delay=self.original_config["base_delay"],
            max_delay=self.original_config["max_delay"],
        )

    def _create_429_response(self, retry_after=None, content="Too Many Requests"):
        """Create a mock 429 response."""
        resp = Response()
        resp.status_code = 429
        resp.raw = BytesIO(content.encode("utf-8"))
        resp._content = content.encode("utf-8")
        if retry_after:
            resp.headers["Retry-After"] = str(retry_after)
        return resp

    def _create_ok_response(self):
        """Create a mock successful response."""
        resp = Response()
        resp.status_code = 200
        resp._content = b'{"stat": "ok", "user": {"id": "123", "username": {"_content": "testuser"}}}'
        return resp

    @patch.object(method_call.requests, "post")
    def test_raises_rate_limit_error_on_429(self, mock_post):
        """Raises FlickrRateLimitError on 429 response."""
        mock_post.return_value = self._create_429_response()

        with self.assertRaises(FlickrRateLimitError) as context:
            f.Person.findByUserName("testuser")

        self.assertIn("Rate limit exceeded", str(context.exception))

    @patch.object(method_call.requests, "post")
    def test_rate_limit_error_includes_retry_after(self, mock_post):
        """FlickrRateLimitError includes Retry-After value."""
        mock_post.return_value = self._create_429_response(retry_after=30)

        with self.assertRaises(FlickrRateLimitError) as context:
            f.Person.findByUserName("testuser")

        self.assertEqual(30.0, context.exception.retry_after)
        self.assertIn("30", str(context.exception))

    @patch.object(method_call.requests, "post")
    @patch.object(method_call.time, "sleep")
    def test_retries_on_429_with_retries_enabled(self, mock_sleep, mock_post):
        """Retries on 429 when retries are enabled."""
        method_call.set_retry_config(max_retries=2, base_delay=1.0)

        # First two calls return 429, third succeeds
        mock_post.side_effect = [
            self._create_429_response(retry_after=1),
            self._create_429_response(retry_after=1),
            self._create_ok_response(),
        ]

        # Should not raise - succeeds on third attempt
        f.Person.findByUserName("testuser")

        self.assertEqual(3, mock_post.call_count)
        self.assertEqual(2, mock_sleep.call_count)

    @patch.object(method_call.requests, "post")
    @patch.object(method_call.time, "sleep")
    def test_raises_after_max_retries_exceeded(self, mock_sleep, mock_post):
        """Raises FlickrRateLimitError after max retries exceeded."""
        method_call.set_retry_config(max_retries=2, base_delay=1.0)

        # All calls return 429
        mock_post.return_value = self._create_429_response(retry_after=1)

        with self.assertRaises(FlickrRateLimitError):
            f.Person.findByUserName("testuser")

        # Initial attempt + 2 retries = 3 calls
        self.assertEqual(3, mock_post.call_count)
        # 2 sleeps (after first and second failures)
        self.assertEqual(2, mock_sleep.call_count)


class TestFlickrRateLimitError(unittest.TestCase):
    """Tests for FlickrRateLimitError exception."""

    def test_error_with_retry_after(self):
        """Error message includes retry_after when provided."""
        error = FlickrRateLimitError(retry_after=30.0, content="Rate limited")
        self.assertEqual(30.0, error.retry_after)
        self.assertEqual("Rate limited", error.content)
        self.assertIn("30", str(error))
        self.assertIn("Rate limit exceeded", str(error))

    def test_error_without_retry_after(self):
        """Error message works without retry_after."""
        error = FlickrRateLimitError(retry_after=None, content="Rate limited")
        self.assertIsNone(error.retry_after)
        self.assertEqual("Rate limited", error.content)
        self.assertIn("Rate limit exceeded", str(error))
