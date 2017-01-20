"""
    Object Oriented implementation of Flickr API.

    Important notes:
    - For consistency, the nameing of methods might differ from the name
      in the official API. Please check the method "docstring" to know
      what is the implemented method.

    - For methods which expect an object "id", either the 'id' string
      or the object itself can be used as argument. Similar consideration
      holds for lists of id's.

      For instance if "photo_id" is expected you can give call the function
      with named argument "photo = PhotoObject" or with the id string
      "photo_id = id_string".


    Author : Alexis Mignon (c)
    email  : alexis.mignon_at_gmail.com
    Date   : 05/08/2011

"""

from __future__ import print_function

try:
    from .objects import *
    from . import objects
    from .upload import upload as Upload
    from .upload import upload, replace
except Exception as e:
    print ("Could not load all modules")
    print (type(e), e)

from .auth import set_auth_handler
from .method_call import enable_cache, disable_cache
from .keys import set_keys
from ._version import __version__
