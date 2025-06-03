"""
Category manager module.
This module contains the CategoryManager class, which is responsible for managing
the Category model.
It provides methods for creating, updating, deleting, and retrieving Category records.
"""

from base.db_access import manager

from .models import Category


class CategoryManager(manager.Manager[Category]):
    """
    Manager class for the Category model.
    """

    model = Category


category_manager = CategoryManager()
