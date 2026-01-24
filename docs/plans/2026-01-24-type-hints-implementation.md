# Type Hints Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add inline type hints to the public API of python-flickr-api for IDE autocompletion and type checking.

**Architecture:** Add type annotations to function signatures and class attributes in the public API modules. Use `Any` for dynamic API responses. Add `py.typed` marker for PEP 561 compliance.

**Tech Stack:** Python 3.10+ type hints, mypy for verification

---

## Task 1: Add mypy to dev dependencies

**Files:**
- Modify: `pyproject.toml:28-32`

**Step 1: Add mypy to dev dependencies**

Edit `pyproject.toml` to add mypy:

```toml
[dependency-groups]
dev = [
    "pytest",
    "flake8",
    "mypy",
]
```

**Step 2: Sync dependencies**

Run: `uv sync --dev`
Expected: mypy installed successfully

**Step 3: Commit**

```bash
git add pyproject.toml uv.lock
git commit -m "Add mypy to dev dependencies for type checking"
```

---

## Task 2: Type flickrerrors.py

**Files:**
- Modify: `flickr_api/flickrerrors.py`

**Step 1: Add type hints to FlickrAPIError**

```python
class FlickrAPIError(FlickrError):
    code: int
    message: str

    def __init__(self, code: int, message: str) -> None:
```

**Step 2: Add type hints to FlickrServerError**

```python
class FlickrServerError(FlickrError):
    status_code: int
    content: str

    def __init__(self, status_code: int, content: str) -> None:
```

**Step 3: Run mypy to verify**

Run: `uv run mypy flickr_api/flickrerrors.py --ignore-missing-imports`
Expected: Success: no issues found

**Step 4: Run tests**

Run: `uv run pytest -x`
Expected: All tests pass

**Step 5: Commit**

```bash
git add flickr_api/flickrerrors.py
git commit -m "Add type hints to flickrerrors.py"
```

---

## Task 3: Type keys.py

**Files:**
- Modify: `flickr_api/keys.py`

**Step 1: Add type hints**

```python
API_KEY: str | None = None
API_SECRET: str | None = None

# ... existing try/except ...

def set_keys(api_key: str, api_secret: str) -> None:
    global API_KEY, API_SECRET
    API_KEY = api_key
    API_SECRET = api_secret
```

**Step 2: Run mypy**

Run: `uv run mypy flickr_api/keys.py --ignore-missing-imports`
Expected: Success

**Step 3: Run tests**

Run: `uv run pytest -x`
Expected: All tests pass

**Step 4: Commit**

```bash
git add flickr_api/keys.py
git commit -m "Add type hints to keys.py"
```

---

## Task 4: Type auth.py

**Files:**
- Modify: `flickr_api/auth.py`

**Step 1: Add imports**

Add at top of file after existing imports:

```python
from typing import Any
```

**Step 2: Type AuthHandler class attributes and __init__**

```python
class AuthHandler:
    key: str
    secret: str
    callback: str
    request_token_key: str | None
    request_token_secret: str | None
    access_token_key: str | None
    access_token_secret: str | None

    def __init__(
        self,
        key: str | None = None,
        secret: str | None = None,
        callback: str | None = None,
        access_token_key: str | None = None,
        access_token_secret: str | None = None,
        request_token_key: str | None = None,
        request_token_secret: str | None = None,
    ) -> None:
```

**Step 3: Type AuthHandler methods**

```python
    def get_authorization_url(self, perms: str = 'read') -> str:

    def set_verifier(self, oauth_verifier: str) -> None:

    def complete_parameters(self, url: str, params: dict[str, Any] = {}) -> "OAuthRequest":

    def tofile(self, filename: str, include_api_keys: bool = False) -> None:

    def save(self, filename: str, include_api_keys: bool = False) -> None:

    def write(self, filename: str, include_api_keys: bool = False) -> None:

    def todict(self, include_api_keys: bool = False) -> dict[str, str]:

    @staticmethod
    def load(filename: str, set_api_keys: bool = False) -> "AuthHandler":

    @staticmethod
    def fromfile(filename: str, set_api_keys: bool = False) -> "AuthHandler":

    @staticmethod
    def fromdict(input_dict: dict[str, str]) -> "AuthHandler":

    @staticmethod
    def create(access_key: str, access_secret: str) -> "AuthHandler":
```

**Step 4: Type OAuthRequest class**

```python
class OAuthRequest:
    def __init__(self, url: str, params: dict[str, Any], oauth: OAuth1) -> None:

    def __iter__(self) -> Iterator[str]:

    def __getitem__(self, key: str) -> Any:

    def __setitem__(self, key: str, value: Any) -> None:

    def __contains__(self, key: object) -> bool:

    def items(self) -> ItemsView[str, Any]:

    def get(self, key: str, default: Any = None) -> Any:

    @property
    def oauth(self) -> OAuth1:
```

