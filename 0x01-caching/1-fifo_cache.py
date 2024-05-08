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
        """put key: value in cache dict FIFO"""

        if key is None or item is None:
            return
        if len(self.cache_data.keys()) >= BaseCaching.MAX_ITEMS:
            key_to_pop = list(self.cache_data.keys())[0]
            self.cache_data.pop(key_to_pop)
            print("DISCARD: ", key_to_pop)
        self.cache_data[key] = item

    def get(self, key):
        """get key: value from cache dict"""
        if key and key in self.cache_data.keys():
            return (self.cache_data[key])
        return None
