"""
This model is used to store category information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models
from utils.functions import get_uuid
from base.db_models import BaseModel


class Category(BaseModel, models.Model):
    """Represents a category within the system."""

    category_id = models.CharField(primary_key=True, default=get_uuid, max_length=36)

    category_code = models.CharField(max_length=256)
    category_name = models.CharField(max_length=256)

    class Meta:
        db_table = "categories"

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        """
        return {
            "category_id": self.category_id,
            "category_code": self.category_code,
            "category_name": self.category_name,
        }
