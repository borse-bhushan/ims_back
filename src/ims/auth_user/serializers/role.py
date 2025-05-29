"""
Serializer for role endpoints.
"""

from rest_framework import serializers

from utils.validators import validate_unique

from ..db_access import role_manager


class RoleSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a role.
    """

    role_code = serializers.CharField(required=True, max_length=16)
    display_name = serializers.CharField(required=True, max_length=16)

    def get_query(self, field_name, value):
        """
        Generate a query dictionary for role field validation.
        This method constructs a query dictionary used to check uniqueness of role fields.
        For updates, it excludes the current role instance from the uniqueness check.
        Args:
            field_name (str): The name of the field to query
            value: The value to check for uniqueness
        Returns:
            dict: Query dictionary containing field name and value, with optional role_id exclusion
                    for updates
        """

        is_update = self.instance is not None

        query = {field_name: value}
        if is_update:
            query["role_id"] = {"NOT": self.instance.role_id}

        return query

    def validate_role_code(self, value):
        """
        Validate role_code field.
        - For create: role_code must not exist.
        - For update: role_code must not belong to a different role.
        """

        validate_unique(role_manager, self.get_query("role_code", value))

        return value

    def validate_display_name(self, value):
        """
        Validate display_name field.
        - For create: display_name must not exist.
        - For update: display_name must not belong to a different role.
        """

        validate_unique(role_manager, self.get_query("display_name", value))

        return value
