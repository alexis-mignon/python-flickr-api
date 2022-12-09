""" Version module.

    Allows to define the version number uniquely.
"""

try:
    import importlib.metadata

    __version__ = importlib.metadata.version("flickr_api")
except ImportError:
    import importlib_metadata  # pyright: reportMissingImports=false

    __version__ = importlib_metadata.version("flickr_api")
