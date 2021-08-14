#!/usr/bin/env python3
"""
class LFUCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache
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
        if key or item is None:
            return
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            if key not in self.cache_data.keys():
                lfu_elem = self.cache_data.keys()[-1]
                print(f"DISCARD: {lfu_elem}")
                del self.cache_data[lfu_elem]
                self.cache_data[key] = item

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
