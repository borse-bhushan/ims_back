"""
Serializer for querying permission lists based on tenant ID.
"""

from rest_framework import serializers


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
