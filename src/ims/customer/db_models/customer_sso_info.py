"""
This model is used to store customer information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models

from utils.functions import get_uuid
from base.db_models.model import BaseModel

from ..constants import SSOProvideEnum, TenantIDEnum

from auth_user.constants import MethodEnum


class CustomerSSOInfo(BaseModel, models.Model):
    """
    Customer model for the application.
    """

    customer_sso_info_id = models.CharField(
        primary_key=True, max_length=64, default=get_uuid
    )

    sso_client_id = models.CharField(max_length=255, null=True, default=None)
    sso_client_secret = models.CharField(max_length=255, null=True, default=None)

    sso_token_timeout = models.IntegerField(null=True, default=None)
    scope = models.CharField(max_length=255, null=True, default=None)
    sso_path = models.CharField(max_length=255, null=True, default=None)
    grant_type = models.CharField(max_length=255, null=True, default=None)
    sso_domain = models.CharField(max_length=255, null=True, default=None)
    sso_token_path = models.CharField(max_length=255, null=True, default=None)

    response_type = models.CharField(max_length=255, null=True, default=None)
    response_mode = models.CharField(max_length=255, null=True, default=None)

    sso_tenant_id = models.CharField(max_length=255, choices=TenantIDEnum.choices)
    sso_provider = models.CharField(max_length=100, choices=SSOProvideEnum.choices)

    sso_callback_path = models.CharField(max_length=255, null=True, default=None)
    sso_callback_domain = models.CharField(max_length=255, null=True, default=None)

    sso_token_method_type = models.CharField(max_length=20, choices=MethodEnum.choices)
    sso_token_headers = models.JSONField(null=True, default=None)

    customer_domain = models.CharField(max_length=255, null=True, default=None)
    customer_sub_domain = models.CharField(max_length=255, null=True, default=None)

    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "customer_sso_info"

    def to_dict(self):
        """
        Returns the dict with specific fields
        """
        return {
            "scope": self.scope,
            "sso_path": self.sso_path,
            "sso_domain": self.sso_domain,
            "sso_provider": self.sso_provider,
            "response_type": self.response_type,
            "response_mode": self.response_mode,
            "sso_tenant_id": self.sso_tenant_id,
            "sso_client_id": self.sso_client_id,
            "sso_client_secret": self.sso_client_secret,
            "sso_token_headers": self.sso_token_headers,
            "sso_callback_path": self.sso_callback_path,
            "sso_callback_domain": self.sso_callback_domain,
            "sso_token_method_type": self.sso_token_method_type,
            "customer_sso_info_id": self.customer_sso_info_id,
        }
