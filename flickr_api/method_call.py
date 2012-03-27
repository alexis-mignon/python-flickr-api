"""
    method_call module.
    
    This module is used to perform the calls to the REST interface.
    
    Author: Alexis Mignon (c)
    e-mail: alexis.mignon@gmail.com
    Date  : 06/08/2011
    
"""
import urllib2
import urllib
import hashlib
import json

from flickrerrors import FlickrError,FlickrAPIError
from cache import SimpleCache

API_KEY = None
API_SECRET = None

try :
    import flickr_keys 
    API_KEY = flickr_keys.API_KEY
    API_SECRET = flickr_keys.API_SECRET
except ImportError :
    pass

def set_keys(api_key,api_secret):
    global API_KEY,API_SECRET
    API_KEY = api_key
    API_SECRET = api_secret

REST_URL = "http://api.flickr.com/services/rest/"

CACHE = None

def enable_cache(cache_object = None):
    global CACHE
    CACHE = cache_object or SimpleCache()


def disable_cache():
    global CACHE
    CACHE = None

def send_request(url,data):
    req = urllib2.Request(url,data)
    try :
        return urllib2.urlopen(req).read()
    except urllib2.HTTPError , e:
        raise FlickrError( e.read().split('&')[0] )
    

def call_api(api_key = None, api_secret = None, auth_handler = None, needssigning = False,request_url = REST_URL, raw = False,**args):
    """
        Performs the calls to the Flickr REST interface.
        
        Arguments :
            api_key : The API_KEY to use, if none is given, the key from flickr_keys is used.
            api_secret : The API_SECRET to use, if none is given, the key from flickr_keys is used.
            auth_handler : The authentication handler object to use to perform authentication
            request_url : The url to the rest interface to use by default the url in REST_URL is used.
            raw : if True the default xml response from the server is returned. if False (default)
                  a dictionnary built from the JSON answer is returned.
            args : the arguments to pass to the method.
    """
    
    if not api_key :
        api_key = API_KEY
    if not api_secret :
        api_secret = API_SECRET
    
    if not api_key or not api_secret :
        raise FlickrError("The Flickr API keys have not been set")

    clean_args(args)
    args["api_key"] = api_key
    if not raw :
        args["format"] = 'json'
        args["nojsoncallback"] = 1
    if auth_handler is None :
        if needssigning :
            query_elements = [e.split("=") for e in query.split("&")]
            query_elements.sort()
            sig = API_SECRET+["".join(["".join(e) for e in query_elements])]
            m = hashlib.md5()
            m.update(sig)
            api_sig = m.digest()
            args["api_sig"] = api_sig
        data = urllib.urlencode(args)
        
    else :
         data = auth_handler.complete_parameters(url = request_url,params = args).to_postdata()
    
    
    if CACHE is None :
        resp = send_request(request_url,data)
    else :
        resp = CACHE.get(data) or send_request(request_url,data)
        if data not in CACHE : CACHE.set(data,resp)

    if raw :
        return resp

    try :
        resp = json.loads(resp)
    except ValueError,e :
        print resp
        raise e

    if resp["stat"] != "ok" :
        raise FlickrAPIError(resp["code"],resp["message"])

    resp = clean_content(resp)

    return resp

def clean_content(d,lists = {}):
    """
        Cleans out recursively the keys comming from the JSON
        dictionnary.
        
        Namely: "_content" keys are replaces with their associated
            values if they are the only key of the dictionnary. Other
            wise they are replaces by a "text" key with the same value.
    """
    if isinstance(d,dict):
        d_clean = {}
        if len(d) == 1 and d.has_key("_content") :
            return clean_content(d["_content"])
        for k,v in d.iteritems() :
            if k == "_content" :
                k = "text"
            d_clean[k] = clean_content(v)
        return d_clean
    elif isinstance(d,list):
        return [clean_content(i) for i in d]
    else :
        return d

def clean_args(args):
    """
        Reformat the arguments.
    """
    for k,v in args.items() :
        if isinstance(v,bool):
            args[k] = int(v)
