"""
Tenant Serializer and Swagger Examples
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


class TenantDataSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a tenant.
    """

    tenant_id = serializers.UUIDField(required=True, help_text="PK for the tenant.")
    tenant_code = serializers.CharField(
        max_length=256, help_text="Unique code for the tenant."
    )
    tenant_name = serializers.CharField(max_length=256, help_text="Name of the tenant.")


class TenantResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of tenant-related endpoints.
    """

    data = TenantDataSerializer(help_text="Tenant information.")
    errors = serializers.JSONField(
        help_text="Any errors message for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class TenantListDataSerializer(serializers.Serializer):
    """
    Serializer for the data field in tenant list response.
    """

    list = TenantDataSerializer(many=True, help_text="List of tenant records.")
    pagination = PaginationSerializer(
        help_text="Pagination information for the list of tenants."
    )


class TenantListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the tenant list endpoint.
    """

    data = TenantListDataSerializer(help_text="Tenants and pagination.")
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

tenant_sample_data = {
    "tenant_id": "f2e92c48-42c2-4a84-a5df-128471fba810",
    "tenant_code": "NEOSOFT",
    "tenant_name": "NeoSoft Technologies",
}

tenant_create_success_example: OpenApiExample = get_create_success_example(
    name="Create Tenant - Success",
    data=tenant_sample_data,
)

tenant_list_success_example: OpenApiExample = get_list_success_example(
    name="List Tenant - Success",
    list_data=[tenant_sample_data],
)

tenant_get_by_id_success_example: OpenApiExample = get_by_id_success_example(
    name="Get Tenant by Id - Success",
    data=tenant_sample_data,
)

tenant_update_success_example: OpenApiExample = get_update_success_example(
    name="Update Tenant - Success",
    data=tenant_sample_data,
)

tenant_delete_success_example: OpenApiExample = get_delete_success_example(
    name="Delete Tenant - Success",
)
