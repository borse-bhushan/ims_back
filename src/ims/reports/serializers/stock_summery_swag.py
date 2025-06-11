"""
Report List - Serializer and Swagger Example (No Pagination)
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample

from stock.constants import StockMovementEnum
from utils.swagger.common_swagger_functions import get_list_success_example


# ----------------------------------
# Serializers
# ----------------------------------


class ReportProductSerializer(serializers.Serializer):
    """
    Serializer for product data inside report entry.
    """

    product_id = serializers.UUIDField()
    sell_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category_id = serializers.UUIDField()
    product_code = serializers.CharField()
    product_name = serializers.CharField()
    purchase_price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ReportEntrySerializer(serializers.Serializer):
    """
    Serializer for each report entry.
    """

    movement_type = serializers.ChoiceField(
        help_text="Stock movement type (IN / OUT)", choices=StockMovementEnum.choices
    )
    total_quantity = serializers.IntegerField(
        help_text="Total quantity of this movement"
    )
    product = ReportProductSerializer(help_text="Product details")


class ReportListResponseSerializer(serializers.Serializer):
    """
    Serializer for the report list response (without pagination).
    """

    data = ReportEntrySerializer(
        many=True, help_text="List of stock movement summary by product"
    )
    errors = serializers.JSONField(allow_null=True)
    messages = serializers.JSONField(allow_null=True)
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# ----------------------------------
# Swagger Example
# ----------------------------------

report_list_data_example = [
    {
        "movement_type": "IN",
        "total_quantity": 42,
        "product": {
            "product_id": "a4d4cd4f-6580-4a88-a157-b0eba816df60",
            "sell_price": 2.99,
            "category_id": "b4f792e2-d1be-4398-9fdf-5265539e1f71",
            "product_code": "asd",
            "product_name": "asdsad",
            "purchase_price": 1.23,
        },
    }
]

report_list_success_example: OpenApiExample = get_list_success_example(
    name="Report - Stock Movement by Product", list_data=report_list_data_example, pagination_data=False
)
