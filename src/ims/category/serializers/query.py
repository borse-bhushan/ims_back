"""
Category Query Serializer
"""

from rest_framework import serializers

from base.serializers import QuerySerializer


class CategoryQuerySerializer(QuerySerializer):
    """
    Serializer for querying categories.
    """

    category_code = serializers.CharField(max_length=256)
    category_name = serializers.CharField(max_length=256)
