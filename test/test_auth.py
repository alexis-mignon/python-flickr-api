"""Regression tests for authentication callback warnings."""

import warnings
from unittest.mock import patch

import pytest

from flickr_api.auth import AuthHandler


DEFAULT_CALLBACK = "https://api.flickr.com/services/rest/?method=flickr.test.echo&api_key=test_key"


def test_load_access_token_without_callback_does_not_warn(tmp_path):
    token_file = tmp_path / "auth.txt"
    token_file.write_text("test_key\ntest_secret\naccess_key\naccess_secret")

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        with patch("flickr_api.auth.requests.post") as post:
            handler = AuthHandler.load(str(token_file))

    post.assert_not_called()
    assert handler.access_token_key == "access_key"
    assert handler.access_token_secret == "access_secret"
    assert handler.callback == DEFAULT_CALLBACK


@pytest.mark.parametrize("token_type", ["access", "request"])
def test_restore_token_from_dict_without_callback_does_not_warn(token_type):
    data = {
        "api_key": "test_key",
        "api_secret": "test_secret",
        f"{token_type}_token_key": "token_key",
        f"{token_type}_token_secret": "token_secret",
    }

    with warnings.catch_warnings():
        warnings.simplefilter("error")
        with patch("flickr_api.auth.requests.post") as post:
            handler = AuthHandler.fromdict(data)

    post.assert_not_called()
    assert getattr(handler, f"{token_type}_token_key") == "token_key"
    assert getattr(handler, f"{token_type}_token_secret") == "token_secret"
    assert handler.callback == DEFAULT_CALLBACK


@pytest.mark.parametrize("callback", [None, "oob", "https://example.com/callback"])
def test_new_authorization_callback_warning(callback):
    with patch("flickr_api.auth.requests.post") as post:
        post.return_value.text = "oauth_token=request_key&oauth_token_secret=request_secret"
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            handler = AuthHandler(key="test_key", secret="test_secret", callback=callback)

    if callback is None:
        assert len(caught) == 1
        assert caught[0].category is UserWarning
        assert "No 'callback' was provided" in str(caught[0].message)
    else:
        assert not caught
    assert handler.callback == (DEFAULT_CALLBACK if callback is None else callback)
    assert handler.request_token_key == "request_key"
    assert handler.request_token_secret == "request_secret"
    post.assert_called_once()
    assert post.call_args.kwargs["auth"].client.callback_uri == handler.callback
