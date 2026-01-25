#!/bin/bash
set -ex

rm -rf ./dist

VERSION=$(uv run python -c "from flickr_api._version import __version__ as v; print(v)")

git tag "v$VERSION"
git push origin "v$VERSION"

uv build
uv run twine upload dist/*
