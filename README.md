# Python Flickr API

A Python implementation of the [Flickr API](https://www.flickr.com/services/developer/api/).

The project provides an almost exhaustive access to the [Flickr API](https://www.flickr.com/services/developer/api/), through an *object-oriented* Python interface.

## Quick Start

1. Install the package via PyPi (or manually cloning the repo):

```bash
pip install flickr_api
```

2. Aquire Flickr API keys and set up authorisation as per the [Wiki](https://github.com/alexis-mignon/python-flickr-api/wiki/Flickr-API-Keys-and-Authentication)

3. Start using the OO interface!

Here's an example of fetching a list of a specific users' public photos:

```python
user = flickr_api.Person.findByUserName("tomquirkphoto")
photos = user.getPhotos()
```

If you've authorised yourself as a user, you can do cooler things like upload photos:

```python
flickr_api.upload(photo_file="path_to_the_photo_file", title="My title")
```

And even create albums (a.k.a Photosets):

```python
photoset = flickr_api.Photoset.create(title="The title of the photoset", primary_photo=cover_photo)
```

## Features

Consult the [API Reference](https://github.com/alexis-mignon/python-flickr-api/wiki/API-reference) for a (semi) complete list

* Object Oriented implementation
* (Almost) comprehensive implementation
* Uses OAuth for authentication
* Context-sensitive objects (depending on the query context, objects may exhibit different attributes)
* An interface for direct seamless calls to the Flickr API.
* A (Django-compliant) caching mechanism

Requires:

* python >= 2.7
* [python-oauth2](https://github.com/joestump/python-oauth2)
* [six](https://github.com/benjaminp/six)
* requests

Please note that `flickrapi` on Pypi is a different distribution by a different author.

## API Guide

A brief guide is available in the [Wiki section](https://github.com/alexis-mignon/python-flickr-api/wiki/).

## Projects using this API
> create a PR to add your project here!

* [FlickrBox](https://github.com/tomquirk/FlickrBox) - A Dropbox-like backup experience for your free 1TB Flickr library!
* [Album Sorter](https://github.com/Scraft/flickr-album-sorter) - Sort flickr albums into date taken order

## Development
This project uses pipenv to create a virtualenv for development and control dependencies.

To run tests you can simply run it with:
```
pipenv install --dev
pipenv run nose2
```

To evoke the unittest module directly, one can run from the root directory (the directory with this file):

```
python -m unittest discover test
```

## Notes

The project is still at an early stage and requires a lot of testing.
Any help, including bug reports, is appreciated!
