"""
Address constants module.
"""

from django.db import models


class AddressType(models.TextChoices):
    """
    Enum for address type.
    """

    PERMANENT = "PERMANENT", "Permanent"
    CURRENT = "CURRENT", "Current"
    BILLING = "BILLING", "Billing"
