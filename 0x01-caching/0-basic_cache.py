#!/usr/bin/env python3
""" the BaseCaching module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class for caching information """

    def __init__(self):
        """
        class initialize using the parent
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """ function """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ the return value """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
