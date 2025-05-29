"""
Module providing serializers and OpenAPI examples for login and logout endpoints.
"""

from rest_framework import serializers, status
from drf_spectacular.utils import OpenApiExample

from utils.messages import error
from utils.exceptions import codes


class CommonFields:
    """
    Common fields used across various serializers for standardized response formatting.
    Attributes:
        status_code (IntegerField): HTTP status code of the response, defaults to 201
        is_success (BooleanField): Flag indicating if the operation was successful, defaults to True
    """

    status_code = serializers.IntegerField(default=201)
    is_success = serializers.BooleanField(default=True)


class LoginTokenDataSerializer(serializers.Serializer):
    """
    A serializer for handling login token response data.
    Serializes an authentication token and its creation timestamp.
    Attributes:
        token (str): The authentication token string.
        created_dtm (datetime): The timestamp when the token was created.
    """

    token = serializers.CharField(help_text="Authentication token.")
    created_dtm = serializers.DateTimeField(help_text="Token creation timestamp.")


class LoginResponseSerializer(CommonFields, serializers.Serializer):
    """
    A serializer for handling login response data.
    This serializer represents the structure of the response returned after a login attempt.
    Attributes:
        data (LoginTokenDataSerializer): Contains login data including authentication token.
        errors (JSONField): JSON field for any error messages that occurred during login.
            Defaults to null if no errors.
        messages (JSONField): JSON field for any informational messages.
            Defaults to null if no messages.
        status_code (IntegerField): HTTP status code for the response.
            Defaults to 201.
        is_success (BooleanField): Flag indicating if the login was successful.
            Defaults to True.
    """

    data = LoginTokenDataSerializer(help_text="Login data with token.")
    errors = serializers.JSONField(allow_null=True, help_text="Any errors.")
    messages = serializers.JSONField(
        allow_null=True, help_text="Informational messages."
    )


login_success_example = OpenApiExample(
    name="Login Successful",
    value={
        "data": {
            "token": "BABD5D130CB04C05717D5D22635BBE4D",
            "created_dtm": "2025-04-18T07:25:20.135018Z",
        },
        "errors": None,
        "messages": {"message": "Logged in successful."},
        "status_code": status.HTTP_201_CREATED,
        "is_success": True,
    },
    response_only=True,
    status_codes=[str(status.HTTP_201_CREATED)],
)


# === 401 Wrong Credentials ===
class WrongCredentialsSerialize(CommonFields, serializers.Serializer):
    """
    Standard response for unauthorized access.
    """

    data = serializers.JSONField(default=None)
    errors = serializers.JSONField(help_text="Unauthorized")


responses_401_example = OpenApiExample(
    "401 WrongCredentials",
    value={
        "data": None,
        "errors": {
            "code": codes.UNAUTHORIZED,
            "message": error.UNAUTHORIZED_ACCESS,
        },
        "status_code": status.HTTP_401_UNAUTHORIZED,
        "is_success": False,
    },
    response_only=True,
    status_codes=[str(status.HTTP_401_UNAUTHORIZED)],
)


class LogoutResponseSerializer(CommonFields, serializers.Serializer):
    """
    A serializer for handling logout response data.
    This serializer represents the structure of the response returned after a logout attempt.
    Attributes:
        data (JSONField): Contains logout data, typically null.
        errors (JSONField): JSON field for any error messages that occurred during logout.
            Defaults to null if no errors.
        messages (JSONField): JSON field for any informational messages.
            Defaults to null if no messages.
        status_code (IntegerField): HTTP status code for the response.
            Defaults to 201.
        is_success (BooleanField): Flag indicating if the logout was successful.
            Defaults to True.
    """

    data = serializers.JSONField(
        allow_null=True, help_text="Logout data, null on success."
    )
    errors = serializers.JSONField(
        allow_null=True, help_text="Any errors, null if none."
    )
    messages = serializers.JSONField(
        allow_null=True, help_text="Informational messages."
    )


logout_success_example = OpenApiExample(
    name="Logout Successful",
    value={
        "data": None,
        "errors": None,
        "messages": {"message": "Logged out successfully."},
        "status_code": status.HTTP_204_NO_CONTENT,
        "is_success": True,
    },
    response_only=True,
    status_codes=[str(status.HTTP_204_NO_CONTENT)],
)
