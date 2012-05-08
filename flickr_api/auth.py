"""
    Authentication capabilities for the Flickr API.
    
    It implements the new authentication specifications of Flickr
    based on OAuth.
    
    The authentication process is in 3 steps.
    
    - Authorisation request :
    >>> a = AuthHandler(call_back_url)
    >>> a.get_authorization_url('write')
    print  'http://www.flickr.com/services/oauth/authorize?oauth_token=xxxx&perms=write'
    
    - The user gives his authorization at the url given by 'get_authorization_url'
      and is redrected to the 'call_back_url' with the oauth_verifier encoded
      in the url. This value can then be given to the AuthHandler:
      
    >>> a.set_verifier("66455xxxxx")
    
    - The authorization handler can then be set for the python session
      and will be automatically used when needed.
      
    >>> flickr_api.set_auth_handler(a)
    
    The authorization handler can also be saved and loaded :
    >>> a.write(filename)
    >>> a = AuthHandler.load(filename)

    Date   : 06/08/2011
    Author: Alexis Mignon <alexis.mignon@gmail.com>
    Author: Christoffer Viken <christoffer@viken.me>

"""

from oauth import oauth
import time
import urlparse
import urllib2
from method_call import API_KEY, API_SECRET

TOKEN_REQUEST_URL = "http://www.flickr.com/services/oauth/request_token"
AUTHORIZE_URL = "http://www.flickr.com/services/oauth/authorize"
ACCESS_TOKEN_URL = "http://www.flickr.com/services/oauth/access_token"

AUTH_HANDLER = None

class AuthHandlerError(Exception):
    pass

