from rest_framework import serializers

from base.serializers import QuerySerializer

from ..constants import RoleEnum


class UserListQuerySerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class UserCompanyAdminListQuerySerializer(
    QuerySerializer,
    UserListQuerySerializer,
    serializers.Serializer,
):
    tenant_id = serializers.UUIDField(required=True)
    role_id = serializers.ChoiceField(
        choices=RoleEnum.choices,
        default=RoleEnum.COMPANY_ADMIN,
    )

    def to_internal_value(self, data):
        data = data.copy()
        tenant_id = data.get("tenant_id")

        if not tenant_id:
            data["tenant_id"] = None

        data["role_id"] = RoleEnum.COMPANY_ADMIN

        data = QuerySerializer.to_internal_value(self, data)

        return data
