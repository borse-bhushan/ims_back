"""
Notification Serializer and List Swagger Example
"""

from rest_framework import serializers
from drf_spectacular.utils import OpenApiExample
from utils.swagger import PaginationSerializer
from utils.swagger.common_swagger_functions import (
    get_list_success_example,
    get_update_success_example,
)


# ----------------------------------
# Serializers
# ----------------------------------


class NotificationDataSerializer(serializers.Serializer):
    """
    Serializer for individual notification content.
    """

    notification_id = serializers.UUIDField()
    title = serializers.CharField()
    message = serializers.CharField()
    created_by = serializers.CharField()
    notification_type = serializers.CharField()
    notification_data = serializers.JSONField()


class SentByUserSerializer(serializers.Serializer):
    """
    Serializer for the user who sent the notification.
    """

    email = serializers.EmailField()
    user_id = serializers.UUIDField()
    role_id = serializers.CharField()
    phone_number = serializers.CharField()
    profile_photo = serializers.CharField(allow_null=True)
    last_name = serializers.CharField()
    first_name = serializers.CharField()
    full_name = serializers.CharField()


class NotificationListItemSerializer(serializers.Serializer):
    """
    Serializer for a single notification list item.
    """

    created_dtm = serializers.DateTimeField()
    sent_by = SentByUserSerializer()
    notification = NotificationDataSerializer()


class NotificationListDataSerializer(serializers.Serializer):
    """
    Data serializer for paginated notification list response.
    """

    list = NotificationListItemSerializer(many=True)
    pagination = PaginationSerializer()


class NotificationListResponseSerializer(serializers.Serializer):
    """
    Full response serializer for list notifications.
    """

    data = NotificationListDataSerializer()
    errors = serializers.JSONField(allow_null=True)
    messages = serializers.JSONField(allow_null=True)
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


class MarkNotificationResponseSerializer(serializers.Serializer):
    """
    Response serializer for mark as read operation.
    """

    data = serializers.JSONField(help_text="Read status update summary.")
    errors = serializers.JSONField(
        help_text="Any error messages for the response.", allow_null=True
    )
    messages = serializers.JSONField(
        help_text="Any informational messages for the response body.", allow_null=True
    )
    status_code = serializers.IntegerField(default=200)
    is_success = serializers.BooleanField(default=True)


# ----------------------------------
# Swagger List Example
# ----------------------------------

notification_list_example_data = [
    {
        "created_dtm": "2025-06-10T11:10:42.099860Z",
        "sent_by": {
            "email": "test@gmail.com",
            "user_id": "c4edf0fb-200f-475c-a9c9-5f8831e22f26",
            "role_id": "COMPANY_ADMIN",
            "phone_number": "234234",
            "profile_photo": None,
            "last_name": "Bhushan",
            "first_name": "Borse",
            "full_name": "Borse Bhushan",
        },
        "notification": {
            "title": "Stock Movement",
            "message": "Stock(IN:8702DF6C) has been In. The quantity is 1.",
            "created_by": "c4edf0fb-200f-475c-a9c9-5f8831e22f26",
            "notification_id": "1160442a-d08b-4ce7-9ab8-ec7a495e0a5e",
            "notification_type": "STOCK_IN",
            "notification_data": {"stock_id": "184843e7-7c59-4611-97d4-f0c9e32fa7e7"},
        },
    }
]

notification_list_success_example: OpenApiExample = get_list_success_example(
    name="List Notifications - Success", list_data=notification_list_example_data
)


mark_read_patch_success_example: OpenApiExample = get_update_success_example(
    name="Mark Notifications as Read - Success",
    data=None,
    message="1 Notifications are mark as read.",
)
