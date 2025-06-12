"""
Tenant Configuration Serializer and Swagger Examples
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample
from utils.swagger.common_swagger_functions import (
    get_create_success_example,
    get_by_id_success_example,
)
from tenant.constants import AuthenticationTypeEnum, DatabaseStrategyEnum


# ----------------------------------
# Serializers
# ----------------------------------


class TenantConfigurationDataSerializer(serializers.Serializer):
    """
    Serializer for creating and updating tenant configuration.
    """

    authentication_type = serializers.ChoiceField(
        choices=AuthenticationTypeEnum.choices,
        help_text="Authentication type (e.g., password, SAML, OIDC).",
    )
    database_strategy = serializers.ChoiceField(
        choices=DatabaseStrategyEnum.choices,
        default=DatabaseStrategyEnum.SHARED,
        help_text="Database Strategy type (e.g., Shared DB, Separate DB).",
    )


class TenantConfigurationResponseSerializer(serializers.Serializer):
    """
    Serializer for the response of tenant configuration endpoints.
    """

    data = TenantConfigurationDataSerializer(
        help_text="Tenant configuration information."
    )
    errors = serializers.JSONField(
        help_text="Any errors message for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# ----------------------------------
# Swagger Examples
# ----------------------------------

tenant_config_sample_data = {
    "database_strategy": DatabaseStrategyEnum.SHARED.name,
    "authentication_type": AuthenticationTypeEnum.JWT_TOKEN.name,
}

tenant_config_create_success_example: OpenApiExample = get_create_success_example(
    name="Create Tenant Configuration - Success",
    data=tenant_config_sample_data,
)

tenant_config_get_by_id_success_example: OpenApiExample = get_by_id_success_example(
    name="Get Tenant Configuration by Id - Success",
    data=tenant_config_sample_data,
)
