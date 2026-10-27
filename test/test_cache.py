"""Tests for flickr_api.cache.SimpleCache."""

from unittest.mock import patch

from flickr_api.cache import SimpleCache


class TestBasicOperations:
    def test_set_and_get(self):
        cache = SimpleCache()
        cache.set("k", "v")
        assert cache.get("k") == "v"

    def test_get_missing_returns_default(self):
        cache = SimpleCache()
        assert cache.get("missing") is None
        assert cache.get("missing", default=42) == 42

    def test_delete(self):
        cache = SimpleCache()
        cache.set("k", "v")
        cache.delete("k")
        assert cache.get("k") is None

    def test_delete_missing_key_is_silent(self):
        cache = SimpleCache()
        cache.delete("never-set")  # must not raise

    def test_len_counts_stored_entries(self):
        cache = SimpleCache()
        assert len(cache) == 0
        cache.set("a", 1)
        cache.set("b", 2)
        assert len(cache) == 2

    def test_has_key_and_contains(self):
        cache = SimpleCache()
        cache.set("k", "v")
        assert cache.has_key("k")  # noqa: W601 - part of the Django-style API
        assert "k" in cache
        assert "other" not in cache


class TestExpiry:
    def test_expired_entry_is_returned_as_default_and_purged(self):
        cache = SimpleCache(timeout=10)
        with patch("flickr_api.cache.time.time", return_value=1000.0):
            cache.set("k", "v")
        # After expiry time has passed the entry is treated as missing
        with patch("flickr_api.cache.time.time", return_value=1011.0):
            assert cache.get("k") is None
            assert "k" not in cache
            assert cache.has_key("k") is False  # noqa: W601
        # ... and purged from storage
        assert "k" not in cache.storage

    def test_set_with_explicit_timeout_overrides_default(self):
        cache = SimpleCache(timeout=10)
        with patch("flickr_api.cache.time.time", return_value=1000.0):
            cache.set("k", "v", timeout=100)
        with patch("flickr_api.cache.time.time", return_value=1050.0):
            assert cache.get("k") == "v"

    def test_contains_on_missing_key(self):
        cache = SimpleCache()
        assert "k" not in cache


class TestCulling:
    def test_cull_removes_every_third_entry(self):
        cache = SimpleCache(max_entries=10)
        for i in range(9):
            cache.set(f"k{i}", i)
        cache.cull()
        remaining = set(cache.storage)
        # cull_frequency=3: entries at index 0, 3, 6 are removed
        assert remaining == {f"k{i}" for i in range(9) if i % 3 != 0}

    def test_set_culls_when_full(self):
        cache = SimpleCache(max_entries=4)
        for i in range(5):
            cache.set(f"k{i}", i)
        assert len(cache) < 5
        assert "k0" not in cache.storage  # first entry culled


class TestConcurrency:
    def test_locking_allows_reentrant_access(self):
        cache = SimpleCache()
        # get() is decorated with @locking and internally calls delete()
        # (also locked); RLock semantics must allow the nesting.
        cache.set("k", "v")
        with patch("flickr_api.cache.time.time", return_value=1.0e12):
            assert cache.get("k") is None  # expired -> delete() inside get()
