"""Tests for proactive rate limiting (throttling) in method_call module."""

import unittest
from unittest.mock import patch

from flickr_api import method_call


class TestRateLimitDisabledByDefault(unittest.TestCase):
    """Test that rate limiting is disabled by default."""

    def setUp(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)

    def tearDown(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)

    def test_rate_limit_disabled_by_default(self):
        """Rate limiting should be disabled by default."""
        result = method_call.get_rate_limit()
        self.assertIsNone(result["requests_per_hour"])


class TestSetAndGetRateLimit(unittest.TestCase):
    """Test setting and getting rate limit configuration."""

    def setUp(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)

    def tearDown(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)

    def test_set_and_get_rate_limit(self):
        """Can set and get rate limit value."""
        method_call.set_rate_limit(3600.0)
        result = method_call.get_rate_limit()
        self.assertEqual(3600.0, result["requests_per_hour"])

    def test_disable_rate_limit(self):
        """Can disable rate limiting by setting to None."""
        method_call.set_rate_limit(3600.0)
        method_call.set_rate_limit(None)
        result = method_call.get_rate_limit()
        self.assertIsNone(result["requests_per_hour"])

    def test_reject_zero_rate_limit(self):
        """Zero rate limit should raise ValueError."""
        with self.assertRaises(ValueError) as ctx:
            method_call.set_rate_limit(0.0)
        self.assertEqual(str(ctx.exception), "requests_per_hour must be positive")

    def test_reject_negative_rate_limit(self):
        """Negative rate limit should raise ValueError."""
        with self.assertRaises(ValueError) as ctx:
            method_call.set_rate_limit(-100.0)
        self.assertEqual(str(ctx.exception), "requests_per_hour must be positive")


class TestIntervalCalculation(unittest.TestCase):
    """Test interval calculation for rate limiting."""

    def setUp(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)

    def tearDown(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)

    def test_interval_calculation_3600_per_hour(self):
        """3600 requests/hour = 1.0 second interval."""
        method_call.set_rate_limit(3600.0)
        status = method_call.get_rate_limit_status()
        self.assertEqual(1.0, status["interval_seconds"])

    def test_interval_calculation_1800_per_hour(self):
        """1800 requests/hour = 2.0 second interval."""
        method_call.set_rate_limit(1800.0)
        status = method_call.get_rate_limit_status()
        self.assertEqual(2.0, status["interval_seconds"])

    def test_interval_calculation_7200_per_hour(self):
        """7200 requests/hour = 0.5 second interval."""
        method_call.set_rate_limit(7200.0)
        status = method_call.get_rate_limit_status()
        self.assertEqual(0.5, status["interval_seconds"])


