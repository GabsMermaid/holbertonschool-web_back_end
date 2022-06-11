#!/usr/bin/python3
""" LFU Caching: Create a class LFUCache that inherits
from BaseCaching and is a caching system """

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ Inherits all behaviors from BaseCaching except, upon any attempt to add
        an entry to the cache when it is at max capacity (as specified by
        BaseCaching.MAX_ITEMS), it discards the least frequently used entry to
        accommodate for the new one """

    def __init__(self):
        """ Creates new instance """
        super().__init__()
        self.keys = []
        self.uses = {}

    def put(self, key, item):
        """ Add key/value pair to cache data """

        if key is not None and item is not None:
            if (len(self.keys) == BaseCaching.MAX_ITEMS and
                    key not in self.keys):
                discard = self.keys.pop(self.keys.index(self.findLFU()))
                del self.cache_data[discard]
                del self.uses[discard]
                print('DISCARD: {:s}'.format(discard))
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
                self.uses[key] = 0
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
                self.uses[key] += 1

    def get(self, key):
        """ Return value stored in 'key' key of cache """
        if key is not None and key in self.cache_data:
            self.keys.append(self.keys.pop(self.keys.index(key)))
            self.uses[key] += 1
            return self.cache_data[key]
        return None

    def findLFU(self):
        """ Return key of least frequently used item in cache """
        items = list(self.uses.items())
        freqs = [item[1] for item in items]
        least = min(freqs)

        lfus = [item[0] for item in items if item[1] == least]
        for key in self.keys:
            if key in lfus:
                return key
