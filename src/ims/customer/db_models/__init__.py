"""
This module contains the database models for the customer app.
It includes the Customer model and its manager.
"""

from .customer import Customer
from .customer_sso_info import CustomerSSOInfo

__all__ = [
    "Customer",
    "CustomerSSOInfo",
]
