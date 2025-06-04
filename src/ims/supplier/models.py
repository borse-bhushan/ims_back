"""
This model is used to store Supplier information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models
from utils.functions import get_uuid
from base.db_models import BaseModel


class Supplier(BaseModel, models.Model):
    """Represents a supplier within the system."""

    supplier_id = models.CharField(primary_key=True, default=get_uuid, max_length=36)

    supplier_code = models.CharField(max_length=256)
    supplier_name = models.CharField(max_length=256)

    class Meta:
        db_table = "suppliers"

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        """
        return {
            "supplier_id": self.supplier_id,
            "supplier_code": self.supplier_code,
            "supplier_name": self.supplier_name,
        }
