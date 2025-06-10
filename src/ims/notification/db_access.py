"""
This module contains the database access layer for notifications and user notifications.
It defines managers for the Notification and UserNotification models.
"""

from base.db_access import manager

from .models import Notification, UserNotification


class NotificationManager(manager.Manager[Notification]):
    """
    Manager class for the Notification model.
    """

    model = Notification


class UserNotificationManager(manager.Manager[UserNotification]):
    """
    Manager class for the UserNotification model.
    """

    model = UserNotification


notification_manager = NotificationManager()
user_notification_manager = UserNotificationManager()
