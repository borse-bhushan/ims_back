"""
User Serializer for Swagger Documentation
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample

from utils.swagger import PaginationSerializer
from utils.swagger.common_swagger_functions import (
    get_delete_success_example,
    get_update_success_example,
    get_create_success_example,
    get_list_success_example,
    get_by_id_success_example,
)


class UserDataSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a user.
    """

    user_id = serializers.UUIDField(required=True, help_text="PK for user model")
    email = serializers.EmailField(required=True, help_text="User's email address.")
    profile_photo = serializers.CharField(
        required=False, help_text="URL or path to the user's profile photo."
    )
    phone_number = serializers.IntegerField(
        required=True, help_text="User's phone number."
    )
    last_name = serializers.CharField(
        required=True, max_length=16, help_text="User's last name."
    )
    first_name = serializers.CharField(
        required=True, max_length=16, help_text="User's first name."
    )


class UserResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of user-related endpoints.
    """

    data = UserDataSerializer(help_text=" User Information.")
    errors = serializers.JSONField(
        help_text="Any errors message for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class UserListDataSerializer(serializers.Serializer):
    """
    Serializer for the data field in user list response.
    """

    list = UserDataSerializer(many=True, help_text="List of user records.")
    pagination = PaginationSerializer(
        help_text="Pagination information for the list of users."
    )


class UserListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the user list endpoint.
    """

    data = UserListDataSerializer(help_text="Users and pagination.")
    errors = serializers.JSONField(
        help_text="Any errors message for the response body.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# Swagger Examples
user_sample_data = {
    "email": "user@example.com",
    "user_id": "9d018a56-abd9-4dfd-b606-80ce3ba8f53f",
    "profile_photo": "https://cdn.example.com/photos/user.jpg",
    "phone_number": 9876543210,
    "first_name": "John",
    "last_name": "Doe",
    "full_name": "John Doe",
}
user_create_success_example: OpenApiExample = get_create_success_example(
    name="Create User - Success",
    data=user_sample_data,
)

user_list_success_example: OpenApiExample = get_list_success_example(
    name="List User - Success",
    list_data=[user_sample_data],
)
user_get_by_id_success_example: OpenApiExample = get_by_id_success_example(
    name="Get User by Id - Success",
    data=user_sample_data,
)
user_update_success_example = get_update_success_example(
    name="Update User - Success",
    data=user_sample_data,
)
user_delete_success_example: OpenApiExample = get_delete_success_example(
    "Delete User - Success",
)
