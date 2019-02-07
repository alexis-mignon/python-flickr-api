
release:
	rm -fr ./dist
	curv=`pipenv run python -c "from flickr_api._version import __version__ as v; print(v)"`
	nextv=`semver -i $curv`
	sed -e "s/$curv/$nextv/g" -i flickr_api/_version.py
	git commit -m"releasing version v$nextv"
	git tag "v$nextv"
	git push --tags
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
