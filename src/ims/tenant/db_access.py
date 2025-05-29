"""
Tenant manager module.
This module contains the TenantManager class, which is responsible for managing
the Tenant model.
It provides methods for creating, updating, deleting, and retrieving Tenant records.
"""

from base.db_access import manager

from .models import Tenant


class TenantManager(manager.Manager[Tenant]):
    """
    Manager class for the Tenant model.
    """

    model = Tenant


tenant_manager = TenantManager()
