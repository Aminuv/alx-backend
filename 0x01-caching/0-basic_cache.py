#!/usr/bin/python3
""" The class 'BasicCache' inherits """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ The class """

    def put(self, key, item):
        """ Function """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ get """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
