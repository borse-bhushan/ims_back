"""
This model is used to store audit_logs information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models

from base.db_models.model import BaseModel
from utils.functions import get_uuid


class AuditLogs(BaseModel, models.Model):
    """
    Audit_logs model for the application.
    """

    audit_id = models.CharField(primary_key=True, max_length=64, default=get_uuid)

    extra_details = models.JSONField(null=True, default=None)
    request_headers = models.JSONField(null=True, default=None)
    user_id = models.CharField(max_length=64, null=True, default=None)
    client_ip = models.CharField(max_length=128, null=True, default=None)
    http_method = models.CharField(max_length=16, null=True, default=None)
    module_name = models.CharField(max_length=128, null=True, default=None)
    request_path = models.CharField(max_length=256, null=True, default=None)
    request_route = models.CharField(max_length=256, null=True, default=None)
    client_user_agent = models.CharField(max_length=128, null=True, default=None)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "audit_logs"

    def to_dict(self):
        """
        Returns the dict with specific fields
        """
        return {
            "audit_id": self.audit_id,
            "user_id": self.user_id,
            "client_ip": self.client_ip,
            "module_name": self.module_name,
            "http_method": self.http_method,
            "request_path": self.request_path,
            "extra_details": self.extra_details,
            "request_headers": self.request_headers,
            "client_user_agent": self.client_user_agent,
        }
