"""
User related models
"""

from django.db import models

from utils.functions import get_uuid
from base.db_models import BaseModel

from auth_user.constants import RoleEnum


class RolePermissionMapping(BaseModel, models.Model):
    """
    Model to link roles to permissions.
    Useful for tracking role permissions mapping over time.
    """

    role_permission_mapping_id = models.CharField(
        max_length=64, primary_key=True, default=get_uuid
    )

    role_id = models.CharField(choices=RoleEnum.choices, max_length=64)
    permission = models.ForeignKey("Permission", on_delete=models.CASCADE)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "role_permission_mappings"

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        Returns:
            dict: Dictionary representation of the model instance.
        """
        return {
            "role_id": self.role_id,
            "permission_id": self.permission_id,
        }
