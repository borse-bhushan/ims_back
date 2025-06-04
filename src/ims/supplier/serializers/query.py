"""
Supplier Query Serializer
"""

from rest_framework import serializers

from base.serializers import QuerySerializer


class SupplierQuerySerializer(QuerySerializer):
    """
    Serializer for querying suppliers.
    """

    supplier_code = serializers.CharField(max_length=256)
    supplier_name = serializers.CharField(max_length=256)