class TestGetRateLimitStatus(unittest.TestCase):
    """Test get_rate_limit_status function."""

    def setUp(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    def tearDown(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    def test_get_rate_limit_status_disabled(self):
        """Status shows disabled state correctly."""
        status = method_call.get_rate_limit_status()
        self.assertFalse(status["enabled"])
        self.assertIsNone(status["requests_per_hour"])
        self.assertEqual(0.0, status["interval_seconds"])
        self.assertIsNone(status["last_request_time"])

    def test_get_rate_limit_status_enabled(self):
        """Status shows enabled state correctly."""
        method_call.set_rate_limit(3600.0)
        status = method_call.get_rate_limit_status()
        self.assertTrue(status["enabled"])
        self.assertEqual(3600.0, status["requests_per_hour"])
        self.assertEqual(1.0, status["interval_seconds"])
        self.assertIsNone(status["last_request_time"])

    def test_get_rate_limit_status_with_last_request(self):
        """Status includes last request time when set."""
        method_call.set_rate_limit(3600.0)
        method_call._RATE_LIMIT_LAST_REQUEST = 1000.0
        status = method_call.get_rate_limit_status()
        self.assertEqual(1000.0, status["last_request_time"])


class TestNoSleepWhenDisabled(unittest.TestCase):
    """Test that no sleep occurs when rate limiting is disabled."""

    def setUp(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    def tearDown(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    @patch.object(method_call.time, "sleep")
    @patch.object(method_call.time, "time", return_value=1000.0)
    def test_no_sleep_when_disabled(self, mock_time, mock_sleep):
        """No sleep when rate limiting is disabled."""
        method_call._maybe_wait_for_rate_limit()
        mock_sleep.assert_not_called()


class TestSleepsWhenIntervalNotElapsed(unittest.TestCase):
    """Test that sleep occurs when interval hasn't elapsed."""

    def setUp(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    def tearDown(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    @patch.object(method_call.time, "sleep")
    @patch.object(method_call.time, "time", return_value=1000.5)
    def test_sleeps_when_interval_not_elapsed(self, mock_time, mock_sleep):
        """Sleep for remaining time when interval hasn't elapsed."""
        method_call.set_rate_limit(3600.0)  # 1 second interval
        method_call._RATE_LIMIT_LAST_REQUEST = 1000.0  # 0.5 seconds ago

        method_call._maybe_wait_for_rate_limit()

        # Should sleep for 0.5 seconds (1.0 - 0.5)
        mock_sleep.assert_called_once_with(0.5)


class TestNoSleepWhenIntervalElapsed(unittest.TestCase):
    """Test that no sleep occurs when interval has elapsed."""

    def setUp(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    def tearDown(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    @patch.object(method_call.time, "sleep")
    @patch.object(method_call.time, "time", return_value=1002.0)
    def test_no_sleep_when_interval_elapsed(self, mock_time, mock_sleep):
        """No sleep when interval has already elapsed."""
        method_call.set_rate_limit(3600.0)  # 1 second interval
        method_call._RATE_LIMIT_LAST_REQUEST = 1000.0  # 2.0 seconds ago

        method_call._maybe_wait_for_rate_limit()

        mock_sleep.assert_not_called()


class TestFirstRequestNoSleep(unittest.TestCase):
    """Test that first request doesn't sleep."""

    def setUp(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    def tearDown(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    @patch.object(method_call.time, "sleep")
    @patch.object(method_call.time, "time", return_value=1000.0)
    def test_first_request_no_sleep(self, mock_time, mock_sleep):
        """First request (no last_request_time) doesn't sleep."""
        method_call.set_rate_limit(3600.0)  # Rate limiting enabled
        # _RATE_LIMIT_LAST_REQUEST is None (first request)

        method_call._maybe_wait_for_rate_limit()

        mock_sleep.assert_not_called()


class TestUpdatesLastRequestTime(unittest.TestCase):
    """Test that last request time is updated after waiting."""

    def setUp(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    def tearDown(self):
        """Reset rate limit state."""
        method_call.set_rate_limit(None)
        method_call._RATE_LIMIT_LAST_REQUEST = None

    @patch.object(method_call.time, "sleep")
    @patch.object(method_call.time, "time", return_value=1000.0)
    def test_updates_last_request_time(self, mock_time, mock_sleep):
        """Last request time is updated after _maybe_wait_for_rate_limit."""
        method_call.set_rate_limit(3600.0)

        method_call._maybe_wait_for_rate_limit()

        self.assertEqual(1000.0, method_call._RATE_LIMIT_LAST_REQUEST)

    @patch.object(method_call.time, "sleep")
    @patch.object(method_call.time, "time", return_value=1001.0)
    def test_updates_last_request_time_after_sleep(self, mock_time, mock_sleep):
        """Last request time is updated to current time after sleeping."""
        method_call.set_rate_limit(3600.0)  # 1 second interval
        method_call._RATE_LIMIT_LAST_REQUEST = 1000.5  # Would need to wait

        method_call._maybe_wait_for_rate_limit()

        # Should update to the current time after potential sleep
        self.assertEqual(1001.0, method_call._RATE_LIMIT_LAST_REQUEST)
