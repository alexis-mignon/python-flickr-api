"""Pytest configuration.

Doctests are collected from ``flickr_api/`` (see ``--doctest-modules`` in
``pyproject.toml``). Docstring examples that require a live Flickr API
connection cannot run in CI, so they are explicitly skipped here:

- ``flickr_api.auth``: the module docstring is a usage tutorial whose
  examples perform OAuth token requests.
- ``flickr_api.objects.Walker``: the examples call ``Photo.search`` live.
"""

import pytest

SKIP_DOCTESTS = ("flickr_api.auth", "flickr_api.objects.Walker")


def pytest_collection_modifyitems(items):
    for item in items:
        if item.name.startswith("flickr_api.") and any(
            item.name == skipped or item.name.startswith(skipped)
            for skipped in SKIP_DOCTESTS
        ):
            item.add_marker(
                pytest.mark.skip(reason="doctest requires a live Flickr API connection")
            )