Add to imports: `from typing import Any, Iterator` and `from collections.abc import ItemsView`

**Step 5: Type module-level functions**

```python
def token_factory(
    filename: str | None = None,
    token_key: str | None = None,
    token_secret: str | None = None,
) -> AuthHandler:

def set_auth_handler(
    auth_handler: AuthHandler | str,
    set_api_keys: bool = False,
) -> None:
```

**Step 6: Run mypy**

Run: `uv run mypy flickr_api/auth.py --ignore-missing-imports`
Expected: Success

**Step 7: Run tests**

Run: `uv run pytest -x`
Expected: All tests pass

**Step 8: Commit**

```bash
git add flickr_api/auth.py
git commit -m "Add type hints to auth.py"
```

---

## Task 5: Type method_call.py (public functions only)

**Files:**
- Modify: `flickr_api/method_call.py`

**Step 1: Add typing import**

```python
from typing import Any
```

**Step 2: Type public functions**

```python
def enable_cache(cache_object: Any | None = None) -> None:

def disable_cache() -> None:

TIMEOUT: float = 10

def set_timeout(seconds: float) -> None:

def get_timeout() -> float:
```

**Step 3: Run mypy**

Run: `uv run mypy flickr_api/method_call.py --ignore-missing-imports`
Expected: Success (or only warnings about internal functions)

**Step 4: Run tests**

Run: `uv run pytest -x`
Expected: All tests pass

**Step 5: Commit**

```bash
git add flickr_api/method_call.py
git commit -m "Add type hints to method_call.py public functions"
```

---

## Task 6: Type upload.py

**Files:**
- Modify: `flickr_api/upload.py`

**Step 1: Add typing import**

```python
from typing import Any, BinaryIO
```

**Step 2: Type upload function**

```python
def upload(
    *,
    photo_file: str,
    photo_file_data: BinaryIO | None = None,
    title: str | None = None,
    description: str | None = None,
    tags: str | None = None,
    is_public: int | None = None,
    is_friend: int | None = None,
    is_family: int | None = None,
    safety_level: int | None = None,
    content_type: int | None = None,
    hidden: int | None = None,
    asynchronous: bool = False,
    **kwargs: Any,
) -> "Photo | UploadTicket":
```

Note: Since the current function uses `**args`, we'll keep it as `**kwargs: Any` to maintain compatibility.

**Step 3: Type replace function**

```python
def replace(
    *,
    photo_file: str,
    photo_id: str | None = None,
    photo: "Photo | None" = None,
    photo_file_data: BinaryIO | None = None,
    asynchronous: bool = False,
    **kwargs: Any,
) -> "Photo | UploadTicket":
```

Note: Keep as `**kwargs: Any` to maintain compatibility with current signature.

**Step 4: Add forward reference imports**

Add at top (TYPE_CHECKING block to avoid circular imports):

```python
from typing import TYPE_CHECKING, Any, BinaryIO
if TYPE_CHECKING:
    from .objects import Photo, UploadTicket
```

And update the existing import to be conditional.

**Step 5: Run mypy**

Run: `uv run mypy flickr_api/upload.py --ignore-missing-imports`
Expected: Success

**Step 6: Run tests**

Run: `uv run pytest -x`
Expected: All tests pass

**Step 7: Commit**

```bash
git add flickr_api/upload.py
git commit -m "Add type hints to upload.py"
```

---

## Task 7: Type objects.py - Base classes and Walker

**Files:**
- Modify: `flickr_api/objects.py`

**Step 1: Add typing imports**

Add after existing imports:

```python
from typing import Any, TypeVar, Generic, Callable, Iterator

T = TypeVar('T', bound='FlickrObject')
```

**Step 2: Type FlickrObject base class**

```python
class FlickrObject(object, metaclass=FlickrAutoDoc):
    __converters__: list[Callable[[dict[str, Any]], None]] = []
    __display__: list[str] = []
    __self_name__: str = ""
    loaded: bool

    def __init__(self, **params: Any) -> None:

    def _set_properties(self, **params: Any) -> None:

    def setToken(
        self,
        filename: str | None = None,
        token: "auth.AuthHandler | None" = None,
        token_key: str | None = None,
        token_secret: str | None = None,
    ) -> None:

    def getToken(self) -> "auth.AuthHandler | None":

    def __getattr__(self, name: str) -> Any:

    def __setattr__(self, name: str, values: Any) -> None:

    def get(self, key: str, *args: Any, **kwargs: Any) -> Any:

    def __getitem__(self, key: str) -> Any:

    def __setitem__(self, key: str, value: Any) -> None:

    def __str__(self) -> str:

    def __repr__(self) -> str:

    def getInfo(self) -> dict[str, Any]:

    def load(self) -> None:
```

