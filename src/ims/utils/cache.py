"""
Interface for caching operations with tenant awareness support.
"""

from django.core.cache import cache as d_cache
from django.core.cache.backends.base import DEFAULT_TIMEOUT

from tenant.utils.helpers import get_tenant_details_from_request_thread


class CacheInterface:
    """
    This class provides a wrapper around a cache implementation with tenant-specific
    key management. When tenant awareness is enabled, cache keys are automatically
    prefixed with the tenant ID.
    """

    def __init__(self):
        self.cache = d_cache
        self.clear()

    def _build_key(key):
        """
        Builds a cache key by prefixing it with the tenant ID if available.
        """

        tenant_id = get_tenant_details_from_request_thread(raise_err=False)["tenant_id"]
        if not tenant_id:
            return key
        return f"{tenant_id}:{key}"

    def clear(self):
        """
        Clear the whole cache
        """
        self.cache.clear()

    def get(self, key, default=None):
        """
        Retrieve a value from cache by key
        """
        value = self.cache.get(self._build_key(key), default)
        return value

    def set(self, key, value, timeout=DEFAULT_TIMEOUT):
        """
        Store a value in cache with optional timeout
        """
        return self.cache.set(self._build_key(key), value, timeout)

    def delete(self, key):
        """
        Remove a value from cache by key
        """
        return self.cache.delete(self._build_key(key))

    def has_key(self, key):
        """
        Check if a key exists in cache
        """
        return self.cache.has_key(self._build_key(key))

    def clear(self):
        """
        Remove all entries from cache
        """
        return self.cache.clear()


cache = CacheInterface()
