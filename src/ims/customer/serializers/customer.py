"""
Serializer for Customer.
"""

from rest_framework import serializers

from utils.validators import validate_unique

from ..db_access import customer_manager


class CreateCustomerSerializer(serializers.Serializer):
    """
    Serializer for creating a new customer.
    """

    customer_name = serializers.CharField(max_length=128)
    customer_code = serializers.CharField(max_length=128)

    def get_query(self, field_name, value):
        """
        Generate a query dictionary for customer field validation.
        For updates, it excludes the current customer instance from the uniqueness check.
        """
        is_update = self.instance is not None
        query = {field_name: value}
        if is_update:
            query["customer_id"] = {"NOT": self.instance.customer_id}
        return query

    def validate_customer_name(self, value):
        """
        Validate customer_name field using uniqueness.
        """
        validate_unique(customer_manager, self.get_query("customer_name", value))
        return value

    def validate_customer_code(self, value):
        """
        Validate customer_code field using uniqueness.
        """
        validate_unique(customer_manager, self.get_query("customer_code", value))
        return value
