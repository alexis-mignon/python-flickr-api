# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Python Flickr API is an object-oriented Python wrapper for the Flickr REST API. It provides Pythonic access to Flickr functionality through domain objects (Photo, Person, Gallery, etc.) rather than raw API calls.

## Development Commands

### Install Dependencies
```bash
uv sync --dev
```

### Run Tests
```bash
# All tests
uv run pytest

# Single test file
uv run pytest test/test_parse_sizes.py

# Specific test method
uv run pytest test/test_parse_sizes.py::TestPhotoSizes::test_video_largest_size
```

### Linting
```bash
uv run flake8 flickr_api/
```

## Architecture

### Module Responsibilities

- **objects.py**: Core domain objects (Photo, Person, Gallery, Photoset, Tag, etc.). Uses `FlickrObject` base class with metaclass `FlickrAutoDoc` for automatic documentation generation. Largest source file (~2000 lines).

- **method_call.py**: Central HTTP request handler. Manages OAuth signing, caching, timeouts (default 10s), and JSON response parsing. Entry point is `call_api()`.

- **auth.py**: 3-step OAuth 1.0a authentication flow. `AuthHandler` manages request/access tokens with serialization support.

- **api.py**: Proxy pattern for direct Flickr API calls (e.g., `flickr.photos.search(tags="test")`). Built dynamically from reflection metadata.

- **methods.py**: Auto-generated file (693KB) containing Flickr API method definitions from reflection. Do not edit manually.

- **cache.py**: Thread-safe `SimpleCache` with Django-compatible interface.

- **reflection.py**: Introspection of Flickr API methods, generates docstrings via `FlickrAutoDoc` metaclass.

### Key Patterns

**Dynamic Object Creation**: Objects are created from API responses with automatic property assignment. The `FlickrObject` base class handles initialization and metadata.

**Converter Pattern**: Objects define converters to transform API response fields (timestamps, size labels, etc.).

**Lazy Loading**: Objects track `loaded` attribute for on-demand data fetching.

**Flexible Arguments**: Methods accept either object instances or IDs:
```python
photo.addTag(tag=tag_object)    # Object
photo.addTag(tag_id="12345")    # ID string
```

### Module Dependencies
```
__init__.py → objects, auth, keys, upload, method_call
objects.py → method_call, auth, reflection, cache
api.py → method_call, reflection
method_call.py → requests, cache, auth, keys
```

## Important Conventions

- Python 3.10+ required
- API keys required before use: `flickr_api.set_keys(api_key="...", api_secret="...")`
- OAuth authentication optional for read-only, required for write operations
- Version defined in `flickr_api/_version.py` and `pyproject.toml`