class AuthHandler(object):
    def __init__(self,key = API_KEY, secret = API_SECRET, callback = None, 
                 access_token_key = None, access_token_secret = None,
                 request_token_key = None, request_token_secret = None):
        if callback is None :
            callback = "http://api.flickr.com/services/rest/?method=flickr.test.echo&api_key=%s"%key
        self.key = key
        self.secret = secret
        params = {
            'oauth_timestamp': str(int(time.time())),
            'oauth_signature_method':"HMAC-SHA1",
            'oauth_version': "1.0",
            'oauth_callback': callback,
            'oauth_nonce': oauth.generate_nonce(),
            'oauth_consumer_key': self.key
        }

        self.consumer = oauth.OAuthConsumer(key=self.key, secret=self.secret)
        if (access_token_key is None) and (request_token_key is None) :
            req = oauth.OAuthRequest(http_method="GET", http_url=TOKEN_REQUEST_URL, parameters=params)
            req.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),self.consumer,None)
            resp = urllib2.urlopen(req.to_url())
            request_token = dict(urlparse.parse_qsl(resp.read()))
            self.request_token = oauth.OAuthToken(request_token['oauth_token'],request_token['oauth_token_secret'])
            self.access_token = None
        elif request_token_key is not None :
            self.access_token = None
            self.request_token = oauth.OAuthToken(request_token_key,request_token_secret)
        else :
            self.request_token = None
            self.access_token = oauth.OAuthToken(access_token_key,access_token_secret)


    def get_authorization_url(self,perms = 'read'):
        if self.request_token is None :
            raise AuthHandlerError("Request token is not defined. This ususally means that the access token has been loaded from a file.")
        return "%s?oauth_token=%s&perms=%s" % (AUTHORIZE_URL, self.request_token.key, perms)

    def set_verifier(self,oauth_verifier):
        if self.request_token is None :
            raise AuthHandlerError("Request token is not defined. This ususally means that the access token has been loaded from a file.")
        self.request_token.set_verifier(oauth_verifier)

        access_token_parms = {
            'oauth_consumer_key': self.key,
            'oauth_nonce': oauth.generate_nonce(),
            'oauth_signature_method':"HMAC-SHA1",
            'oauth_timestamp': str(int(time.time())),
            'oauth_token': self.request_token.key,
            'oauth_verifier' : self.request_token.verifier
        }

        req = oauth.OAuthRequest(http_method="GET", http_url=ACCESS_TOKEN_URL, parameters=access_token_parms)
        req.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),self.consumer,self.request_token)
        resp = urllib2.urlopen(req.to_url())
        access_token_resp = dict(urlparse.parse_qsl(resp.read()))
        self.access_token = oauth.OAuthToken(access_token_resp["oauth_token"],access_token_resp["oauth_token_secret"])

    def complete_parameters(self,url,params = {},exclude_signature = []):

        defaults = {
            'oauth_timestamp': str(int(time.time())),
            'oauth_nonce': oauth.generate_nonce(),
            'signature_method': "HMAC-SHA1",
            'oauth_token':self.access_token.key,
            'oauth_consumer_key':self.consumer.key,
        }

        excluded = {}
        for e in exclude_signature :
            excluded[e] = params.pop(e)

        defaults.update(params)
        req = oauth.OAuthRequest(http_method="POST", http_url=url, parameters=defaults)
        req.sign_request(oauth.OAuthSignatureMethod_HMAC_SHA1(),self.consumer,self.access_token)
        req.parameters.update(excluded)

        return req

    def tofile(self,filename):
        if self.access_token is None :
            raise AuthHandlerError("Access token not set yet.")
        with open(filename,"w") as f :
            f.write("\n".join([self.key,self.secret,self.access_token.key,self.access_token.secret]))

    def save(self,filename):
        self.tofile(filename)
    
    def write(self,filename):
        self.tofile(filename)
        
    def todict(self,include_api_keys=False):
        """
        Dumps the auth object to a dict,
        Optional inclusion of API-keys, in case you are using multiple.
        - include_api_keys: Whether API-keys should be included, False if you have control of them.
        """
        if self.access_token is not None:
            dump = {'access_token_key':self.access_token.key,'access_token_secret':self.access_token.secret}
        else:
            dump = {'request_token_key':self.request_token.key,'request_token_secret':self.request_token.secret}
        if include_api_keys:
            dump['api_key'] = self.key
            dump['api_secret'] = self.secret
        return dump
    
    @staticmethod
    def load(filename):
        return AuthHandler.fromfile(filename)
    
    @staticmethod
    def fromfile(filename):
        with open(filename,"r") as f :
            try :
                key,secret,access_key,access_secret = f.read().split("\n")
            except :
                access_key,access_secret = f.read().split("\n")
                key = API_KEY
                secret = API_SECRET
        return AuthHandler(key,secret,access_token_key = access_key,access_token_secret = access_secret)

    @staticmethod
    def fromdict(input_dict):
        """
        Loads an auth object from a dict.
        Structure identical to dict returned by todict
        - input_dict: Dictionary to build from
        """
        access_key,access_secret = None,None
        request_token_key,request_token_secret = None,None
        try:
            if 'api_key' in input_dict:
                key = input_dict['api_key']
                secret = input_dict['api_secret']
            else:
                key = API_KEY
                secret = API_SECRET
            if 'access_token_key' in input_dict:
                access_key = input_dict['access_token_key']
                access_secret = input_dict['access_token_secret']
            elif 'request_token_key' in input_dict:
                request_token_key = input_dict['request_token_key']
                request_token_secret = input_dict['request_token_secret']
        except Exception:
            raise AuthHandlerError("Error occurred while processing data")
        return AuthHandler(key,secret,access_token_key = access_key,access_token_secret = access_secret,
                           request_token_key = request_token_key, request_token_secret = request_token_secret)

    @staticmethod
    def create(access_key,access_secret):
        return AuthHandler(access_token_key = access_key,access_token_secret = access_secret)

def token_factory(filename = None, token_key = None, token_secret = None):
    if filename is None :
        if (token_key is None) or (token_secret is None):
            raise ValueError("token_secret and token_key cannot be None")
        return AuthHandler.create(token_key,token_secret)
    else :
        return AuthHandler.load(filename)

def set_auth_handler(auth_handler):
    global AUTH_HANDLER
    if isinstance(auth_handler,str):
        ah = AuthHandler.load(auth_handler)
        set_auth_handler(ah)
    else :
        AUTH_HANDLER = auth_handler
