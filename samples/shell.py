"""
Usage:
  python shell.py <access_token_file>

Description:
  Starts a shell with a `user` object
  This makes it easier to start playing
  with the Flickr API.
"""
from __future__ import print_function

import flickr_api
import sys
import warnings

try:
    import IPython
except ImportError:
    """Not making iPython a dependency because
    this sample module is not core functionality.
    """
    ipython_required = 'iPython is required; pip install ipython.' \
        '\n  Run "pip install ipython" before using this sample module.'
    warnings.warn(ipython_required)



def main():
    """Start shell with `user` object
    """
    ACCESS_TOKEN = sys.argv[1]
    flickr_api.set_auth_handler(ACCESS_TOKEN)

    user_namespace = {
        'flickr_api': flickr_api,
        'user': flickr_api.test.login()}

    # iPython uses `sys.argv`
    # so we're resetting it
    sys.argv = sys.argv[:1]

    IPython.start_ipython(user_ns=user_namespace)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
    else:
        print (__doc__)

