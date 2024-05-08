#!/usr/bin/python3
""" 1. LFU caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Caching Class"""

    def __init__(self):
        """init"""
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """
        put key: value in cache dict LFU
        """

        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            k = min(self.cache_data, key=self.cache_data.get)
            if list(self.cache_data.values()).count(self.cache_data[k]) > 1:
                k = list(self.cache_data.keys())[0]
            self.cache_data.pop(k)
            self.frequency.pop(k)
            print("DISCARD: {}".format(k))
        self.cache_data[key] = item
        if key not in self.frequency:
            self.frequency[key] = 0

    def get(self, key):
        """
        get key: value from cache dict
        """
        item = self.cache_data.get(key)
        if key and key in self.cache_data.keys():
            self.cache_data.pop(key)
            self.frequency[key] += 1
        self.cache_data.put(key, item)
        return self.cache_data.get(key)
