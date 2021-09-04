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

import oauth2
import time
from six import string_types
from six.moves import urllib
from .utils import urlopen_and_read
from . import keys

TOKEN_REQUEST_URL = "https://www.flickr.com/services/oauth/request_token"
AUTHORIZE_URL = "https://www.flickr.com/services/oauth/authorize"
ACCESS_TOKEN_URL = "https://www.flickr.com/services/oauth/access_token"

AUTH_HANDLER = None


class AuthHandlerError(Exception):
    pass


class AuthHandler(object):
    def __init__(self, key=None, secret=None, callback=None,
                 access_token_key=None, access_token_secret=None,
                 request_token_key=None, request_token_secret=None):

        self.key = key or keys.API_KEY
        self.secret = secret or keys.API_SECRET

        if self.key is None or self.secret is None:
            raise ValueError("API keys have not been set.")

        if callback is None:
            callback = ("https://api.flickr.com/services/rest/"
                        "?method=flickr.test.echo&api_key=%s" % self.key)

        params = {
            'oauth_timestamp': str(int(time.time())),
            'oauth_signature_method': "HMAC-SHA1",
            'oauth_version': "1.0",
            'oauth_callback': callback,
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_consumer_key': self.key
        }

        self.consumer = oauth2.Consumer(key=self.key, secret=self.secret)
        if (access_token_key is None) and (request_token_key is None):
            req = oauth2.Request(method="GET",
                                 url=TOKEN_REQUEST_URL,
                                 parameters=params)
            req.sign_request(oauth2.SignatureMethod_HMAC_SHA1(),
                             self.consumer, None)

            resp = urlopen_and_read(req.to_url())
            request_token = dict(urllib.parse.parse_qsl(resp))

            self.request_token = oauth2.Token(
                request_token['oauth_token'],
                request_token['oauth_token_secret']
            )
            self.access_token = None
        elif request_token_key is not None:
            self.access_token = None
            self.request_token = oauth2.Token(
                request_token_key,
                request_token_secret
            )
        else:
            self.request_token = None
            self.access_token = oauth2.Token(
                access_token_key,
                access_token_secret
            )

    def get_authorization_url(self, perms='read'):
        if self.request_token is None:
            raise AuthHandlerError(
                ("Request token is not defined. This ususally means that the"
                 " access token has been loaded from a file.")
            )
        return "%s?oauth_token=%s&perms=%s" % (
            AUTHORIZE_URL, self.request_token.key, perms
        )

    def set_verifier(self, oauth_verifier):
        if self.request_token is None:
            raise AuthHandlerError(
                ("Request token is not defined. "
                 "This ususally means that the access token has been loaded "
                 "from a file.")
            )
        self.request_token.set_verifier(oauth_verifier)

        access_token_parms = {
            'oauth_consumer_key': self.key,
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_signature_method': "HMAC-SHA1",
            'oauth_timestamp': str(int(time.time())),
            'oauth_token': self.request_token.key,
            'oauth_verifier': self.request_token.verifier
        }

        req = oauth2.Request(method="GET", url=ACCESS_TOKEN_URL,
                             parameters=access_token_parms)
        req.sign_request(oauth2.SignatureMethod_HMAC_SHA1(),
                         self.consumer, self.request_token)
        resp = urlopen_and_read(req.to_url())
        access_token_resp = dict(urllib.parse.parse_qsl(resp))

        self.access_token = oauth2.Token(
            access_token_resp["oauth_token"],
            access_token_resp["oauth_token_secret"]
        )

    def complete_parameters(self, url, params={}):

        defaults = {
            'oauth_timestamp': str(int(time.time())),
            'oauth_nonce': oauth2.generate_nonce(),
            'signature_method': "HMAC-SHA1",
            'oauth_token': self.access_token.key,
            'oauth_consumer_key': self.consumer.key,
        }

        defaults.update(params)
        req = oauth2.Request(method="POST", url=url, parameters=defaults)
        req.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), self.consumer,
                         self.access_token)

        return req

    def tofile(self, filename, include_api_keys=False):
        """ saves authentication information to a file.

    Parameters:
    ----------
    filename: str
        The name of the file to which we save the information.

    include_api_keys: bool, optional (default False)
        Should we include the api keys in the file ? For security issues, it
        is recommended not to save the API keys information in several places
        and the default behaviour is thus not to save the API keys.
"""
        if self.access_token is None:
            raise AuthHandlerError("Access token not set yet.")
        with open(filename, "w") as f:
            if include_api_keys:
                f.write("\n".join([self.key, self.secret,
                                   self.access_token.key, self.access_token.secret]))
            else:
                f.write("\n".join([self.access_token.key,
                                   self.access_token.secret]))

    def save(self, filename, include_api_keys=False):
        self.tofile(filename, include_api_keys)

    def write(self, filename, include_api_keys=False):
        self.tofile(filename, include_api_keys)

    def todict(self, include_api_keys=False):
        """
        Dumps the auth object to a dict,
        Optional inclusion of API-keys, in case you are using multiple.
        - include_api_keys: Whether API-keys should be included, False if you
        have control of them.
        """
        if self.access_token is not None:
            dump = {'access_token_key': self.access_token.key,
                    'access_token_secret': self.access_token.secret}
        else:
            dump = {'request_token_key': self.request_token.key,
                    'request_token_secret': self.request_token.secret}
        if include_api_keys:
            dump['api_key'] = self.key
            dump['api_secret'] = self.secret
        return dump

    @staticmethod
    def load(filename, set_api_keys=False):
        """ Load authentication information from a file.

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
    def fromfile(filename, set_api_keys=False):
        """ Load authentication information from a file.

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
                key = keys.API_KEY
                secret = keys.API_SECRET
        return AuthHandler(key, secret, access_token_key=access_key,
                           access_token_secret=access_secret)

    @staticmethod
    def fromdict(input_dict):
        """
        Loads an auth object from a dict.
        Structure identical to dict returned by todict
        - input_dict: Dictionary to build from
        """
        access_key, access_secret = None, None
        request_token_key, request_token_secret = None, None
        try:
            if 'api_key' in input_dict:
                key = input_dict['api_key']
                secret = input_dict['api_secret']
            else:
                key = keys.API_KEY
                secret = keys.API_SECRET
            if 'access_token_key' in input_dict:
                access_key = input_dict['access_token_key']
                access_secret = input_dict['access_token_secret']
            elif 'request_token_key' in input_dict:
                request_token_key = input_dict['request_token_key']
                request_token_secret = input_dict['request_token_secret']
        except Exception:
            raise AuthHandlerError("Error occurred while processing data")

        return AuthHandler(key, secret, access_token_key=access_key,
                           access_token_secret=access_secret,
                           request_token_key=request_token_key,
                           request_token_secret=request_token_secret)

    @staticmethod
    def create(access_key, access_secret):
        return AuthHandler(access_token_key=access_key,
                           access_token_secret=access_secret)


def token_factory(filename=None, token_key=None, token_secret=None):
    if filename is None:
        if (token_key is None) or (token_secret is None):
            raise ValueError("token_secret and token_key cannot be None")
        return AuthHandler.create(token_key, token_secret)
    else:
        return AuthHandler.load(filename)


def set_auth_handler(auth_handler, set_api_keys=False):
    """ Set the authentication handler globally.

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
    if isinstance(auth_handler, string_types):
        ah = AuthHandler.load(auth_handler, set_api_keys)
        set_auth_handler(ah)
    else:
        AUTH_HANDLER = auth_handler
