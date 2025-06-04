"""
Serializer for Product.
"""

from decimal import Decimal

from rest_framework import serializers

from utils.messages import error
from utils.exceptions import codes
from utils.validators import validate_unique

from ..db_access import product_manager
from category.db_access import category_manager


class ProductSerializer(serializers.Serializer):
    """Serializer for the Product model"""

    category_id = serializers.UUIDField()
    product_code = serializers.CharField(max_length=256)
    product_name = serializers.CharField(max_length=256)

    sell_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, min_value=Decimal("0.01")
    )
    purchase_price = serializers.DecimalField(
        max_digits=10, decimal_places=2, min_value=Decimal("0.01")
    )

    def get_query(self, field_name, value):
        """
        Generate a query dictionary for product field validation.
        This method constructs a query dictionary used to check uniqueness of product fields.
        For updates, it excludes the current product instance from the uniqueness check.
        Args:
            field_name (str): The name of the field to query
            value: The value to check for uniqueness
        Returns:
            dict: Query dictionary containing field name and value,
            with optional product_id exclusion for updates
        """

        is_update = self.instance is not None

        query = {field_name: value}
        if is_update:
            query["product_id"] = {"NOT": self.instance.product_id}

        return query

    def validate_product_code(self, value):
        """
        Validate product_code field.
        - For create: product_code must not exist.
        - For update: product_code must not belong to a different product.
        """

        validate_unique(product_manager, self.get_query("product_code", value))

        return value

    def validate_product_name(self, value):
        """
        Validate product_name field.
        - For create: product_name must not exist.
        - For update: product_name must not belong to a different product.
        """

        validate_unique(product_manager, self.get_query("product_name", value))

        return value

    def validate_category_id(self, value):
        """
        Validate category_id field.
        - For create and update: category_id must exist.
        """

        if not category_manager.exists(query={"category_id": value}):
            raise serializers.ValidationError(
                error.NO_DATA_FOUND,
                code=codes.NO_DATA_FOUND,
            )

        return value
