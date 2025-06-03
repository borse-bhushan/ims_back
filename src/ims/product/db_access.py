"""
Product manager module.
This module contains the ProductManager class, which is responsible for managing
the Product model.
It provides methods for creating, updating, deleting, and retrieving Product records.
"""

from base.db_access import manager

from .models import Product


class ProductManager(manager.Manager[Product]):
    """
    Manager class for the Product model.
    """

    model = Product


product_manager = ProductManager()
