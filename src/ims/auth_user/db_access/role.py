"""
Role Manager
This module contains the manager for the Role model.
It provides an interface to interact with the Role model and perform
"""

from base.db_access import manager

from ..db_models import Role


class RoleManager(manager.Manager[Role]):
    """
    Manager class for the Role model.
    """

    model = Role


role_manager = RoleManager()
