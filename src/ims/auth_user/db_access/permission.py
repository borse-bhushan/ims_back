"""
Permission manager module.
It provides an interface to interact with the Permission model and perform
"""

from base.db_access import manager
from ..db_models import Permission


class PermissionManager(manager.Manager[Permission]):
    """
    Manager class for the Permission model.
    """

    model = Permission


permission_manager = PermissionManager()
