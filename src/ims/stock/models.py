"""
This model is used to store Stock information.
It inherits from the BaseModel class which contains common fields for all models.
"""

from django.db import models
from base.db_models import BaseModel
from stock.constants import StockMovementEnum
from utils.functions import get_uuid, create_stock_reference


class Stock(BaseModel, models.Model):
    """Represents a stock item within the system."""

    stock_id = models.CharField(primary_key=True, default=get_uuid, max_length=36)

    quantity = models.IntegerField(default=0)
    reference_number = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    movement_type = models.CharField(max_length=20, choices=StockMovementEnum.choices)

    product = models.ForeignKey("product.Product", on_delete=models.CASCADE)
    supplier = models.ForeignKey(
        "supplier.Supplier",
        null=True,
        default=None,
        on_delete=models.CASCADE,
    )

    class Meta:
        db_table = "stocks"

    def to_dict(self):
        """
        Convert the model instance to a dictionary.
        """
        return {
            "price": self.price,
            "stock_id": self.stock_id,
            "quantity": self.quantity,
            "product_id": self.product_id,
            "supplier_id": self.supplier_id,
            "movement_type": self.movement_type,
            "reference_number": self.reference_number,
        }

    def save(self, *args, **kwargs):
        """
        If the reference_number is not set, it will create a new one.
        """
        if not self.reference_number:
            self.reference_number = create_stock_reference(self.movement_type)
        super().save(*args, **kwargs)
