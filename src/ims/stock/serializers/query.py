"""
Stock Query Serializer
"""

from rest_framework import serializers

from base.serializers import QuerySerializer

from ..constants import StockMovementEnum


class StockQuerySerializer(QuerySerializer):
    """
    Serializer for querying stocks.
    """

    product_id = serializers.UUIDField()
    supplier_id = serializers.UUIDField()

    reference_number = serializers.CharField(max_length=256)
    movement_type = serializers.ChoiceField(choices=StockMovementEnum.choices)
