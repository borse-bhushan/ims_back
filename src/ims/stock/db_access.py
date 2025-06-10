"""
Stock manager module.
This module contains the StockManager class, which is responsible for managing
the Stock model.
It provides methods for creating, updating, deleting, and retrieving Stock records.
"""

from django.db.models import Sum
from django.dispatch import receiver
from django.db.models.signals import post_save

from base.db_access import manager
from notification.constants import NotificationTypeEnum
from notification.utils.helpers import SendNotification

from auth_user.constants import RoleEnum
from auth_user.db_access import user_manager

from utils.messages import notifications

from .models import Stock
from .constants import StockMovementEnum


class StockManager(manager.Manager[Stock]):
    """
    Manager class for the Stock model.
    """

    model = Stock

    @staticmethod
    @receiver(post_save, sender=Stock)
    def send_notification_on_stock_movement(sender, instance: Stock, created, **__):
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

        if notification_type is None:
            return None

        SendNotification(
            title=notifications.STOCK_MOVEMENT_TITLE,
            message=notifications.STOCK_MOVEMENT_MESSAGE.format(
                quantity=instance.quantity,
                reference_number=instance.reference_number,
                movement_type=instance.get_movement_type_display(),
            ),
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

    def get_stock_summary(self, query):
        """
        Get stock summary.
        Returns a dictionary with the total quantity of stock.
        """

        return (
            self._parse_query(query)
            .values("product_id", "movement_type")
            .annotate(total_quantity=Sum("quantity"))
        )


stock_manager = StockManager()
