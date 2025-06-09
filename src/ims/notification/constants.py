from django.db.models import TextChoices


class NotificationType(TextChoices):
    """
    Enum for notification types.
    """

    IN = "IN", "Stock In"
    OUT = "OUT", "Stock Out"
    ALERT = "NOT_AVAILABLE", "Not Available"

