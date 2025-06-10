from utils.constants import SeverityEnum

from ..db_access import notification_manager, user_notification_manager


class SendNotification:
    """
    A class to handle sending notifications.
    """

    def __init__(
        self,
        title,
        message,
        notification_type,
        created_by,
        notification_data=None,
        severity=SeverityEnum.INFO,
    ):
        self.title = title
        self.message = message
        self.severity = severity
        self.created_by = created_by
        self.notification_type = notification_type
        self.notification_data = notification_data or {}

    def __create_notification(self):
        """
        Create a notification object.
        based on the provided title, message, recipient, and notification type.
        """
        return notification_manager.create(
            data={
                "title": self.title,
                "message": self.message,
                "severity": self.severity,
                "created_by": self.created_by,
                "updated_by": self.created_by,
                "notification_data": self.notification_data,
                "notification_type": self.notification_type,
            }
        )

    def send(self, recipient_list):
        """
        Send the notification.
        """


        notification = self.__create_notification()
        for recipient in recipient_list:
            user_notification_manager.create(
                data={
                    "is_read": False,
                    "user_id": recipient.user_id,
                    "notification": notification,
                    "created_by": self.created_by,
                    "updated_by": self.created_by,
                }
            )
        return notification
