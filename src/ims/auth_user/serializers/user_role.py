"""
Serializer for user-role endpoints.
"""

from rest_framework import serializers

from utils.messages import error
from utils.exceptions import codes

from ..db_access import user_role_mapping_manager, user_manager, role_manager


class UserRoleSerializer(serializers.Serializer):
    """
    Serializer for creating user-role mapping.
    """

    role_id = serializers.UUIDField(required=True)
    user_id = serializers.UUIDField(required=True)

    def validate(self, attrs):
        """
        Validate user_role.
        - For create: user-role mapping must not exist.
        """

        if user_role_mapping_manager.exists(
            query={
                "role_id": attrs["role_id"],
                "user_id": attrs["user_id"],
            }
        ):
            raise serializers.ValidationError(
                {
                    "user_role": error.ALREADY_EXIST,
                },
                code=codes.DUPLICATE_ENTRY,
            )

        return attrs

    def validate_user_id(self, value):
        """
        Validate the given user ID. If the user ID does not exist in the database
        Raises serializers.ValidationError
        """
        if not user_manager.exists(query={"user_id": value}):
            raise serializers.ValidationError(
                error.NO_DATA_FOUND,
                code=codes.NO_DATA_FOUND,
            )
        return value

    def validate_role_id(self, value):
        """
        Validate the given role ID. If the role ID does not exist in the database
        Raises serializers.ValidationError
        """
        if not role_manager.exists(query={"role_id": value}):
            raise serializers.ValidationError(
                error.NO_DATA_FOUND,
                code=codes.NO_DATA_FOUND,
            )

        return value


class UserRoleListQuerySerializer(serializers.Serializer):
    """
    Serializer for Listing user-role mapping.
    """

    user_id = serializers.UUIDField(required=True)
