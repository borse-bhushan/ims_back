"""
tenant serializers module.
"""

from .tenant import TenantSerializer
from .query import TenantQuerySerializer

__all__ = ["TenantSerializer", "TenantQuerySerializer"]
