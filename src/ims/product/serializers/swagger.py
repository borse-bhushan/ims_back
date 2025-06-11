"""
Product Serializer and Swagger Examples
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample
from utils.swagger import PaginationSerializer
from utils.swagger.common_swagger_functions import (
    get_create_success_example,
    get_update_success_example,
    get_list_success_example,
    get_by_id_success_example,
    get_delete_success_example,
)


# ----------------------------------
# Serializers
# ----------------------------------


class ProductDataSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a product.
    """

    product_id = serializers.UUIDField(required=True, help_text="PK for the product.")
    product_code = serializers.CharField(
        required=True, help_text="Unique code for the product."
    )
    product_name = serializers.CharField(
        required=True, help_text="Name of the product."
    )
    category_id = serializers.UUIDField(
        required=True, help_text="Foreign key of category."
    )

    sell_price = serializers.FloatField(
        required=True, help_text="Selling price of the product."
    )
    purchase_price = serializers.FloatField(
        required=True, help_text="Purchase price of the product."
    )


class ProductResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of product-related endpoints.
    """

    data = ProductDataSerializer(help_text="Product information.")
    errors = serializers.JSONField(
        help_text="Any errors message for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class ProductListDataSerializer(serializers.Serializer):
    """
    Serializer for the data field in product list response.
    """

    list = ProductDataSerializer(many=True, help_text="List of product records.")
    pagination = PaginationSerializer(
        help_text="Pagination information for the list of products."
    )


class ProductListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the product list endpoint.
    """

    data = ProductListDataSerializer(help_text="Products and pagination.")
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

product_sample_data = {
    "product_id": "0e7b4f91-c76e-4c63-b94c-ea7d51524fa1",
    "product_code": "BLUE-DELL-LATITUDE",
    "product_name": "Dell latitude",
    "category_id": "b4f792e2-d1be-4398-9fdf-5265539e1f71",
    "sell_price": 2.99,
    "purchase_price": 1.23,
}

product_create_success_example: OpenApiExample = get_create_success_example(
    name="Create Product - Success",
    data=product_sample_data,
)

product_list_success_example: OpenApiExample = get_list_success_example(
    name="List Product - Success",
    list_data=[product_sample_data],
)

product_get_by_id_success_example: OpenApiExample = get_by_id_success_example(
    name="Get Product by Id - Success",
    data=product_sample_data,
)

product_update_success_example: OpenApiExample = get_update_success_example(
    name="Update Product - Success",
    data=product_sample_data,
)

product_delete_success_example: OpenApiExample = get_delete_success_example(
    name="Delete Product - Success",
)
