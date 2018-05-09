# -*- encoding: utf-8 -*-
# This code comes form the Stuvel's "flickrapi" project.

#Copyright (c) 2007 by the respective coders, see
#http://www.stuvel.eu/projects/flickrapi

#This code is subject to the Python licence, as can be read on
#http://www.python.org/download/releases/2.5.2/license/

#For those without an internet connection, here is a summary. When this
#summary clashes with the Python licence, the latter will be applied.

#Permission is hereby granted, free of charge, to any person obtaining
#a copy of this software and associated documentation files (the
#"Software"), to deal in the Software without restriction, including
#without limitation the rights to use, copy, modify, merge, publish,
#distribute, sublicense, and/or sell copies of the Software, and to
#permit persons to whom the Software is furnished to do so, subject to
#the following conditions:

#The above copyright notice and this permission notice shall be
#included in all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
''' Call result cache.

Designed to have the same interface as the `Django low-level cache API`_.
Heavily inspired (read: mostly copied-and-pasted) from the Django framework -
thanks to those guys for designing a simple and effective cache!

.. _`Django low-level cache API`:
    http://www.djangoproject.com/documentation/cache/#the-low-level-cache-api
'''

import threading
import time


class SimpleCache(object):
    '''Simple response cache for FlickrAPI calls.

    This stores max 50 entries, timing them out after 120 seconds:
    >>> cache = SimpleCache(timeout=120, max_entries=50)
    '''

    def __init__(self, timeout=300, max_entries=200):
        self.storage = {}
        self.expire_info = {}
        self.lock = threading.RLock()
        self.default_timeout = timeout
        self.max_entries = max_entries
        self.cull_frequency = 3

    def locking(method):
        '''Method decorator, ensures the method call is locked'''

        def locked(self, *args, **kwargs):
            self.lock.acquire()
            try:
                return method(self, *args, **kwargs)
            finally:
                self.lock.release()

        return locked

    @locking
    def get(self, key, default=None):
        '''Fetch a given key from the cache. If the key does not exist, return
        default, which itself defaults to None.
        '''

        now = time.time()
        exp = self.expire_info.get(key)
        if exp is None:
            return default
        elif exp < now:
            self.delete(key)
            return default

        return self.storage[key]

    @locking
    def set(self, key, value, timeout=None):
        '''Set a value in the cache. If timeout is given, that timeout will be
        used for the key; otherwise the default cache timeout will be used.
        '''

        if len(self.storage) >= self.max_entries:
            self.cull()
        if timeout is None:
            timeout = self.default_timeout
        self.storage[key] = value
        self.expire_info[key] = time.time() + timeout

    @locking
    def delete(self, key):
        '''Deletes a key from the cache, failing silently if it doesn't exist.
        '''

        if key in self.storage:
            del self.storage[key]
        if key in self.expire_info:
            del self.expire_info[key]

    @locking
    def has_key(self, key):
        '''Returns True if the key is in the cache and has not expired.'''
        return self.get(key) is not None

    @locking
    def __contains__(self, key):
        '''Returns True if the key is in the cache and has not expired.'''
        return self.has_key(key)

    @locking
    def cull(self):
        '''Reduces the number of cached items'''

        doomed = [k for (i, k) in enumerate(self.storage)
                  if i % self.cull_frequency == 0]
        for k in doomed:
            self.delete(k)

    @locking
    def __len__(self):
        '''Returns the number of cached items -- they might be expired
        though.
        '''

        return len(self.storage)
