"""
This model is used to store address information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models

from base.db_models.model import BaseModel
from utils.functions import get_uuid
from ..constants import AddressType


class Address(BaseModel, models.Model):
    """
    Address model for the application.
    """

    address_id = models.CharField(primary_key=True, max_length=64, default=get_uuid)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, null=True, default=None)
    city = models.CharField(max_length=100, null=True, default=None)
    state_province_region = models.CharField(max_length=100, null=True, default=None)
    postal_code = models.CharField(max_length=20, null=True, default=None)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=100, null=True, default=None)
    address_type = models.CharField(max_length=64, choices=AddressType.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "addresses"

    def to_dict(self):
        """
        Returns the dict with specific fields
        """
        return {
            "address_id": self.address_id,
            "address_line1": self.address_line1,
            "address_line2": self.address_line2,
            "country_code": self.country_code,
            "country_name": self.country_name,
            "city": self.city,
            "state_province_region": self.state_province_region,
            "postal_code": self.postal_code,
            "address_type": self.address_type,
        }
