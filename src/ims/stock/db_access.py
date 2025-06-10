"""
Stock manager module.
This module contains the StockManager class, which is responsible for managing
the Stock model.
It provides methods for creating, updating, deleting, and retrieving Stock records.
"""

from django.dispatch import receiver
from django.db.models.signals import post_save

from base.db_access import manager
from notification.constants import NotificationTypeEnum
from notification.utils.helpers import SendNotification

from auth_user.constants import RoleEnum
from auth_user.db_access import user_manager

from .models import Stock
from .constants import StockMovementEnum


class StockManager(manager.Manager[Stock]):
    """
    Manager class for the Stock model.
    """

    model = Stock

    @staticmethod
    @receiver(post_save, sender=Stock)
    def send_notification_on_stock_movement(sender, instance: Stock, created, **kwargs):
        """
        Signal receiver that sends a notification when a Stock instance is created.
        """

        if not created:
            return None

        notification_type = None

        if instance.movement_type == StockMovementEnum.IN:
            notification_type = NotificationTypeEnum.STOCK_IN
        elif instance.movement_type == StockMovementEnum.OUT:
            notification_type = NotificationTypeEnum.STOCK_OUT

        SendNotification(
            title="Stock Movement",
            message=f"Stock {instance.reference_number} has been created",
            created_by=instance.created_by,
            notification_type=notification_type,
            notification_data={
                "stock_id": instance.stock_id,
            },
        ).send(
            recipient_list=user_manager.list(
                query={
                    "role_id": RoleEnum.COMPANY_ADMIN,
                },
            )
        )


stock_manager = StockManager()
