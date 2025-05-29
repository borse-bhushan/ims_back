"""
User Manager
It provides an interface to interact with the User model and perform
"""

from base.db_access import manager

from ..models import User


class UserManager(manager.Manager[User]):
    """
    Manager class for the User model.
    """

    model = User


user_manager = UserManager()
