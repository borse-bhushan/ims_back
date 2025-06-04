"""
Serializer for Category.
"""

from rest_framework import serializers

from utils.validators import validate_unique

from ..db_access import category_manager


class CategorySerializer(serializers.Serializer):
    """Serializer for the Category model"""

    category_code = serializers.CharField(max_length=256)
    category_name = serializers.CharField(max_length=256)

    def get_query(self, field_name, value):
        """
        Generate a query dictionary for category field validation.
        This method constructs a query dictionary used to check uniqueness of category fields.
        For updates, it excludes the current category instance from the uniqueness check.
        Args:
            field_name (str): The name of the field to query
            value: The value to check for uniqueness
        Returns:
            dict: Query dictionary containing field name and value,
            with optional category_id exclusion for updates
        """

        is_update = self.instance is not None

        query = {field_name: value}
        if is_update:
            query["category_id"] = {"NOT": self.instance.category_id}

        return query

    def validate_category_code(self, value):
        """
        Validate category_code field.
        - For create: category_code must not exist.
        - For update: category_code must not belong to a different category.
        """

        validate_unique(category_manager, self.get_query("category_code", value))

        return value

    def validate_category_name(self, value):
        """
        Validate category_name field.
        - For create: category_name must not exist.
        - For update: category_name must not belong to a different category.
        """

        validate_unique(category_manager, self.get_query("category_name", value))

        return value
