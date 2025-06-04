"""
Supplier manager module.
This module contains the SupplierManager class, which is responsible for managing
the Supplier model.
It provides methods for creating, updating, deleting, and retrieving Supplier records.
"""

from base.db_access import manager

from .models import Supplier


class SupplierManager(manager.Manager[Supplier]):
    """
    Manager class for the Supplier model.
    """

    model = Supplier


supplier_manager = SupplierManager()
