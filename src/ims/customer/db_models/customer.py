"""
This model is used to store customer information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models

from utils.functions import get_uuid
from base.db_models.model import BaseModel


class Customer(BaseModel, models.Model):
    """
    Customer model for the application.
    """

    customer_id = models.CharField(primary_key=True, max_length=64, default=get_uuid)

    customer_name = models.CharField(max_length=255)
    customer_desc = models.TextField(null=True, default=None)
    contact_phone = models.CharField(max_length=50, null=True, default=None)
    contact_person = models.CharField(max_length=255, null=True, default=None)
    contact_email = models.CharField(max_length=255, null=True, default=None)
    customer_code = models.CharField(max_length=100, null=True, default=None)

    class Meta:
        """
        db_table (str): Specifies the database table name for the model.
        """

        db_table = "customer"

    def to_dict(self):
        """
        Returns the dict with specific fields
        """
        return {
            "customer_id": self.customer_id,
            "customer_code": self.customer_code,
            "contact_phone": self.contact_phone,
            "contact_email": self.contact_email,
            "customer_name": self.customer_name,
            "customer_desc": self.customer_desc,
            "contact_person": self.contact_person,
        }
