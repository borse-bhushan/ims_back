"""
Serializer for Address.
"""

import re  # Standard library
from rest_framework import serializers  # Third-party library
from ..constants import AddressType


class CreateAddressSerializer(serializers.Serializer):
    """
    Serializer for creating a new Address.
    """

    address_id = serializers.CharField(read_only=True, help_text="Unique identifier")
    address_line1 = serializers.CharField(help_text="First address.", required=True)
    address_line2 = serializers.CharField(help_text="Second address.")
    city = serializers.CharField(help_text="City of the address.", required=True)
    state_province_region = serializers.CharField(
        help_text="State of the address.", required=True
    )
    postal_code = serializers.CharField(
        help_text="Postal code of the address.", required=True
    )
    country_code = serializers.CharField(help_text="Country code of the address.")
    country_name = serializers.CharField(
        help_text="Country name of the address.", required=True
    )
    address_type = serializers.ChoiceField(
        choices=AddressType.choices,
        required=True,
        help_text="Type of address (Permanent, Current, Billing).",
    )

    def get_query(self, field_name, value):
        """
        Generate a query dictionary for address field validation.
        For updates, it excludes the current address instance from the uniqueness check.
        """
        is_update = self.instance is not None
        query = {field_name: value}
        if is_update:
            query["address_id"] = {"NOT": self.instance.address_id}
        return query

    def validate_address_line1(self, value):
        """
        Validate address line 1 to ensure it is not empty and does not exceed 255 characters.
        """
        if not value.strip():
            raise serializers.ValidationError("Address1 cannot be empty.")
        if len(value) > 255:
            raise serializers.ValidationError("Address1 is too long.")
        return value

    def validate_address_line2(self, value):
        """
        Validate address line 2 to ensure it does not exceed 255 characters.
        """
        if value == "":
            return None
        if value and len(value) > 255:
            raise serializers.ValidationError("Address2 is too long.")
        return value

    def validate_city(self, value):
        """
        Validate the city name to ensure it contains only letters,
        spaces, hyphens, periods, and apostrophes.
        """
        if value == "":
            return None
        if value and not re.match(r"^[a-zA-Z\s\-'.]+$", value):
            raise serializers.ValidationError(
                "City name must contain only letters and common symbols."
            )
        return value

    def validate_state_province_region(self, value):
        """
        Validate the state/province/region to ensure it contains only letters,
        spaces, hyphens, periods, and apostrophes.
        """
        if value == "":
            return None
        if value and not re.match(r"^[a-zA-Z\s\-'.]+$", value):
            raise serializers.ValidationError(
                "State/Province/Region must contain only letters and common symbols."
            )
        return value

    def validate_postal_code(self, value):
        """
        Validate the postal code to ensure it contains only alphanumeric characters,
        spaces, and dashes.
        """
        if value == "":
            return None
        if value and not re.match(r"^[0-9a-zA-Z\s\-]+$", value):
            raise serializers.ValidationError(
                "Postal code must contain only numbers, letters, and dashes."
            )
        return value

    def validate_country_name(self, value):
        """
        Validate the country name to ensure it contains only letters and common punctuation.
        """
        if value == "":
            return None
        if value and not re.match(r"^[a-zA-Z\s\-'.]+$", value):
            raise serializers.ValidationError(
                "Country name must contain only letters and common symbols."
            )
        return value
