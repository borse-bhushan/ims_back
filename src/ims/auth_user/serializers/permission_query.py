"""
Serializer for querying permission lists based on tenant ID.
"""

from rest_framework import serializers

from utils.exceptions import codes
from utils.messages import error

from tenant.db_access import tenant_manager


class PermissionListQuerySerializer(serializers.Serializer):
    """
    Serializer for querying permission lists based on tenant ID.
    """

    tenant_id = serializers.UUIDField(required=True, allow_null=False)

    def to_internal_value(self, data):
        data = data.copy()

        tenant_id = data.get("tenant_id")

        if not tenant_id:
            data["tenant_id"] = None

        return super().to_internal_value(data)

    def validate_tenant_id(self, value):
        """
        Validates the tenant_id field.
        """
        if not value:
            raise serializers.ValidationError(
                self.error_messages["required"], code=codes.REQUIRED
            )

        if not tenant_manager.exists(query={"tenant_id": value}):
            raise serializers.ValidationError(
                error.NO_DATA_FOUND,
                code=codes.NO_DATA_FOUND,
            )

        return value
