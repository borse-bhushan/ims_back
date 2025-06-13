"""
Interface for caching operations with tenant awareness support.
"""

from django.core.cache import cache as d_cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT


class CacheInterface:
    """
    This class provides a wrapper around a cache implementation with tenant-specific
    key management. When tenant awareness is enabled, cache keys are automatically
    prefixed with the tenant ID.
    """

    def __init__(self):
        self.cache = d_cache
        self.clear()

    def clear(self):
        """
        Clear the whole cache
        """
        self.cache.clear()

    def get(self, key, default=None):
        """
        Retrieve a value from cache by key
        """
        value = self.cache.get(key, default)
        return value

    def set(self, key, value, timeout=DEFAULT_TIMEOUT):
        """
        Store a value in cache with optional timeout
        """
        return self.cache.set(key, value, timeout)

    def delete(self, key):
        """
        Remove a value from cache by key
        """
        return self.cache.delete(key)

    def has_key(self, key):
        """
        Check if a key exists in cache
        """
        return self.cache.has_key(key)

    def clear(self):
        """
        Remove all entries from cache
        """
        return self.cache.clear()


cache = CacheInterface()
