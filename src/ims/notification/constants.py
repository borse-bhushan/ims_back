from django.db.models import TextChoices


class NotificationTypeEnum(TextChoices):
    """
    Enum for notification types.
    """

    STOCK_IN = "STOCK_IN", "Stock In"
    STOCK_OUT = "STOCK_OUT", "Stock Out"
    STOCK_NOT_AVAILABLE = "STOCK_NOT_AVAILABLE", "Stock Not Available"
