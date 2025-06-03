"""
Product Query Serializer
"""

from rest_framework import serializers

from base.serializers import QuerySerializer


class ProductQuerySerializer(QuerySerializer):
    """
    Serializer for querying products.
    """

    product_code = serializers.CharField(max_length=256)
    product_name = serializers.CharField(max_length=256)
