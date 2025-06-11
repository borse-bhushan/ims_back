"""
Permission Serializer for Swagger Documentation
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample

from utils.swagger import PaginationSerializer
from utils.swagger.common_swagger_functions import (
    get_delete_success_example,
    get_create_success_example,
    get_list_success_example,
)


class PermissionSwaggerSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a permission.
    """

    permission_id = serializers.CharField(
        read_only=True, help_text="Unique identifier for the permission."
    )
    name = serializers.CharField(required=True, help_text="Permission name")
    code = serializers.CharField(required=False, help_text="Permission code")
    module = serializers.CharField(required=True, help_text="Module name")
    action = serializers.CharField(
        required=True, help_text="Action this permission allows"
    )


class PermissionResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of permission-related endpoints.
    """

    data = PermissionSwaggerSerializer(help_text="Permission details.")
    errors = serializers.JSONField(help_text="Errors, if any", allow_null=True)
    messages = serializers.JSONField(
        help_text="Informational messages", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class PermissionListDataSerializer(serializers.Serializer):
    """
    Serializer for the data field in permission list response.
    """

    list = PermissionSwaggerSerializer(many=True, help_text="List of permissions")
    pagination = PaginationSerializer(help_text="Pagination info")


class PermissionListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the permission list endpoint.
    """

    data = PermissionListDataSerializer(help_text="Paginated permissions")
    errors = serializers.JSONField(help_text="Errors, if any", allow_null=True)
    messages = serializers.JSONField(help_text="Messages, if any", allow_null=True)
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# Swagger examples
permission_data_obj = {
    "name": "View User",
    "code": "view_user",
    "module": "User",
    "action": "view",
}
permission_create_success_example: OpenApiExample = get_create_success_example(
    name="Create Permission - Success",
    data=None,
)

permission_list_success_example: OpenApiExample = get_list_success_example(
    name="List Permissions - Success",
    list_data=[
        {
            **permission_data_obj,
            "permission_id": "9d018a56-abd9-4dfd-b606-80ce3ba8f53f",
        }
    ],
    pagination_data=False,
)

permission_delete_success_example: OpenApiExample = get_delete_success_example(
    "Delete Permission - Success"
)
