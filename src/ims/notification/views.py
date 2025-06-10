"""
Notification ViewSet
This module contains the NotificationViewSet class, which is responsible for
handling HTTP requests related to notifications.
"""

from rest_framework import viewsets, status

from utils.messages import success
from utils.response import generate_response
from utils.exceptions import ValidationError, NoDataFoundError

from auth_user.constants import MethodEnum
from base.views.base import UpdateView, ListView
from authentication import register_permission, get_authentication_classes


from .db_access import user_notification_manager
from .serializers import NotificationMarkAsReadSerializer

MODULE = "Notification"


class NotificationViewSet(UpdateView, ListView, viewsets.ViewSet):
    """
    ViewSet for managing invoices.
    """

    manager = user_notification_manager
    serializer_class = NotificationMarkAsReadSerializer

    get_authenticators = get_authentication_classes

    @classmethod
    def get_method_view_mapping(cls):
        """
        Returns a dictionary mapping HTTP methods to their corresponding view methods.
        """
        return {
            **ListView.get_method_view_mapping(),
            **UpdateView.get_method_view_mapping(),
        }

    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.PUT, f"Make {MODULE} mark as read")
    def update(self, request, *args, **kwargs):
        """
        This function will make  is_read flag false -> true so the notification will be mark as read and wont
        be seen in the notification list.
        """
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            raise ValidationError(serializer.errors)

        validated_data = serializer.validated_data

        query = {
            "is_read": False,
            "user_id": request.user.user_id,
        }

        if not validated_data.get("mark_all_as_read"):
            query["notification_id__in"] = validated_data.get("list_notification_id")

        count = user_notification_manager.count(query=query)

        if not count:
            raise NoDataFoundError()

        user_notification_manager.update(data={"is_read": True}, query=query)

        return generate_response(
            status_code=status.HTTP_200_OK,
            messages={
                "message": success.NOTIFICATION_MARK_AS_READ.format(count=count),
            },
        )
