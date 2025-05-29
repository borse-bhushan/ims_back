"""
Role Serializer for Swagger Documentation
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample
from utils.swagger import PaginationSerializer
from utils.swagger.common_swagger_functions import (get_delete_success_example,
                                                    get_update_success_example,
                                                    get_create_success_example,
                                                    get_list_success_example,
                                                    get_by_id_success_example)


class RoleSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a role.
    """
    role_id = serializers.CharField(
        read_only=True, help_text="Unique identifier for the role."
    )
    role_code = serializers.CharField(
        required=True,
        max_length=16,
        help_text="Unique identifier for the role."
    )
    display_name = serializers.CharField(
        required=True,
        max_length=16,
        help_text="Human-readable name for the role."
    )


class RoleResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of role-related endpoints.
    """
    data = RoleSerializer(help_text="Role details.")
    errors = serializers.JSONField(help_text="Any errors for the response.", allow_null=True)
    messages = serializers.JSONField(help_text="Any informational messages.", allow_null=True)
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class RoleListDataSerializer(serializers.Serializer):
    """
    Serializer for the data field in role list response.
    """
    list = RoleSerializer(many=True, help_text="List of role records.")
    pagination = PaginationSerializer(help_text="Pagination information for the list of roles.")


class RoleListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the role list endpoint.
    """
    data = RoleListDataSerializer(help_text="Roles and pagination.")
    errors = serializers.JSONField(help_text="Any errors for the response.", allow_null=True)
    messages = serializers.JSONField(help_text="Any informational messages.", allow_null=True)
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# Swagger Examples

role_create_success_example:OpenApiExample=get_create_success_example(
    name="Create Role - Success",
    data= {
            "role_id": "9d018a56-abd9-4dfd-b606-80ce3ba8f53f",
            "role_code": "admin",
            "display_name": "Administrator"
        }
)

role_list_example_data = [
                   {
                    "role_id": "9d018a56-abd9-4dfd-b606-80ce3ba8f53f",
                    "role_code": "admin",
                    "display_name": "Administrator"
                },
                {
                    "role_id": "9d018a56-abd9-4dfd-b606-80ce3ba8f511",
                    "role_code": "user",
                    "display_name": "User"
                }
]
role_list_success_example:OpenApiExample=get_list_success_example(
    name="List Role - Success",
    list_data = role_list_example_data,
)
role_get_by_id_success_example:OpenApiExample=get_by_id_success_example(
    name="Get Role by Id - Success",
        data={
            "role_id": "9d018a56-abd9-4dfd-b606-80ce3ba8f53f",
            "role_code": "admin",
            "display_name": "Administrator"
        }
)
role_update_success_example = get_update_success_example(
    name="Update Role - Success",
    data={
            "role_id": "9d018a56-abd9-4dfd-b606-80ce3ba8f53f",
            "role_code": "admin",
            "display_name": "Admin Updated"
        }
)
role_delete_success_example: OpenApiExample = get_delete_success_example(
    "Delete Role - Success",
    "Deleted Successfully."
)
