"""
Stock Serializer and Swagger Examples
"""

from decimal import Decimal
from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample
from utils.swagger import PaginationSerializer
from utils.swagger.common_swagger_functions import (
    get_create_success_example,
    get_list_success_example,
    get_by_id_success_example,
    get_delete_success_example,
)
from stock.constants import StockMovementEnum


# ----------------------------------
# Serializers
# ----------------------------------


class StockDataSerializer(serializers.Serializer):
    """
    Serializer for creating and updating stock records.
    """

    stock_id = serializers.UUIDField(
        required=True, help_text="PK for the stock record."
    )
    product_id = serializers.UUIDField(required=True, help_text="UUID of the product.")
    supplier_id = serializers.UUIDField(
        required=False,
        allow_null=True,
        default=None,
        help_text="UUID of the supplier (nullable).",
    )
    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=Decimal("0.01"),
        help_text="Unit price of the stock.",
    )
    movement_type = serializers.ChoiceField(
        choices=StockMovementEnum.choices, help_text="Type of stock movement (IN/OUT)."
    )
    quantity = serializers.IntegerField(
        min_value=1, help_text="Quantity of the stock item."
    )


class StockResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of stock-related endpoints.
    """

    data = StockDataSerializer(help_text="Stock information.")
    errors = serializers.JSONField(
        help_text="Any errors message for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class StockListDataSerializer(serializers.Serializer):
    """
    Serializer for the data field in stock list response.
    """

    list = StockDataSerializer(many=True, help_text="List of stock records.")
    pagination = PaginationSerializer(
        help_text="Pagination information for the list of stocks."
    )


class StockListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the stock list endpoint.
    """

    data = StockListDataSerializer(help_text="Stocks and pagination.")
    errors = serializers.JSONField(
        help_text="Any errors message for the response body.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# ----------------------------------
# Swagger Examples
# ----------------------------------

stock_sample_data = {
    "stock_id": "a84e7159-9d99-4b5a-98b6-4568c40267b4",
    "product_id": "b4f792e2-d1be-4398-9fdf-5265539e1f71",
    "supplier_id": "9187cfc1-ccfb-4c7e-8fd1-98e57c9b0f00",
    "price": 25.50,
    "movement_type": StockMovementEnum.IN.name,
    "quantity": 10,
}

stock_create_success_example: OpenApiExample = get_create_success_example(
    name="Create Stock - Success",
    data=stock_sample_data,
)

stock_list_success_example: OpenApiExample = get_list_success_example(
    name="List Stock - Success",
    list_data=[stock_sample_data],
)

stock_get_by_id_success_example: OpenApiExample = get_by_id_success_example(
    name="Get Stock by Id - Success",
    data=stock_sample_data,
)

stock_delete_success_example: OpenApiExample = get_delete_success_example(
    name="Delete Stock - Success",
)
