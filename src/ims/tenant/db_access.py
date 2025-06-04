"""
Tenant manager module.
This module contains the TenantManager class, which is responsible for managing
the Tenant model.
It provides methods for creating, updating, deleting, and retrieving Tenant records.
"""

from base.db_access import manager

from .models import Tenant, TenantConfiguration


class TenantManager(manager.Manager[Tenant]):
    """
    Manager class for the Tenant model.
    """

    model = Tenant


class TenantConfigurationManager(manager.Manager[TenantConfiguration]):
    """
    Manager class for the TenantConfiguration model.
    """

    model = TenantConfiguration


tenant_manager = TenantManager()
tenant_configuration_manager = TenantConfigurationManager()
