"""
module utils

some utility functions
"""

import urllib.request


def urlopen_and_read(url):
    return urllib.request.urlopen(url).read().decode("utf8")
