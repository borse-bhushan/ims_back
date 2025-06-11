"""
Supplier Serializer and Swagger Examples
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


class SupplierDataSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a supplier.
    """

    supplier_id = serializers.UUIDField(required=True, help_text="PK for the supplier.")
    supplier_code = serializers.CharField(
        required=True, help_text="Unique code for the supplier."
    )
    supplier_name = serializers.CharField(
        required=True, help_text="Name of the supplier."
    )


class SupplierResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of supplier-related endpoints.
    """

    data = SupplierDataSerializer(help_text="Supplier information.")
    errors = serializers.JSONField(
        help_text="Any errors message for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class SupplierListDataSerializer(serializers.Serializer):
    """
    Serializer for the data field in supplier list response.
    """

    list = SupplierDataSerializer(many=True, help_text="List of supplier records.")
    pagination = PaginationSerializer(
        help_text="Pagination information for the list of suppliers."
    )


class SupplierListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the supplier list endpoint.
    """

    data = SupplierListDataSerializer(help_text="Suppliers and pagination.")
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

supplier_sample_data = {
    "supplier_id": "9187cfc1-ccfb-4c7e-8fd1-98e57c9b0f00",
    "supplier_code": "DELL",
    "supplier_name": "Dell",
}

supplier_create_success_example: OpenApiExample = get_create_success_example(
    name="Create Supplier - Success",
    data=supplier_sample_data,
)

supplier_list_success_example: OpenApiExample = get_list_success_example(
    name="List Supplier - Success",
    list_data=[supplier_sample_data],
)

supplier_get_by_id_success_example: OpenApiExample = get_by_id_success_example(
    name="Get Supplier by Id - Success",
    data=supplier_sample_data,
)

supplier_update_success_example: OpenApiExample = get_update_success_example(
    name="Update Supplier - Success",
    data=supplier_sample_data,
)

supplier_delete_success_example: OpenApiExample = get_delete_success_example(
    name="Delete Supplier - Success",
)
