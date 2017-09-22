"""
module utils

some utility functions
"""

from six.moves import urllib


def urlopen_and_read(url):
    return urllib.request.urlopen(url).read().decode("utf8")
