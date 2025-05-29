"""
This model is used to store file information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models

from base.db_models.model import BaseModel
from utils.functions import get_uuid


class File(BaseModel, models.Model):
    """
    File model for the application.
    """

    file_id = models.CharField(primary_key=True, max_length=64, default=get_uuid)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    file_size = models.BigIntegerField(blank=True, null=True)
    file_path = models.CharField(max_length=1000, blank=True, null=True)
    mime_type = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "file"

    def to_dict(self):
        """
        Returns the dict with specific fields
        """
        return {
            "file_id": self.file_id,
            "file_name": self.file_name,
            "file_size": self.file_size,
            "file_path": self.file_path,
            "mime_type": self.mime_type,
        }
