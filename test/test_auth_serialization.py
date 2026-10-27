"""Tests for AuthHandler serialization and token helpers (no network)."""

import pytest
from unittest.mock import patch

from requests_oauthlib import OAuth1

from flickr_api import keys
from flickr_api.auth import AuthHandler, AuthHandlerError, OAuthRequest, token_factory


def make_oauth() -> OAuth1:
    return OAuth1("k", client_secret="s")


@pytest.fixture
def no_global_keys():
    """Ensure global API keys are unset during a test, then restore them."""
    saved = (keys.API_KEY, keys.API_SECRET)
    keys.API_KEY = keys.API_SECRET = None
    yield
    keys.API_KEY, keys.API_SECRET = saved


def make_handler(**kwargs):
    kwargs.setdefault("key", "test_key")
    kwargs.setdefault("secret", "test_secret")
    kwargs.setdefault("access_token_key", "access_key")
    kwargs.setdefault("access_token_secret", "access_secret")
    return AuthHandler(**kwargs)


class TestFileSerialization:
    def test_tofile_roundtrip_without_api_keys(self, tmp_path):
        handler = make_handler()
        path = str(tmp_path / "auth.txt")
        handler.tofile(path)
        with patch("flickr_api.auth.keys") as keys_mod:
            keys_mod.API_KEY = "global_key"
            keys_mod.API_SECRET = "global_secret"
            loaded = AuthHandler.load(path)
        assert loaded.access_token_key == "access_key"
        assert loaded.access_token_secret == "access_secret"
        assert loaded.key == "global_key"

    def test_tofile_roundtrip_with_api_keys(self, tmp_path):
        handler = make_handler()
        path = str(tmp_path / "auth.txt")
        handler.save(path, include_api_keys=True)
        loaded = AuthHandler.load(path)
        assert (loaded.key, loaded.secret) == ("test_key", "test_secret")
        assert loaded.access_token_key == "access_key"

    def test_write_is_an_alias_for_tofile(self, tmp_path):
        handler = make_handler()
        path = str(tmp_path / "auth.txt")
        handler.write(path, include_api_keys=True)
        assert AuthHandler.load(path).access_token_key == "access_key"

    def test_tofile_without_access_token_raises(self, tmp_path):
        handler = make_handler(request_token_key="req", request_token_secret="req_s")
        handler.access_token_key = handler.access_token_secret = None
        with pytest.raises(AuthHandlerError, match="Access token not set"):
            handler.tofile(str(tmp_path / "auth.txt"))

    def test_fromfile_without_api_keys_requires_global_keys(self, tmp_path, no_global_keys):
        path = tmp_path / "auth.txt"
        path.write_text("access_key\naccess_secret")
        with pytest.raises(ValueError, match="API keys have not been set"):
            AuthHandler.fromfile(str(path))


class TestDictSerialization:
    def test_todict_access_token(self):
        handler = make_handler()
        assert handler.todict() == {
            "access_token_key": "access_key",
            "access_token_secret": "access_secret",
        }

    def test_todict_includes_api_keys_when_asked(self):
        handler = make_handler()
        dump = handler.todict(include_api_keys=True)
        assert dump["api_key"] == "test_key"
        assert dump["api_secret"] == "test_secret"

    def test_todict_request_token(self):
        handler = make_handler(
            access_token_key=None, access_token_secret=None,
            request_token_key="req_key", request_token_secret="req_secret",
        )
        assert handler.todict() == {
            "request_token_key": "req_key",
            "request_token_secret": "req_secret",
        }

    def test_fromdict_roundtrip_with_api_keys(self):
        dump = make_handler().todict(include_api_keys=True)
        loaded = AuthHandler.fromdict(dump)
        assert loaded.key == "test_key"
        assert loaded.access_token_key == "access_key"
        assert loaded.access_token_secret == "access_secret"

    def test_fromdict_without_api_keys_requires_global_keys(self, no_global_keys):
        with pytest.raises(AuthHandlerError, match="Error occurred"):
            AuthHandler.fromdict({"access_token_key": "k", "access_token_secret": "s"})


class TestGuards:
    def test_get_authorization_url_without_request_token(self):
        handler = make_handler()
        with pytest.raises(AuthHandlerError, match="Request token is not defined"):
            handler.get_authorization_url()

    def test_set_verifier_without_request_token(self):
        handler = make_handler()
        with pytest.raises(AuthHandlerError, match="Request token is not defined"):
            handler.set_verifier("123456789")

    def test_missing_api_keys_raises(self):
        with patch("flickr_api.auth.keys") as keys_mod:
            keys_mod.API_KEY = None
            keys_mod.API_SECRET = None
            with pytest.raises(ValueError, match="API keys have not been set"):
                AuthHandler(key=None, secret=None, callback="oob")

    def test_init_without_access_or_request_token_hits_token_endpoint(self):
        with patch("flickr_api.auth.requests.post") as post:
            post.return_value.text = (
                "oauth_token=req_key&oauth_token_secret=req_secret"
            )
            handler = AuthHandler(key="k", secret="s", callback="oob")
        post.assert_called_once()
        assert handler.request_token_key == "req_key"
        assert handler.request_token_secret == "req_secret"
        assert handler.access_token_key is None


class TestTokenFactory:
    def test_explicit_tokens(self):
        with patch("flickr_api.auth.keys") as keys_mod:
            keys_mod.API_KEY = "k"
            keys_mod.API_SECRET = "s"
            handler = token_factory(token_key="tk", token_secret="ts")
        assert handler.access_token_key == "tk"
        assert handler.access_token_secret == "ts"

    def test_missing_tokens_raises(self):
        with pytest.raises(ValueError, match="cannot be None"):
            token_factory(token_key="tk")

    def test_from_file(self, tmp_path):
        path = tmp_path / "auth.txt"
        path.write_text("access_key\naccess_secret")
        with patch("flickr_api.auth.keys") as keys_mod:
            keys_mod.API_KEY = "k"
            keys_mod.API_SECRET = "s"
            handler = token_factory(filename=str(path))
        assert handler.access_token_key == "access_key"


class TestOAuthRequest:
    def test_dict_like_interface(self):
        request = OAuthRequest("http://example.com", {"a": 1}, oauth=make_oauth())
        request["b"] = 2
        assert dict(request.items()) == {"a": 1, "b": 2}
        assert list(request) == ["a", "b"]
        assert request["a"] == 1
        assert request.get("missing", "d") == "d"
        assert "a" in request
        assert "z" not in request

    def test_params_are_copied(self):
        params = {"a": 1}
        request = OAuthRequest("http://example.com", params, oauth=make_oauth())
        params["a"] = 999
        assert request["a"] == 1

    def test_complete_parameters(self):
        handler = make_handler()
        request = handler.complete_parameters("http://example.com", {"a": 1})
        assert isinstance(request, OAuthRequest)
        assert request.oauth.client.client_key == "test_key"
        assert request.oauth.client.client_secret == "test_secret"
        assert request.oauth.client.resource_owner_key == "access_key"
