#!/usr/bin/env python3
"""
class FIFOCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache
    """
    def __init__(self):
        """
        Initilize
        Call parent init
        """
        super().__init__()

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key is None or item is None:
            return
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                fifo_elem = self.cache_data.keys()[0]
                print(f"DISCARD: {fifo_elem}")
                del self.cache_data[fifo_elem]
                self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