**Step 3: Type FlickrList**

```python
class FlickrList(UserList[FlickrObject]):
    info: "Info | None"

    def __init__(
        self, data: list[FlickrObject] | None = None, info: "Info | None" = None
    ) -> None:

    def __str__(self) -> str:

    def __repr__(self) -> str:
```

**Step 4: Type Walker class**

```python
class Walker(Generic[T]):
    method: Callable[..., FlickrList]
    args: tuple[Any, ...]
    kwargs: dict[str, Any]
    stop: int | None

    def __init__(self, method: Callable[..., FlickrList], *args: Any, **kwargs: Any) -> None:

    def __len__(self) -> int:

    def __iter__(self) -> "Walker[T]":

    def __getitem__(self, slice_: slice) -> "SlicedWalker[T]":

    def __next__(self) -> T:

    def next(self) -> T:
```

**Step 5: Type SlicedWalker class**

```python
class SlicedWalker(Generic[T]):
    walker: Walker[T]
    start: int
    stop: int
    step: int

    def __init__(
        self, walker: Walker[T], start: int | None, stop: int | None, step: int | None
    ) -> None:

    def __len__(self) -> int:

    def __iter__(self) -> "SlicedWalker[T]":

    def __next__(self) -> T:

    def next(self) -> T:
```

**Step 6: Run mypy**

Run: `uv run mypy flickr_api/objects.py --ignore-missing-imports`
Expected: Success or minor warnings

**Step 7: Run tests**

Run: `uv run pytest -x`
Expected: All tests pass

**Step 8: Commit**

```bash
git add flickr_api/objects.py
git commit -m "Add type hints to objects.py base classes and Walker"
```

---

## Task 8: Type objects.py - Main domain classes (Photo, Person, Photoset, etc.)

**Files:**
- Modify: `flickr_api/objects.py`

**Step 1: Type Person class (key attributes)**

Add class-level type annotations for commonly-accessed attributes:

```python
class Person(FlickrObject):
    id: str
    username: str
    nsid: str
```

**Step 2: Type Photo class (key attributes)**

```python
class Photo(FlickrObject):
    id: str
    secret: str
    server: str
    farm: str
    title: str
    owner: Person
```

**Step 3: Type Photoset class (key attributes)**

```python
class Photoset(FlickrObject):
    id: str
    title: str
    description: str
    owner: Person
```

**Step 4: Type Gallery class (key attributes)**

```python
class Gallery(FlickrObject):
    id: str
    title: str
    owner: Person
```

**Step 5: Type Group class (key attributes)**

```python
class Group(FlickrObject):
    id: str
    name: str
```

**Step 6: Type Tag class (key attributes)**

```python
class Tag(FlickrObject):
    id: str
    text: str
    raw: str
```

**Step 7: Type helper function dict_converter**

```python
def dict_converter(
    keys: list[str], func: Callable[[Any], Any]
) -> Callable[[dict[str, Any]], None]:
```

**Step 8: Run mypy**

Run: `uv run mypy flickr_api/objects.py --ignore-missing-imports`
Expected: Success or minor warnings

**Step 9: Run tests**

Run: `uv run pytest -x`
Expected: All tests pass

**Step 10: Commit**

```bash
git add flickr_api/objects.py
git commit -m "Add type hints to objects.py domain classes"
```

---

## Task 9: Create py.typed marker

**Files:**
- Create: `flickr_api/py.typed`

**Step 1: Create empty py.typed file**

Create an empty file at `flickr_api/py.typed`

**Step 2: Verify py.typed is included in package**

Run: `uv build && unzip -l dist/*.whl | grep py.typed`
Expected: Shows `flickr_api/py.typed` in the wheel

**Step 3: Run tests**

Run: `uv run pytest -x`
Expected: All tests pass

**Step 4: Commit**

```bash
git add flickr_api/py.typed
git commit -m "Add py.typed marker for PEP 561 compliance"
```

---

## Task 10: Final verification

**Files:**
- None (verification only)

**Step 1: Run full mypy check**

Run: `uv run mypy flickr_api/ --ignore-missing-imports`
Expected: No errors on typed modules

**Step 2: Run full test suite**

Run: `uv run pytest`
Expected: All tests pass

**Step 3: Test IDE autocomplete (manual)**

Create a test script and verify autocomplete works:

```python
import flickr_api
flickr_api.set_keys("test", "test")
# Verify: IDE shows set_keys(api_key: str, api_secret: str) -> None
```

**Step 4: Clean up build artifacts**

Run: `rm -rf dist/`

---

## Summary

After completing all tasks:
- All public API functions have type hints
- mypy passes on typed files
- py.typed marker enables type discovery
- All existing tests pass
