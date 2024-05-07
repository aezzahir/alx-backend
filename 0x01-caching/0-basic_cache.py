#!/usr/bin/python3
""" 0. Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache Class"""

    def put(self, key, item):
        """put key: value in cache dict"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """get key: value from cache dict"""
        if key and key in self.cache_data.keys():
            return (self.cache_data[key])
        return None
