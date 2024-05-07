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
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            key_to_pop = list(self.cache_data.keys())[0]
            for key in self.cache_data.keys():
                if key < key_to_pop:
                    key_to_pop = key
            self.cache_data.pop(key_to_pop)
            print("DISCARD: ", key_to_pop)

    def get(self, key):
        """get key: value from cache dict"""
        if key and key in self.cache_data.keys():
            return (self.cache_data[key])
        return None
