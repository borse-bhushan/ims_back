"""
This model is used to store Product information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models
from utils.functions import get_uuid
from base.db_models import BaseModel


class Product(BaseModel, models.Model):
    """Represents a product within the system."""

    product_id = models.CharField(primary_key=True, default=get_uuid, max_length=36)

    product_code = models.CharField(max_length=256)
    product_name = models.CharField(max_length=256)
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    category = models.ForeignKey("category.Category", on_delete=models.CASCADE)

    class Meta:
        db_table = "products"

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        """
        return {
            "product_id": self.product_id,
            "sell_price": self.sell_price,
            "category_id": self.category_id,
            "product_code": self.product_code,
            "product_name": self.product_name,
            "purchase_price": self.purchase_price,
        }
