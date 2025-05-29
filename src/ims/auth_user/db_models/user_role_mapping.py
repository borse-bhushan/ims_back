"""
This module defines the UserRoleMapping model, which is used to link users to roles.
"""

from django.db import models

from utils.functions import get_uuid
from base.db_models import BaseModel


class UserRoleMapping(BaseModel, models.Model):
    """
    Model to link users to roles.
    Useful for tracking user role mappings over time.
    """

    user_role_mapping_id = models.CharField(
        max_length=64, primary_key=True, default=get_uuid
    )
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    role = models.ForeignKey("Role", on_delete=models.CASCADE)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "user_role_mappings"

    def to_dict(self):
        """
        Convert the UserRoleMapping obj to dict.
        """
        return {
            "user_id": self.user_id,
            "role_id": self.role_id,
        }
