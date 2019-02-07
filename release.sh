#! /bin/bash
set -ex

rm -fr ./dist
CURV=`pipenv run python -c "from flickr_api._version import __version__ as v; print(v)"`
NEXTV=`semver -i "$CURV"`
gsed -e "s/$CURV/$NEXTV/g" -i flickr_api/_version.py
git add .
git commit -m"releasing version v$NEXTV"
git tag "v$NEXTV"
git push --tags
python3 setup.py sdist bdist_wheel
twine upload dist/*
