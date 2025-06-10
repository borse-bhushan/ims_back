from rest_framework import serializers

from utils.exceptions import codes


class NotificationMarkAsReadSerializer(serializers.Serializer):
    """
    Serializer for marking notifications as read.
    """

    list_notification_id = serializers.ListField(
        child=serializers.UUIDField(),
        help_text="List of notification IDs to mark as read.",
    )

    mark_all_as_read = serializers.BooleanField(
        default=False,
        help_text="Flag to indicate if all notifications should be marked as read.",
    )

    def validate(self, attrs):
        """
        Validate the input data.
        """

        if not attrs.get("list_notification_id") and not attrs.get("mark_all_as_read"):
            raise serializers.ValidationError(
                {"list_notification_id": self.error_messages["required"]},
                code=codes.REQUIRED,
            )
        return attrs
