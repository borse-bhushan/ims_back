"""
Customer manager module.
This module contains the CustomerManager class, which is responsible for managing
the Customer model.
It provides methods for creating, updating, deleting, and retrieving customer records.
"""

from base.db_access import manager
from ..db_models import Customer


class CustomerManager(manager.Manager[Customer]):
    """
    Manager class for the Customer model.
    """

    model = Customer


customer_manager = CustomerManager()
