from django.db.models import TextChoices


class StockMovementEnum(TextChoices):
    """
    Constants for stock movement.
    """

    IN = "IN", "In"
    OUT = "OUT", "Out"
