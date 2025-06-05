"""
Serializer for user endpoints.
"""

from rest_framework import serializers


from utils.messages import error
from utils.exceptions import codes

from auth_user.db_access import user_manager

from ..constants import RoleEnum


class UserSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a user.
    """

    email = serializers.EmailField(required=True)
    profile_photo = serializers.CharField(required=False)
    phone_number = serializers.IntegerField(required=True)
    role_id = serializers.ChoiceField(choices=RoleEnum.choices)
    last_name = serializers.CharField(required=True, max_length=16)
    first_name = serializers.CharField(required=True, max_length=16)
    passwrod = serializers.CharField(required=True, max_length=16, min_length=4)

    def validate_email(self, value):
        """
        Validate email field.
        - For create: email must not exist.
        - For update: email must not belong to a different user.
        """

        is_update = self.instance is not None

        query = {"email": value}
        if is_update:
            query["user_id"] = {"NOT": self.instance.user_id}

        if user_manager.exists(query=query):
            raise serializers.ValidationError(
                error.ALREADY_EXIST,
                code=codes.DUPLICATE_ENTRY,
            )

        return value


class UserCompanyAdminSerializer(UserSerializer, serializers.Serializer):
    role_id = serializers.ChoiceField(
        choices=RoleEnum.choices,
        default=RoleEnum.COMPANY_ADMIN,
    )
    tenant_id = serializers.UUIDField()
