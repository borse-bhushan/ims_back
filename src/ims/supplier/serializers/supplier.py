"""
Serializer for Supplier.
"""

from rest_framework import serializers

from utils.validators import validate_unique

from ..db_access import supplier_manager


class SupplierSerializer(serializers.Serializer):
    """Serializer for the Supplier model"""

    supplier_code = serializers.CharField(max_length=256)
    supplier_name = serializers.CharField(max_length=256)

    def get_query(self, field_name, value):
        """
        Generate a query dictionary for supplier field validation.
        This method constructs a query dictionary used to check uniqueness of supplier fields.
        For updates, it excludes the current supplier instance from the uniqueness check.
        Args:
            field_name (str): The name of the field to query
            value: The value to check for uniqueness
        Returns:
            dict: Query dictionary containing field name and value,
            with optional supplier_id exclusion for updates
        """

        is_update = self.instance is not None

        query = {field_name: value}
        if is_update:
            query["supplier_id"] = {"NOT": self.instance.supplier_id}

        return query

    def validate_supplier_code(self, value):
        """
        Validate supplier_code field.
        - For create: supplier_code must not exist.
        - For update: supplier_code must not belong to a different supplier.
        """

        validate_unique(supplier_manager, self.get_query("supplier_code", value))

        return value

    def validate_supplier_name(self, value):
        """
        Validate supplier_name field.
        - For create: supplier_name must not exist.
        - For update: supplier_name must not belong to a different supplier.
        """

        validate_unique(supplier_manager, self.get_query("supplier_name", value))

        return value
