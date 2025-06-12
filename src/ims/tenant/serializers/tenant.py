"""
Serializer for Tenant.
"""

from rest_framework import serializers

from utils.messages import error
from utils.exceptions import codes
from utils.validators import validate_unique

from ..db_access import tenant_manager
from ..constants import AuthenticationTypeEnum, DatabaseStrategyEnum


class TenantSerializer(serializers.Serializer):
    """Serializer for the Tenant model"""

    tenant_code = serializers.CharField(max_length=256)
    tenant_name = serializers.CharField(max_length=256)

    def get_query(self, field_name, value):
        """
        Generate a query dictionary for tenant field validation.
        This method constructs a query dictionary used to check uniqueness of tenant fields.
        For updates, it excludes the current tenant instance from the uniqueness check.
        Args:
            field_name (str): The name of the field to query
            value: The value to check for uniqueness
        Returns:
            dict: Query dictionary containing field name and value,
            with optional tenant_id exclusion for updates
        """

        is_update = self.instance is not None

        query = {field_name: value}
        if is_update:
            query["tenant_id"] = {"NOT": self.instance.tenant_id}

        return query

    def validate_tenant_code(self, value):
        """
        Validate tenant_code field.
        - For create: tenant_code must not exist.
        - For update: tenant_code must not belong to a different tenant.
        """

        validate_unique(tenant_manager, self.get_query("tenant_code", value))

        return value

    def validate_tenant_name(self, value):
        """
        Validate tenant_name field.
        - For create: tenant_name must not exist.
        - For update: tenant_name must not belong to a different tenant.
        """

        validate_unique(tenant_manager, self.get_query("tenant_name", value))

        return value


class TenantConfigurationSerializer(serializers.Serializer):
    """Serializer for Tenant Configuration"""

    authentication_type = serializers.ChoiceField(
        choices=AuthenticationTypeEnum.choices
    )

    database_strategy = serializers.ChoiceField(
        default=DatabaseStrategyEnum.SHARED,
        choices=DatabaseStrategyEnum.choices,
    )

    tenant_id = serializers.UUIDField()

    def validate_tenant_id(self, value):

        if not tenant_manager.exists({"tenant_id": value}):
            raise serializers.ValidationError(
                error.NO_DATA_FOUND,
                code=codes.NO_DATA_FOUND,
            )

        return value
