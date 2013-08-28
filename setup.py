from setuptools import setup
import re

VERSION_FILE = "flickr_api/_version.py"
try:
    vers_content = open(VERSION_FILE, "r").read()
    version_str = re.search(r'__version__ = "(.+?)"', vers_content).group(1)
except:
    raise RuntimeError("Could not read version file.")

setup(
    name="flickr_api",
    version=version_str,
    description="Python wrapper for the Flickr API",
    author="Alexis Mignon",
    author_email="alexis.mignon@gmail.com",
    url="http://code.google.com/p/python-flickr-api/",
    packages=["flickr_api"],
    install_requires=[
        "oauth",
    ],
    license="BSD License",
)
