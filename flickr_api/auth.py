"""
Authentication capabilities for the Flickr API.

It implements the new authentication specifications of Flickr
based on OAuth.

The authentication process is in 3 steps.

- Authorisation request:
>>> a = AuthHandler(call_back_url)
>>> a.get_authorization_url('write')
print  ('http://www.flickr.com/services/oauth/'
        'authorize?oauth_token=xxxx&perms=write')

- The user gives his authorization at the url given by
'get_authorization_url' and is redirected to the 'call_back_url' with
the `oauth_verifier` encoded in the url. This value can then be given to
the `AuthHandler`:

>>> a.set_verifier("66455xxxxx")

- The authorization handler can then be set for the python session
  and will be automatically used when needed.

>>> flickr_api.set_auth_handler(a)

The authorization handler can also be saved and loaded:
>>> a.write(filename)
>>> a = AuthHandler.load(filename)

Date: 06/08/2011
Author: Alexis Mignon <alexis.mignon@gmail.com>
Author: Christoffer Viken <christoffer@viken.me>

"""

from typing import Any
from collections.abc import Iterator, ItemsView

from requests_oauthlib import OAuth1
import requests
from . import keys

TOKEN_REQUEST_URL = "https://www.flickr.com/services/oauth/request_token"
AUTHORIZE_URL = "https://www.flickr.com/services/oauth/authorize"
ACCESS_TOKEN_URL = "https://www.flickr.com/services/oauth/access_token"

AUTH_HANDLER = None


class AuthHandlerError(Exception):
    pass


