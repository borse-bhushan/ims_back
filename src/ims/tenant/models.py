"""
This model is used to store tenant information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models
from utils.functions import get_uuid
from base.db_models import BaseModel

from .constants import AuthenticationTypeEnum, DatabaseStrategyEnum


class Tenant(BaseModel, models.Model):
    """Represents a tenant organization within the system."""

    migrate_to_tenant = False

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

    migrate_to_tenant = False

    tenant_configuration_id = models.CharField(
        primary_key=True, default=get_uuid, max_length=36
    )

    authentication_type = models.CharField(
        max_length=56,
        default=AuthenticationTypeEnum.TOKEN,
        choices=AuthenticationTypeEnum.choices,
    )

    database_strategy = models.CharField(
        max_length=16,
        choices=DatabaseStrategyEnum.choices,
        default=DatabaseStrategyEnum.SHARED,
        help_text="Defines whether the tenant uses a shared or separate database.",
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
            "database_strategy": self.database_strategy,
            "authentication_type": self.authentication_type,
        }
