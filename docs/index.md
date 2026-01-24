# Python Flickr API Documentation

Welcome to the documentation for **python-flickr-api**, an object-oriented Python wrapper for the Flickr REST API.

## Overview

This library provides Pythonic access to Flickr functionality through domain objects (Photo, Person, Gallery, etc.) rather than raw API calls. It supports:

- Full object-oriented interface for photos, users, photosets, galleries, groups, and more
- Direct REST API access for advanced use cases
- OAuth 1.0a authentication
- Automatic pagination with the Walker utility
- Response caching
- Photo upload and replacement

## Quick Start

### Installation

```bash
pip install flickr_api
```

### Basic Usage

```python
import flickr_api

# Set your API credentials (required)
flickr_api.set_keys(api_key="your_api_key", api_secret="your_api_secret")

# Find a user
user = flickr_api.Person.findByUserName("username")

# Get their public photos
photos = user.getPublicPhotos()

# Search for photos
results = flickr_api.Photo.search(tags="sunset", per_page=10)

# Download a photo
photo = results[0]
photo.save("sunset.jpg", size_label="Large")
```

## Documentation

- **[Authentication](authentication.md)** - Setting up API keys and OAuth authentication
- **[API Reference](api-reference.md)** - Complete reference for all classes and methods

## Requirements

- Python 3.10+
- Flickr API key and secret ([get them here](https://www.flickr.com/services/apps/create/))

## Getting Help

If you find missing documentation or have questions, please [open an issue](https://github.com/alexis-mignon/python-flickr-api/issues) on GitHub.

## License

This project is open source. See the repository for license details.