class AuthHandler(object):
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
        resolved_key = key or keys.API_KEY
        resolved_secret = secret or keys.API_SECRET

        if resolved_key is None or resolved_secret is None:
            raise ValueError("API keys have not been set.")

        # Type narrowing: after the check above, these are guaranteed to be str
        assert resolved_key is not None
        assert resolved_secret is not None
        self.key = resolved_key
        self.secret = resolved_secret

        if callback is None:
            callback = (
                "https://api.flickr.com/services/rest/"
                "?method=flickr.test.echo&api_key=%s" % self.key
            )

        self.callback = callback

        if (access_token_key is None) and (request_token_key is None):
            # Fetch request token
            oauth = OAuth1(self.key, client_secret=self.secret, callback_uri=callback)
            resp = requests.post(TOKEN_REQUEST_URL, auth=oauth)
            resp.raise_for_status()

            # Parse response
            token_data = dict(pair.split("=") for pair in resp.text.split("&"))

            self.request_token_key = token_data["oauth_token"]
            self.request_token_secret = token_data["oauth_token_secret"]
            self.access_token_key = None
            self.access_token_secret = None
        elif request_token_key is not None:
            self.request_token_key = request_token_key
            self.request_token_secret = request_token_secret
            self.access_token_key = None
            self.access_token_secret = None
        else:
            self.request_token_key = None
            self.request_token_secret = None
            self.access_token_key = access_token_key
            self.access_token_secret = access_token_secret

    def get_authorization_url(self, perms: str = "read") -> str:
        if self.request_token_key is None:
            raise AuthHandlerError(
                (
                    "Request token is not defined. This ususally means that the"
                    " access token has been loaded from a file."
                )
            )
        return "%s?oauth_token=%s&perms=%s" % (
            AUTHORIZE_URL,
            self.request_token_key,
            perms,
        )

    def set_verifier(self, oauth_verifier: str) -> None:
        if self.request_token_key is None:
            raise AuthHandlerError(
                (
                    "Request token is not defined. "
                    "This ususally means that the access token has been loaded "
                    "from a file."
                )
            )

        oauth = OAuth1(
            self.key,
            client_secret=self.secret,
            resource_owner_key=self.request_token_key,
            resource_owner_secret=self.request_token_secret,
            verifier=oauth_verifier,
        )
        resp = requests.post(ACCESS_TOKEN_URL, auth=oauth)
        resp.raise_for_status()

        # Parse response
        token_data = dict(pair.split("=") for pair in resp.text.split("&"))

        self.access_token_key = token_data["oauth_token"]
        self.access_token_secret = token_data["oauth_token_secret"]

    def complete_parameters(self, url: str, params: dict[str, Any] = {}) -> "OAuthRequest":
        """
        Returns an OAuth1 auth object that can be used with requests.
        For compatibility with existing code that expects a dict-like object,
        we return a wrapper that contains both the auth and the params.
        """
        oauth = OAuth1(
            self.key,
            client_secret=self.secret,
            resource_owner_key=self.access_token_key,
            resource_owner_secret=self.access_token_secret,
        )
        # Return an OAuthRequest object for compatibility
        return OAuthRequest(url, params, oauth)

    def tofile(self, filename: str, include_api_keys: bool = False) -> None:
        """saves authentication information to a file.

        Parameters:
        ----------
        filename: str
            The name of the file to which we save the information.

        include_api_keys: bool, optional (default False)
            Should we include the api keys in the file ? For security issues, it
            is recommended not to save the API keys information in several places
            and the default behaviour is thus not to save the API keys.
        """
        if self.access_token_key is None or self.access_token_secret is None:
            raise AuthHandlerError("Access token not set yet.")
        # Type narrowing: after the check above, these are guaranteed to be str
        access_token_key: str = self.access_token_key
        access_token_secret: str = self.access_token_secret
        with open(filename, "w") as f:
            if include_api_keys:
                f.write("\n".join([self.key, self.secret, access_token_key, access_token_secret]))
            else:
                f.write("\n".join([access_token_key, access_token_secret]))

    def save(self, filename: str, include_api_keys: bool = False) -> None:
        self.tofile(filename, include_api_keys)

    def write(self, filename: str, include_api_keys: bool = False) -> None:
        self.tofile(filename, include_api_keys)

    def todict(self, include_api_keys: bool = False) -> dict[str, str]:
        """
        Dumps the auth object to a dict,
        Optional inclusion of API-keys, in case you are using multiple.
        - include_api_keys: Whether API-keys should be included, False if you
        have control of them.
        """
        dump: dict[str, str]
        if self.access_token_key is not None:
            assert self.access_token_secret is not None
            dump = {
                "access_token_key": self.access_token_key,
                "access_token_secret": self.access_token_secret,
            }
        else:
            assert self.request_token_key is not None
            assert self.request_token_secret is not None
            dump = {
                "request_token_key": self.request_token_key,
                "request_token_secret": self.request_token_secret,
            }
        if include_api_keys:
            dump["api_key"] = self.key
            dump["api_secret"] = self.secret
        return dump

    @staticmethod
    def load(filename: str, set_api_keys: bool = False) -> "AuthHandler":
        """Load authentication information from a file.

        Parameters
        ----------
        filename: str
            The file in which authentication information is stored.

        set_api_keys: bool, optional (default False)
            If API keys are found in the file, should we use them to set the
            API keys globally.
            Default is False. The API keys should be stored separately from
            authentication information. The recommended way is to use a
            `flickr_keys.py` file. Setting `set_api_keys=True` should be considered
            as a conveniency only for single user settings.
        """
        return AuthHandler.fromfile(filename, set_api_keys)

    @staticmethod
    def fromfile(filename: str, set_api_keys: bool = False) -> "AuthHandler":
        """Load authentication information from a file.

        Parameters
        ----------
        filename: str
            The file in which authentication information is stored.

        set_api_keys: bool, optional (default False)
            If API keys are found in the file, should we use them to set the
            API keys globally.
            Default is False. The API keys should be stored separately from
            authentication information. The recommended way is to use a
            `flickr_keys.py` file. Setting `set_api_keys=True` should be considered
            as a conveniency only for single user settings.
        """
        with open(filename, "r") as f:
            keys_info = f.read().split("\n")
            try:
                key, secret, access_key, access_secret = keys_info
                if set_api_keys:
                    keys.set_keys(api_key=key, api_secret=secret)
            except ValueError:
                access_key, access_secret = keys_info
                if keys.API_KEY is None or keys.API_SECRET is None:
                    raise ValueError("API keys have not been set.")
                key = keys.API_KEY
                secret = keys.API_SECRET
        return AuthHandler(
            key, secret, access_token_key=access_key, access_token_secret=access_secret
        )

    @staticmethod
    def fromdict(input_dict: dict[str, str]) -> "AuthHandler":
        """
        Loads an auth object from a dict.
        Structure identical to dict returned by todict
        - input_dict: Dictionary to build from
        """
        access_key, access_secret = None, None
        request_token_key, request_token_secret = None, None
        try:
            if "api_key" in input_dict:
                key = input_dict["api_key"]
                secret = input_dict["api_secret"]
            else:
                if keys.API_KEY is None or keys.API_SECRET is None:
                    raise ValueError("API keys have not been set.")
                key = keys.API_KEY
                secret = keys.API_SECRET
            if "access_token_key" in input_dict:
                access_key = input_dict["access_token_key"]
                access_secret = input_dict["access_token_secret"]
            elif "request_token_key" in input_dict:
                request_token_key = input_dict["request_token_key"]
                request_token_secret = input_dict["request_token_secret"]
        except Exception:
            raise AuthHandlerError("Error occurred while processing data")

        return AuthHandler(
            key,
            secret,
            access_token_key=access_key,
            access_token_secret=access_secret,
            request_token_key=request_token_key,
            request_token_secret=request_token_secret,
        )

    @staticmethod
    def create(access_key: str, access_secret: str) -> "AuthHandler":
        return AuthHandler(access_token_key=access_key, access_token_secret=access_secret)


