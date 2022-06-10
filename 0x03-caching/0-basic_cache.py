#!/usr/bin/python3
""" Module for BasicCache """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Inherit from BaseCaching and is caching system """

    def put(self, key, item):
        """ Must assign to the dictionary self.cache_data
        the item value for the key key """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Must return the value in self.cache_data linked to key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
