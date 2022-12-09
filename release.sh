#!/bin/bash

VERSION=$(poetry version -s)
echo Getting ready to release version ${VERSION}

if [[ $(git tag -l | grep ${VERSION}) ]]; then
    echo ERROR: ${VERSION} tag already exists, bailing...
    exit 1
fi

if [[ -n $(git status -s) ]]; then
  echo ERROR: Repo is modified or has untracked files, bailing...
  exit 1
fi

git tag v`poetry version -s`
git push --tags
poetry build
poetry publish
poetry version patch
git add pyproject.toml
git commit -m "Bumps to version `poetry version -s`"
git push

echo Remember to edit the relase notes on https://github.com/alexis-mignon/python-flickr-api
