"""
Tenant Domain Configuration Serializer and Swagger get_by_id Example
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample
from utils.swagger.common_swagger_functions import get_by_id_success_example


# ----------------------------------
# Serializer
# ----------------------------------


class TenantDomainConfigSerializer(serializers.Serializer):
    """
    Serializer for tenant domain configuration data.
    """

    host = serializers.CharField(
        help_text="Full host with port (e.g., localhost:8000)."
    )
    base_path = serializers.CharField(help_text="Base API path (e.g., api).")
    sub_domain = serializers.CharField(help_text="Subdomain name (e.g., ami).")
    api_host = serializers.CharField(
        help_text="Full API host URL including scheme (e.g., http://ami.localhost:8000)."
    )


class TenantDomainConfigResponseSerializer(serializers.Serializer):
    """
    Response serializer for tenant domain configuration endpoints.
    """

    data = TenantDomainConfigSerializer(
        help_text="Tenant domain configuration information."
    )
    errors = serializers.JSONField(
        help_text="Any error messages for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# ----------------------------------
# Swagger get_by_id Example
# ----------------------------------

tenant_domain_config_sample_data = {
    "host": "localhost:8000",
    "base_path": "api",
    "sub_domain": "ami",
    "api_host": "http://ami.localhost:8000",
}

tenant_domain_config_get_by_id_success_example: OpenApiExample = (
    get_by_id_success_example(
        name="Get Tenant Domain Configuration by Id - Success",
        data=tenant_domain_config_sample_data,
    )
)
