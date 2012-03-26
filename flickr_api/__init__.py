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

from objects import *
import objects
from auth import set_auth_handler

import upload as Upload
from upload import upload,replace
from method_call import set_keys,enable_cache,disable_cache

#~ def set_auth_handler(auth_handler):
    #~ if isinstance(auth_handler,str):
        #~ ah = AuthHandler.load(auth_handler)
        #~ set_auth_handler(ah)
    #~ else :
        #~ objects.AUTH_HANDLER = auth_handler
        #~ Upload.AUTH_HANDLER = auth_handler
        #~ api.AUTH_HANDLER = auth_handler
