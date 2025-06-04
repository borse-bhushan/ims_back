"""
Stock manager module.
This module contains the StockManager class, which is responsible for managing
the Stock model.
It provides methods for creating, updating, deleting, and retrieving Stock records.
"""

from base.db_access import manager

from .models import Stock


class StockManager(manager.Manager[Stock]):
    """
    Manager class for the Stock model.
    """

    model = Stock


stock_manager = StockManager()
