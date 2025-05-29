"""
address manager module.
This module contains the addressManager class, which is responsible for managing
the Address model.
It provides methods for creating, updating, deleting, and retrieving address records.
"""

from base.db_access import manager
from ..db_models import Address


class AddressManager(manager.Manager[Address]):
    """
    Manager class for the Address model.
    """

    model = Address


address_manager = AddressManager()
