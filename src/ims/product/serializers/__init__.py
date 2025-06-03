"""
tenant serializers module.
"""

from .product import CategorySerializer
from .query import CategoryQuerySerializer

__all__ = ["CategorySerializer", "CategoryQuerySerializer"]
