"""
Swagger documentation serializers and examples for RolePermission.
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample

from utils.swagger.common_swagger_functions import (
    get_create_success_example,
    get_list_success_example,
    get_delete_success_example,
)

from ..constants import RoleEnum


class RolePermissionSwaggerSerializer(serializers.Serializer):
    """
    Serializer for both creating a RolePermission.
    """

    role_id = serializers.ChoiceField(
        required=True, help_text="Role choice.", choices=RoleEnum.choices
    )
    permission_id = serializers.UUIDField(required=True, help_text="Permission UUID.")


class RolePermissionResponseSerializer(serializers.Serializer):
    """
    Response wrapper for RolePermission single object.
    """

    data = RolePermissionSwaggerSerializer(
        help_text="Role-Permission mapping information."
    )
    errors = serializers.JSONField(help_text="Errors if any.", allow_null=True)
    messages = serializers.JSONField(help_text="Messages if any.", allow_null=True)
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class RolePermissionListDataSerializer(serializers.Serializer):
    """
    Serializer for RolePermission list with pagination.
    """

    list = RolePermissionSwaggerSerializer(
        many=True, help_text="List of role-permission mappings."
    )
    pagination = serializers.JSONField(help_text="Pagination info.")


class RolePermissionListResponseSerializer(serializers.Serializer):
    """
    Response wrapper for RolePermission list.
    """

    data = RolePermissionListDataSerializer(
        help_text="List of RolePermission with pagination."
    )
    errors = serializers.JSONField(help_text="Errors if any.", allow_null=True)
    messages = serializers.JSONField(help_text="Messages if any.", allow_null=True)
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# Swagger Examples

role_permission_create_example: OpenApiExample = get_create_success_example(
    name="Create RolePermission - Success",
    data={
        "role_id": "123e4567-e89b-12d3-a456-426614174000",
        "permission_id": "987e6543-e21b-12d3-a456-426614174000",
    },
)

role_permission_list_example: OpenApiExample = get_list_success_example(
    name="List RolePermission - Success",
    list_data=[
        {
            "role_id": "123e4567-e89b-12d3-a456-426614174000",
            "permission_id": "987e6543-e21b-12d3-a456-426614174000",
        },
        {
            "role_id": "321e4567-e89b-12d3-a456-426614174000",
            "permission_id": "789e6543-e21b-12d3-a456-426614174000",
        },
    ],
)

role_permission_delete_example: OpenApiExample = get_delete_success_example(
    name="Delete RolePermission - Success",
)
