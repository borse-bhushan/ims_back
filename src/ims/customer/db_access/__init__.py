"""
This module provides access to the customer database.
It imports the customer_manager from the customer module.
"""

from .customer import customer_manager
from .customer_sso_info import customer_sso_info_manager

__all__ = ["customer_manager", "customer_sso_info_manager"]
