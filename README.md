# Python Flickr API

[![PyPI version](https://badge.fury.io/py/flickr-api.svg)](https://pypi.org/project/flickr-api/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-BSD--3--Clause-green.svg)](LICENSE)

An object-oriented Python wrapper for the [Flickr REST API](https://www.flickr.com/services/developer/api/).

This library provides Pythonic access to Flickr through domain objects like `Photo`, `Person`, `Gallery`, and `Photoset` rather than raw API calls. It covers almost the entire Flickr API.

> **Note:** This package is `flickr_api` on PyPI. The similarly named `flickrapi` is a different package by a different author.

## Installation

```bash
pip install flickr_api
```

Requires Python 3.10 or later.

## Quick Start

### 1. Get API Keys

Apply for API keys at [Flickr App Garden](https://www.flickr.com/services/apps/create/). You'll receive an API key and secret.

### 2. Configure the Library

```python
import flickr_api

flickr_api.set_keys(api_key="YOUR_API_KEY", api_secret="YOUR_API_SECRET")
```

### 3. Start Using It

Fetch a user's public photos:

```python
user = flickr_api.Person.findByUserName("username")
photos = user.getPhotos()

for photo in photos:
    print(photo.title)
```

Search for photos by tag:

```python
photos = flickr_api.Photo.search(tags="sunset", per_page=10)
```

### Authentication for Write Operations

Read-only operations (searching, fetching public data) only need API keys. To upload, edit, or access private content, you'll need OAuth authentication:

```python
# One-time setup: get authorization URL
auth_handler = flickr_api.auth.AuthHandler()
url = auth_handler.get_authorization_url("write")
print(f"Visit this URL and authorize: {url}")

# After user authorizes, set the verifier
auth_handler.set_verifier("VERIFIER_CODE_FROM_FLICKR")
flickr_api.set_auth_handler(auth_handler)

# Save credentials for later
auth_handler.save("flickr_auth.txt")
```

```python
# In future sessions, load saved credentials
auth_handler = flickr_api.auth.AuthHandler.load("flickr_auth.txt")
flickr_api.set_auth_handler(auth_handler)
```

Now you can upload photos and create albums:

```python
# Upload a photo
flickr_api.upload(photo_file="vacation.jpg", title="Beach sunset", tags="vacation beach")

# Create an album
photo = flickr_api.Photo.search(user_id="me")[0]
photoset = flickr_api.Photoset.create(title="Vacation 2024", primary_photo=photo)
```

## Features

- **Object-oriented interface** - Work with `Photo`, `Person`, `Photoset`, `Gallery`, and other domain objects
- **Comprehensive API coverage** - Access to nearly all Flickr API methods
- **OAuth 1.0a authentication** - Secure authentication for write operations
- **Flexible method arguments** - Pass either objects or IDs:
  ```python
  photo.addTag(tag=tag_object)    # Using object
  photo.addTag(tag_id="12345")    # Using ID string
  ```
- **Built-in caching** - Django-compatible cache interface to reduce API calls
- **Direct API access** - Bypass objects and call the Flickr API directly when needed:
  ```python
  flickr_api.flickr.photos.search(tags="test")
  ```

## Documentation

For more detailed documentation, see the [`docs/`](docs/) folder:

- **[Getting Started](docs/index.md)** - Overview and quick start guide
- **[Authentication](docs/authentication.md)** - API keys and OAuth setup
- **[API Reference](docs/api-reference.md)** - Complete reference for all classes and methods

## Projects Using This Library

- [FlickrBox](https://github.com/tomquirk/FlickrBox) - Dropbox-like backup for your Flickr library
- [Album Sorter](https://github.com/Scraft/flickr-album-sorter) - Sort Flickr albums by date taken
- [Flickr Download](https://github.com/beaufour/flickr-download) - Download photos and sets from Flickr

> Have a project using this library? Open a PR to add it here!

## Development

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Install dependencies
uv sync --dev

# Run tests
uv run pytest

# Run linter
uv run flake8 flickr_api/
```

## Contributing

Bug reports, feature requests, and pull requests are welcome on [GitHub](https://github.com/alexis-mignon/python-flickr-api).
