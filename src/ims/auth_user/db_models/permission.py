"""
Permission model to define actions like 'can_view_users', 'can_edit_users', etc.
Each permission is linked to a module and action.
"""

from django.db import models


from utils.functions import get_uuid
from base.db_models import BaseModel

from ..constants import MethodEnum


class Permission(BaseModel, models.Model):
    """
    Permission model to define actions like 'can_view_users', 'can_edit_users', etc.
    Each permission is linked to a module and action.
    """

    permission_id = models.CharField(max_length=64, primary_key=True, default=get_uuid)

    name = models.CharField(max_length=64)
    module = models.CharField(max_length=64)
    action = models.CharField(max_length=64, choices=MethodEnum.choices)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "permissions"

    def to_dict(self):
        """
        Convert Permission model instance to a dictionary representation.
        Returns:
            dict: A dictionary containing the permission details with the following keys:
                - name (str): The name of the permission
                - module (str): The module this permission belongs to
                - action (str): The action type of the permission
                - permission_id (int): The unique identifier of the permission
        """

        return {
            "name": self.name,
            "module": self.module,
            "action": self.action,
            "permission_id": self.permission_id,
        }
