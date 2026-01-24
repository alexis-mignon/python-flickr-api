API_KEY: str | None = None
API_SECRET: str | None = None

try:
    from . import flickr_keys  # type: ignore[attr-defined]

    API_KEY = flickr_keys.API_KEY
    API_SECRET = flickr_keys.API_SECRET
except ImportError:
    pass


def set_keys(api_key: str, api_secret: str) -> None:
    global API_KEY, API_SECRET
    API_KEY = api_key
    API_SECRET = api_secret
