#!/usr/bin/python3

""" Basic Dictionary """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic cache dictionary"""

    def put(self, key, item):
        """Caches item'"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves cached item"""
        return self.cache_data.get(key, None)
