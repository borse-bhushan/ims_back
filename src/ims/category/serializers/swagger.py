"""
Category Serializer and Swagger Examples
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


class CategoryDataSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a category.
    """

    category_id = serializers.UUIDField(required=True, help_text="PK for the category")
    category_code = serializers.CharField(
        required=True, help_text="Unique code for the category."
    )
    category_name = serializers.CharField(
        required=True, help_text="Name of the category."
    )


class CategoryResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of category-related endpoints.
    """

    data = CategoryDataSerializer(help_text="Category information.")
    errors = serializers.JSONField(
        help_text="Any errors message for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class CategoryListDataSerializer(serializers.Serializer):
    """
    Serializer for the data field in category list response.
    """

    list = CategoryDataSerializer(many=True, help_text="List of category records.")
    pagination = PaginationSerializer(
        help_text="Pagination information for the list of categories."
    )


class CategoryListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the category list endpoint.
    """

    data = CategoryListDataSerializer(help_text="Categories and pagination.")
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

category_sample_data = {
    "category_name": "Laptop",
    "category_code": "LAPTOP",
    "category_id": "23456789-abcd-efgh-ijkl-1234567890a2",
}
category_create_success_example: OpenApiExample = get_create_success_example(
    name="Create Category - Success",
    data=category_sample_data,
)

category_list_success_example: OpenApiExample = get_list_success_example(
    name="List Category - Success",
    list_data=[category_sample_data],
)

category_get_by_id_success_example: OpenApiExample = get_by_id_success_example(
    name="Get Category by Id - Success",
    data=category_sample_data,
)

category_update_success_example: OpenApiExample = get_update_success_example(
    name="Update Category - Success",
    data=category_sample_data,
)

category_delete_success_example: OpenApiExample = get_delete_success_example(
    name="Delete Category - Success",
)
