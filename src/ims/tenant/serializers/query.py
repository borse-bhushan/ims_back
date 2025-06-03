"""
Tenant Query Serializer
"""

from rest_framework import serializers

from base.serializers import QuerySerializer


class TenantQuerySerializer(QuerySerializer):
    """
    Serializer for querying tenants.
    """

    tenant_code = serializers.CharField(max_length=256, required=False)
    tenant_name = serializers.CharField(max_length=256, required=False)
