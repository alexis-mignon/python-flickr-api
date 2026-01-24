# Type Hints Implementation Design

**Issue:** https://github.com/alexis-mignon/python-flickr-api/issues/127
**Date:** 2026-01-24

## Summary

Add inline type hints to the public API of python-flickr-api. Since the project requires Python 3.10+, inline annotations are preferred over separate `.pyi` stub files.

## Decisions

- **Inline types** in `.py` files (not separate `.pyi` files)
- **Public API scope** - type user-facing exports, skip internal modules
- **Pragmatic strictness** - type what's knowable, use `Any` for dynamic API responses
- **PEP 561 compliance** - add `py.typed` marker

## Files In Scope

| File | What to type |
|------|--------------|
| `flickrerrors.py` | Exception classes |
| `keys.py` | `set_keys` function |
| `auth.py` | `AuthHandler`, `set_auth_handler`, token functions |
| `method_call.py` | `enable_cache`, `disable_cache`, `set_timeout`, `get_timeout` |
| `upload.py` | `upload`, `replace` functions |
| `objects.py` | All public classes and their methods |
| `__init__.py` | Re-exports |

## Files Out of Scope

- `methods.py` - Auto-generated, 693KB
- `reflection.py` - Internal metaclass machinery
- `cache.py` - Internal cache implementation
- `api.py` - Dynamic proxy, hard to type meaningfully
- `tools.py`, `utils.py` - Internal helpers

## Typing Patterns

### FlickrObject Subclasses

```python
class Photo(FlickrObject):
    id: str
    secret: str
    server: str

    def getSizes(self) -> list[dict[str, Any]]: ...

    @staticmethod
    def search(**kwargs: Any) -> Walker[Photo]: ...
```

- Known attributes as class-level annotations
- `**kwargs: Any` for Flickr API passthrough parameters
- Concrete return types where possible

### Generic Collections

```python
class Walker(Generic[T]): ...
class FlickrList(UserList[FlickrObject]): ...
```

### Dynamic Object Creation

`FlickrObject.__init__` stays `**params: Any` since attributes come from API responses.

## Setup Changes

### New File

Create empty `flickr_api/py.typed` marker file.

### pyproject.toml

```toml
[tool.hatch.build.targets.wheel]
packages = ["flickr_api"]

[dependency-groups]
dev = [
    "pytest",
    "flake8",
    "mypy",
]
```

## Implementation Order

1. `flickrerrors.py`
2. `keys.py`
3. `auth.py`
4. `method_call.py`
5. `upload.py`
6. `objects.py`
7. `__init__.py`
8. `py.typed`

## Verification

1. Run mypy: `uv run mypy flickr_api/ --ignore-missing-imports`
2. Verify py.typed in wheel: `uv build && unzip -l dist/*.whl | grep py.typed`
3. Run existing tests: `uv run pytest`

## Done Criteria

- All public API functions/methods have type annotations
- mypy passes with no errors on typed files
- `py.typed` marker included in package distribution
- Existing tests pass
