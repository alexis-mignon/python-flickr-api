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
    url="https://github.com/alexis-mignon/python-flickr-api",
    packages=["flickr_api"],
    install_requires=[
        "oauth2",
        "six",
        "requests"
    ],
    license="BSD License",
    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ]
)
