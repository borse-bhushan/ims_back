"""
Swagger schemas for user-role mapping
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample

from utils.swagger import PaginationSerializer
from utils.swagger.common_swagger_functions import (get_delete_success_example,
                                                    get_create_success_example,
                                                    get_list_success_example)


class UserRoleSerializer(serializers.Serializer):
    """
    Serializer for creating user-role mapping.
    """

    user_id = serializers.UUIDField(help_text="User ID")
    role_id = serializers.UUIDField(help_text="Role ID")


class UserRoleResponseSerializer(serializers.Serializer):
    """
    Serializer for user-role mapping response.
    """

    data = UserRoleSerializer()
    errors = serializers.JSONField(help_text="Errors if any", allow_null=True)
    messages = serializers.JSONField(help_text="Messages if any", allow_null=True)
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class UserRoleListDataSerializer(serializers.Serializer):
    """
    Serializer for user-role mapping list response.
    """

    list = UserRoleSerializer(many=True)
    pagination = PaginationSerializer()


class UserRoleListResponseSerializer(serializers.Serializer):
    """
    Serializer for user-role mapping list response.
    """

    data = UserRoleListDataSerializer()
    errors = serializers.JSONField(help_text="Errors if any", allow_null=True)
    messages = serializers.JSONField(help_text="Messages if any", allow_null=True)
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# Swagger Examples
user_role_create_success_example: OpenApiExample = get_create_success_example(
    "Successful User-Role Mapping Creation",
    data={
        "user_id": "123e4567-e89b-12d3-a456-426614174000",
        "role_id": "789e4567-e89b-12d3-a456-426614174999",
    },
)
user_role_list_example_data = [
    {
        "user_id": "123e4567-e89b-12d3-a456-426614174000",
        "role_id": "789e4567-e89b-12d3-a456-426614174999",
    }
]
user_role_list_success_example: OpenApiExample = get_list_success_example(
    name="List User-Role Mappings - Success", list_data=user_role_list_example_data
)
user_role_delete_success_example: OpenApiExample = get_delete_success_example(
    "Delete Role - Success", "Deleted Successfully."
)
