#!/usr/bin/python3
""" 1. MRU caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching Class"""

    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """
        put key: value in cache dict MRU
        """

        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_in_key = list(self.cache_data.keys())[-1]
            self.cache_data.pop(first_in_key)
            print("DISCARD: {}".format(first_in_key))
        self.cache_data[key] = item

    def get(self, key):
        """
        get key: value from cache dict
        """
        item = self.cache_data.get(key)
        if key and key in self.cache_data.keys():
            self.cache_data.pop(key)
        self.put(key, item)
        return self.cache_data.get(key)
