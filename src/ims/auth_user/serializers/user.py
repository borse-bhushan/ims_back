"""
Serializer for user endpoints.
"""

from rest_framework import serializers


from utils.messages import error
from utils.exceptions import codes

from tenant.db_access import tenant_manager
from tenant.utils.tenant_conf import get_tenant_db_name

from ..constants import RoleEnum
from ..db_access import user_manager


class UserSerializer(serializers.Serializer):
    """
    Serializer for both creating and updating a user.
    """

    email = serializers.EmailField(required=True)
    phone_number = serializers.IntegerField(required=True)
    role_id = serializers.ChoiceField(choices=RoleEnum.choices)
    last_name = serializers.CharField(required=True, max_length=16)
    first_name = serializers.CharField(required=True, max_length=16)
    profile_photo = serializers.FileField(
        required=False, allow_empty_file=True, allow_null=True
    )
    password = serializers.CharField(required=True, max_length=16, min_length=4)

    def validate_email(self, value, **kwargs):
        """
        Validate email field.
        - For create: email must not exist.
        - For update: email must not belong to a different user.
        """

        is_update = self.instance is not None

        query = {"email": value}
        if is_update:
            query["user_id"] = {"NOT": self.instance.user_id}

        if user_manager.exists(query=query, using=kwargs.get("using")):
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

    def validate_role_id(self, value):
        if value != RoleEnum.COMPANY_ADMIN:
            raise serializers.ValidationError(
                code=codes.INVALID_CHOICE,
                detail=error.ALLOWD_ROLE.format(roles=RoleEnum.COMPANY_ADMIN.value),
            )
        return value

    def validate_tenant_id(self, value):

        if not tenant_manager.exists({"tenant_id": value}):
            raise serializers.ValidationError(
                error.NO_DATA_FOUND,
                code=codes.NO_DATA_FOUND,
            )
        return value

    def validate_email(self, value):
        """
        Validate email field.
        - For create: email must not exist.
        - For update: email must not belong to a different user.
        """

        db_name = get_tenant_db_name(self.initial_data.get("tenant_id"))
        return super().validate_email(value, using=db_name)
