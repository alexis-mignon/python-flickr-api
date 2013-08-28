Python Flickr API
-----------------

As complete as possible implementation of Flickr API.

The project provides an almost exhaustive access to the Flickr API, through an *object oriented* Python interface.

The project is still at an early stage and requires a lot of testing.
Any help including bug reports is appreciated.

Main features
-------------
  *  Object Oriented implementation
  *  (Almost) comprehensive implementation
  *  uses OAuth for authentication
  *  context sensitive objects (depending on the query context, objects may exhibit different attributes)
  *  An interface for direct seamless calls to the Flickr API.
  *  A (django-complient) caching mechanism

Requires
--------
	* python >= 2.6.5 
	* python-oauth (or the python module from http://code.google.com/p/oauth/)

[![githalytics.com alpha](https://cruel-carlota.pagodabox.com/950bd311453e675e4a06ec3a5e99e420 "githalytics.com")](http://githalytics.com/alexis-mignon/python-flickr-api)

Installation
------------

### From source

```bash
$ git clone https://github.com/alexis-mignon/python-flickr-api.git
$ cd python-flickr-api
$ python setup.py install --user  # to install in the user directory (~/.local)
$ sudo python setup.py install    # to install globally
```

### From Pypi

You can also install the last stable release using the `pip` progam:
```bash
$ pip install flickr_api --user  # to install in the user directory (~/.local)
$ sudo pip install flickr_api    # to install globally
```
See its [Pypi page](https://pypi.python.org/pypi/flickr_api/0.4).

Tutorial
--------
A short tutorial is available in the [Wiki section](https://github.com/alexis-mignon/python-flickr-api/wiki/Tutorial).

