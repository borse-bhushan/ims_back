"""
Serializer for Stock.
"""

from decimal import Decimal

from rest_framework import serializers

from utils.messages import error
from utils.exceptions import codes

from product.db_access import product_manager
from supplier.db_access import supplier_manager

from ..db_access import stock_manager
from ..constants import StockMovementEnum


class StockSerializer(serializers.Serializer):
    """Serializer for the Stock model"""

    product_id = serializers.UUIDField()
    supplier_id = serializers.UUIDField(required=False, allow_null=True, default=None)

    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=Decimal("0.01"),
    )

    movement_type = serializers.ChoiceField(choices=StockMovementEnum.choices)

    quantity = serializers.IntegerField(min_value=1)

    def validate_product_id(self, value):
        """
        Validate product_id field.
        - For create and update: product_id must exist.
        """

        if not product_manager.exists(query={"product_id": value}):
            raise serializers.ValidationError(
                error.NO_DATA_FOUND,
                code=codes.NO_DATA_FOUND,
            )

        return value

    def validate_supplier_id(self, value):
        """
        Validate supplier_id field.
        - For create and update: supplier_id must exist.
        """

        movement_type = self.initial_data.get("movement_type")
        if movement_type == StockMovementEnum.IN:

            if value is None:
                raise serializers.ValidationError(
                    self.error_messages["required"], code=codes.REQUIRED
                )

        if value:
            if not supplier_manager.exists(query={"supplier_id": value}):
                raise serializers.ValidationError(
                    error.NO_DATA_FOUND,
                    code=codes.NO_DATA_FOUND,
                )

        return value

    def validate_quantity(self, value):
        """
        Validate quantity field.
        - For create and update: quantity must be greater than sum of quantity in stock.
        """

        movement_type = self.initial_data.get("movement_type")

        if movement_type == StockMovementEnum.OUT:
            quantity = self.initial_data.get("quantity")
            total_quantity = stock_manager.sum(
                field="quantity",
                query={"product_id": self.initial_data.get("product_id")},
            )

            if quantity > total_quantity:
                raise serializers.ValidationError(
                    error.STOCK_QUANTITY_NOT_AVAILABLE.format(quantity=quantity),
                    code=codes.NO_DATA_FOUND,
                )

        return value
