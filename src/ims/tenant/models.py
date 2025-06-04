"""
This model is used to store tenant information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models
from utils.functions import get_uuid
from base.db_models import BaseModel

from .constants import AuthenticationTypeEnum


class Tenant(BaseModel, models.Model):
    """Represents a tenant organization within the system."""

    tenant_id = models.CharField(primary_key=True, default=get_uuid, max_length=36)

    tenant_code = models.CharField(max_length=256)
    tenant_name = models.CharField(max_length=256)

    class Meta:
        """
        Meta class for Tenant model.
        """

        db_table = "tenants"

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        """
        return {
            "tenant_id": self.tenant_id,
            "tenant_code": self.tenant_code,
            "tenant_name": self.tenant_name,
        }


class TenantConfiguration(BaseModel, models.Model):
    """Represents configuration settings for a tenant."""

    tenant_configuration_id = models.CharField(
        primary_key=True, default=get_uuid, max_length=36
    )

    authentication_type = models.CharField(
        max_length=56,
        default=AuthenticationTypeEnum.TOKEN,
        choices=AuthenticationTypeEnum.choices,
    )

    tenant = models.ForeignKey("Tenant", on_delete=models.CASCADE)

    class Meta:
        """
        Meta class for TenantConfiguration model.
        """

        db_table = "tenant_configurations"

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        """
        return {
            "tenant_id": self.tenant.tenant_id,
        }
