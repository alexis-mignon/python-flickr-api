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

# ruff: noqa: I001
from ._version import __version__ as __version__  # noqa: F401
from .auth import set_auth_handler as set_auth_handler  # noqa: F401
from .keys import set_keys as set_keys  # noqa: F401
from .method_call import (  # noqa: F401
    disable_cache as disable_cache,
    enable_cache as enable_cache,
    get_timeout as get_timeout,
    set_timeout as set_timeout,
)

try:
    from . import objects as objects  # noqa: F401
    from .objects import *  # noqa: F401, F403
    from .upload import replace as replace, upload as upload  # noqa: F401

    Upload = upload  # Alias for backward compatibility
except Exception as e:
    print("Could not load all modules")
    print(type(e), e)