class OAuthRequest:
    """
    Wrapper class that provides compatibility with the old oauth2.Request interface.
    It holds the URL, parameters, and OAuth1 auth object for signing requests.
    """

    def __init__(self, url: str, params: dict[str, Any], oauth: OAuth1) -> None:
        self._url = url
        self._params = dict(params)
        self._oauth = oauth

    def __iter__(self) -> Iterator[str]:
        return iter(self._params)

    def __getitem__(self, key: str) -> Any:
        return self._params[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._params[key] = value

    def __contains__(self, key: object) -> bool:
        return key in self._params

    def items(self) -> ItemsView[str, Any]:
        return self._params.items()

    def get(self, key: str, default: Any = None) -> Any:
        return self._params.get(key, default)

    @property
    def oauth(self) -> OAuth1:
        """Return the OAuth1 auth object for use with requests."""
        return self._oauth


def token_factory(
    filename: str | None = None,
    token_key: str | None = None,
    token_secret: str | None = None,
) -> AuthHandler:
    if filename is None:
        if (token_key is None) or (token_secret is None):
            raise ValueError("token_secret and token_key cannot be None")
        return AuthHandler.create(token_key, token_secret)
    else:
        return AuthHandler.load(filename)


def set_auth_handler(
    auth_handler: AuthHandler | str,
    set_api_keys: bool = False,
) -> None:
    """Set the authentication handler globally.

    Parameters
    ----------
    auth_handler: AuthHandler object or str
        If a string is given, it corresponds to the file in which
        authentication information is stored.

    set_api_keys: bool, optional (default False)
        If API keys are found in the file, should we use them to set the
        API keys globally.
        Default is False. The API keys should be stored separately from
        authentication information. The recommended way is to use a
        `flickr_keys.py` file. Setting `set_api_keys=True` should be considered
        as a conveniency only for single user settings.
    """
    global AUTH_HANDLER
    if isinstance(auth_handler, str):
        ah = AuthHandler.load(auth_handler, set_api_keys)
        set_auth_handler(ah)
    else:
        AUTH_HANDLER = auth_handler
