"""
Standard Swagger response schemas for consistent API documentation.
All responses follow the structure:
{
    "data": ...,
    "errors": [{"code": ..., "message": ..., "field": ...}],
    "messages": ...,
    "status_code": ...,
    "is_success": ...
}
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample
from utils.messages import error
from utils.exceptions import codes


class SuccessResponseSerializer(serializers.Serializer):
    """
    Standard response for successful requests.
    """

    data = serializers.JSONField(default=None)
    messages = serializers.DictField(
        help_text="Any informational messages for the response.",
        allow_null=True,
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class ErrorDetailSerializer(serializers.Serializer):
    """
    Standard error detail format.
    """

    code = serializers.CharField(
        help_text="Machine-readable error code, e.g., 'DUPLICATE_ENTRY'."
    )
    message = serializers.CharField(help_text="Human-readable error message.")
    field = serializers.CharField(help_text="Field where the error occurred.")


# === 400 Bad Request ===
class BadRequestResponseSerializer(serializers.Serializer):
    """
    Standard response for a bad request.
    """

    data = serializers.JSONField(default=None)
    errors = ErrorDetailSerializer(
        many=True, help_text="List of validation or business logic errors."
    )
    status_code = serializers.IntegerField(default=400)
    is_success = serializers.BooleanField(default=False)


responses_400_example = OpenApiExample(
    "400 Bad Request",
    value={
        "data": None,
        "errors": [
            {
                "code": codes.INVALID,
                "message": error.BAD_REQUEST,
                "field": "field_name",
            }
        ],
        "status_code": 400,
        "is_success": False,
    },
    response_only=True,
    status_codes=["400"],
)


# === 401 Unauthorized ===
class UnauthorizedResponseSerializer(serializers.Serializer):
    """
    Standard response for unauthorized access.
    """

    data = serializers.JSONField(default=None)
    errors = ErrorDetailSerializer(many=False, help_text="Unauthorized")
    status_code = serializers.IntegerField(default=401)
    is_success = serializers.BooleanField(default=False)


responses_401_example = OpenApiExample(
    "401 Unauthorized",
    value={
        "data": None,
        "errors": {
            "code": codes.UNAUTHORIZED,
            "message": error.UNAUTHORIZED_ACCESS,
        },
        "status_code": 401,
        "is_success": False,
    },
    response_only=True,
    status_codes=["401"],
)


# === 404 Not Found ===
class NotFoundResponseSerializer(serializers.Serializer):
    """Standard response for resource not found."""

    data = serializers.JSONField(default=None)
    errors = ErrorDetailSerializer(many=False, help_text="Resource not found.")
    status_code = serializers.IntegerField(default=404)
    is_success = serializers.BooleanField(default=False)


responses_404_example = OpenApiExample(
    "404 Not Found",
    value={
        "data": None,
        "errors": {
            "code": codes.NO_DATA_FOUND,
            "message": error.NO_DATA_FOUND,
        },
        "status_code": 404,
        "is_success": False,
    },
    response_only=True,
    status_codes=["404"],
)


# === 500 Internal Server Error ===
class InternalServerErrorResponseSerializer(serializers.Serializer):
    """Standard response for internal server error."""

    data = serializers.JSONField(default=None)
    errors = ErrorDetailSerializer(
        many=False, help_text="Unexpected internal server error."
    )
    status_code = serializers.IntegerField(default=500)
    is_success = serializers.BooleanField(default=False)


responses_500_example = OpenApiExample(
    "500 Internal Server Error",
    value={
        "data": None,
        "errors": {
            "code": codes.UNKNOWN_ERROR,
            "message": error.INTERNAL_SERVER_ERROR,
            "field": "",
        },
        "status_code": 500,
        "is_success": False,
    },
    response_only=True,
    status_codes=["500"],
)


class PaginationSerializer(serializers.Serializer):
    """
    Pagination for swagger documentation.
    """

    count = serializers.IntegerField()
    page_size = serializers.IntegerField()
    current_page = serializers.IntegerField()
    total_pages = serializers.IntegerField()


responses_200 = {"200": SuccessResponseSerializer()}

responses_400 = {"400": BadRequestResponseSerializer()}

responses_401 = {"401": UnauthorizedResponseSerializer()}

responses_404 = {"404": NotFoundResponseSerializer()}

responses_500 = {"500": InternalServerErrorResponseSerializer()}
