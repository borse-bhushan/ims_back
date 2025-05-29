"""
Role model to store different roles like Admin, Editor, Viewer.
Roles can have types (e.g., Master, Standard) and can be assigned dynamically.
"""

from django.db import models

from utils.functions import get_uuid
from base.db_models import BaseModel


class Role(BaseModel, models.Model):
    __doc__ = """
    Role model to store different roles like Admin, Editor, Viewer.
    Roles can have types (e.g., Master, Standard) and can be assigned dynamically.
    """

    role_id = models.CharField(max_length=64, primary_key=True, default=get_uuid)
    role_code = models.CharField(max_length=64)
    display_name = models.CharField(max_length=64)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "roles"

    def to_dict(self):
        """
        Convert the Role object to a dictionary representation.
        Returns:
            dict: A dictionary containing the role attributes:
                - role_id: The unique identifier of the role
                - role_code: The code representing the role
                - display_name: The human-readable name of the role
        """

        return {
            "role_id": self.role_id,
            "role_code": self.role_code,
            "display_name": self.display_name,
        }
