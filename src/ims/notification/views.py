"""
Notification ViewSet
This module contains the NotificationViewSet class, which is responsible for
handling HTTP requests related to notifications.
"""

from rest_framework import viewsets, status
from drf_spectacular.utils import extend_schema


from utils.messages import success
from utils.response import generate_response
from utils.exceptions import ValidationError, NoDataFoundError

from auth_user.constants import MethodEnum
from auth_user.db_access import user_manager

from base.views.base import UpdateView, ListView
from authentication import register_permission, get_authentication_classes

from utils.swagger import (
    responses_400,
    responses_404,
    responses_401,
    responses_400_example,
    responses_404_example,
    responses_401_example,
)


from .serializers.swagger import (
    MarkNotificationResponseSerializer,
    NotificationListResponseSerializer,
    notification_list_success_example,
    mark_read_patch_success_example
)


from .serializers import NotificationMarkAsReadSerializer
from .db_access import user_notification_manager, notification_manager

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
            **UpdateView.get_method_view_mapping(patch=False),
        }

    def get_query_obj(self, request, **_):
        return {
            "user_id": request.user.user_id,
            "is_read": False,
        }

    def get_list(self, objects, **_):
        user_ids = []
        notification_ids = []
        for obj in objects:
            user_ids.append(obj.created_by)
            notification_ids.append(obj.notification_id)

        user_mapping_obj = user_manager.get_objects_mapping(
            query={
                "user_id__in": user_ids,
            }
        )
        notification_mapping_obj = notification_manager.get_objects_mapping(
            query={
                "notification_id__in": notification_ids,
            }
        )

        data_list = []
        for obj in objects:

            data_dict = {}
            data_dict["created_dtm"] = obj.created_dtm
            data_dict["sent_by"] = user_mapping_obj[obj.created_by].to_dict()
            data_dict["notification"] = notification_mapping_obj[
                obj.notification_id
            ].to_dict()
            data_list.append(data_dict)

        return data_list

    @extend_schema(
        responses={
            200: NotificationListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            notification_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)


    @extend_schema(
        responses={
            200: MarkNotificationResponseSerializer,
            **responses_400,
            **responses_404,
            **responses_401,
        },
        examples=[
            mark_read_patch_success_example,
            responses_404_example,
            responses_401_example,
            responses_400_example,
        ],
        tags=[MODULE],
    )
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
