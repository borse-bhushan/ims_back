"""
Serializer for Permission endpoints.
"""

from rest_framework import serializers

from utils.messages import error
from utils.exceptions import codes

from ..db_access import permission_manager
from ..constants import MethodEnum


class PermissionSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a Permission.
    """

    name = serializers.CharField(required=True, max_length=64)
    module = serializers.CharField(required=True, max_length=64)
    action = serializers.ChoiceField(
        required=True,
        choices=MethodEnum.choices,
    )

    def validate(self, attrs):
        """
        Validates the permission attributes to ensure no duplicate module-action combination exists.
        Args:
            attrs (dict): Dictionary containing 'module' and 'action' fields to validate
        Returns:
            dict: The validated attribute dictionary if validation passes
        Raises:
            ValidationError: If permission with same module-action combination already exists
        """

        module = attrs.get("module")
        action = attrs.get("action")

        if module and action:
            query = {
                "module": module,
                "action": action,
            }

            is_update = self.instance is not None
            if is_update:
                query["permission_id"] = {"NOT": self.instance.permission_id}

            permission_obj = permission_manager.get(query=query)
            if permission_obj:
                raise serializers.ValidationError(
                    {
                        "module_action": error.ALREADY_EXIST,
                    },
                    code=codes.DUPLICATE_ENTRY,
                )

        return attrs
