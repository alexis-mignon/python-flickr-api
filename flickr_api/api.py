"""
    module: api
    
    This module provide an interface to the REST API through a
    syntax mimicking the method names described on Flickr site.

    The hierarchy of methods is built once when the module is loaded.

    Author : Alexis Mignon (c)
    email  : alexis.mignon_at_gmail.com
    Date   : 08/08/2011

"""

from .method_call import call_api
from . import auth
from . import reflection

__methods__ = reflection.__methods__.keys()
__methods__ = sorted(__methods__)

__proxys__ = {}


def _get_proxy(name):
    """
        return the FlickrMethodProxy object with called 'name' from 
        the __proxys__ global dictionary. Creates the objects if needed.
    """
    if name in __proxys__ :
        return __proxys__[name]
    else :
        p = FlickrMethodProxy(name)
        __proxys__[name] = p
        return p

def _get_children_methods(name):
    """
        Get the list of method names having 'name' for prefix
    """
    return [ m for m in __methods__ if m.startswith(name + ".") ]

class FlickrMethodProxy(object):
    """
        Proxy object to perform seamless direct calls to Flickr
        API.
    """
    def __init__(self, name):
        self.name = name
        children = _get_children_methods(name)
        for child in children :
            child_node = child[(len(self.name) + 1):].split(".")[0]
            child_prefix = "%s.%s" % (self.name, child_node)
            self.__dict__[child_node] = _get_proxy(child_prefix)
        if self.name in __methods__ :
            self.__doc__ = reflection.make_docstring(self.name)

    def __call__(self, **kwargs):
        return call_api(auth_handler=auth.AUTH_HANDLER, raw=True,
                        method=self.name, **kwargs)
    
    def __repr__(self):
        return self.name

    def __str__(self):
        return repr(self)
    
    @staticmethod
    def set_auth_handler(token):
        auth.set_auth_handler(token)
        
if __methods__ :
    flickr = _get_proxy("flickr")

