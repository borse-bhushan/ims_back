"""
Module providing serializers and OpenAPI examples for address endpoints.
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
from ..constants import AddressType


class AddressDataSerializer(serializers.Serializer):
    """
    Serializer for address data structure.
    """

    address_id = serializers.CharField(
        read_only=True, help_text="Unique identifier for the address."
    )
    address_line1 = serializers.CharField(help_text="First line of the address.")
    address_line2 = serializers.CharField(
        help_text="Second line of the address.",
    )
    city = serializers.CharField(
        help_text="City of the address.",
    )
    state_province_region = serializers.CharField(
        help_text="State, province, or region of the address."
    )
    postal_code = serializers.CharField(help_text="Postal code of the address.")
    country_code = serializers.CharField(
        help_text="Country code of the address (e.g., 'IN')."
    )
    country_name = serializers.CharField(help_text="Full country name of the address.")
    primary_type = serializers.ChoiceField(
        choices=AddressType.choices,
        help_text="Type of primary address (Permanent, Current, Billing).",
    )


class AddressDataListSerializer(serializers.Serializer):
    """
    Serializer for the data list of address.
    """

    list = AddressDataSerializer(many=True, help_text="List of address.")
    pagination = PaginationSerializer(
        help_text="Pagination information for the list of address."
    )


class AddressListResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the address list endpoint.
    """

    data = AddressDataListSerializer(
        help_text="List of address with pagination information."
    )
    errors = serializers.JSONField(
        help_text="Any errors for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class AddressResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of the address list endpoint.
    """

    data = AddressDataSerializer(help_text="Address information.")
    errors = serializers.JSONField(
        help_text="Any errors for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


address_create_success_example: OpenApiExample = get_create_success_example(
    "Successful Address Creation",
    data={
        "address_id": "950284d6-43e1-498e-a1ce-6af1b90388a4",
        "address_line1": "Arera colony Bhopal",
        "address_line2": "Arera colony road area Bhopal",
        "country_code": "IN",
        "country_name": "India",
        "city": "Paris",
        "state_province_region": "MP",
        "postal_code": "462016",
        "address_type": "PERMANENT",
    },
)
address_getById_success_example: OpenApiExample = get_by_id_success_example(
    name="Get Address by Id - Success",
    data={
        "address_id": "5fabc6e8-36b0-4b50-a0e4-ee164979d4ea",
        "address_line1": "123 Main St",
        "address_line2": "Apt 4B",
        "country_code": "IN",
        "country_name": "India",
        "city": "New York",
        "state_province_region": "NY",
        "postal_code": "10001",
        "address_type": "CURRENT",
    },
)
address_list_example_data = [
    {
        "address_id": "1a2b3c4d-1234-5678-9101-abcdefabcdef",
        "address_line1": "123 Main St",
        "address_line2": "Apt 4B",
        "country_code": "IN",
        "country_name": "India",
        "city": "New York",
        "state_province_region": "NY",
        "postal_code": "10001",
        "address_type": "CURRENT",
    },
    {
        "address_id": "2b3c4d5e-2345-6789-1011-bcdefabcdefa",
        "address_line1": "456 Elm St",
        "address_line2": "Suite 5A",
        "country_code": "IN",
        "country_name": "India",
        "city": "Los Angeles",
        "postal_code": "90001",
        "address_type": "CURRENT",
    },
]
address_list_success_example: OpenApiExample = get_list_success_example(
    name="List Address - Success",
    list_data=address_list_example_data,
)
address_update_success_example: OpenApiExample = get_update_success_example(
    name="Update Address - Success",
    data={
        "address_id": "5fabc6e8-36b0-4b50-a0e4-ee164979d4ea",
        "address_line1": "123 Main St",
        "address_line2": "Apt 4B",
        "country_code": "IN",
        "country_name": "India",
        "city": "New York",
        "postal_code": "10001",
        "address_type": "CURRENT",
    },
)
address_delete_success_example: OpenApiExample = get_delete_success_example(
    "Delete Address - Success", "Deleted Successfully."
)
