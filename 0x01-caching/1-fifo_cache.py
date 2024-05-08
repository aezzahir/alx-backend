#!/usr/bin/python3
""" 1. FIFO caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO Caching Class"""

    def __init__(self):
        """init"""
        super().__init__()

    def put(self, key, item):
        """
        put key: value in cache dict FIFO
        """

        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_in_key = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_in_key)
            print("DISCARD: {}".format(first_in_key))
        self.cache_data[key] = item

    def get(self, key):
        """
        get key: value from cache dict
        """
        return self.cache_data.get(key)
