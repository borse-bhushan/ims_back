"""
This module defines the Notification model for the system.
"""

from django.db import models

from base.db_models import BaseModel
from utils.functions import get_uuid

from .constants import NotificationType


class Notification(BaseModel, models.Model):
    """
    Represents a notification in the system.
    """

    notification_id = models.CharField(
        primary_key=True, max_length=64, default=get_uuid
    )

    message = models.TextField()
    title = models.CharField(max_length=255)

    notification_type = models.CharField(
        max_length=32,
        default=NotificationType.IN,
        choices=NotificationType.choices,
    )

    def __str__(self):
        return f"Notification[{self.title} - {self.message[:10]}...]"

    class Meta:
        db_table = "notifications"

    def to_dict(self):
        """
        Convert the Notification instance to a dictionary.
        """
        return {
            "title": self.title,
            "message": self.message,
            "notification_id": self.notification_id,
            "notification_type": self.notification_type,
        }


class UserNotification(BaseModel, models.Model):
    """
    Represents a user notification in the system.
    """

    user_notification_id = models.CharField(
        primary_key=True, max_length=64, default=get_uuid
    )

    is_read = models.BooleanField(default=False)
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    notification = models.ForeignKey("Notification", on_delete=models.CASCADE)

    def __str__(self):
        return f"UserNotification[{self.user_id} - {self.notification.title}]"

    class Meta:
        db_table = "user_notifications"

    def to_dict(self):
        """
        Convert the UserNotification instance to a dictionary.
        """

        return {
            "user_id": self.user_id,
            "is_read": self.is_read,
            "notification": self.notification.to_dict(),
        }
