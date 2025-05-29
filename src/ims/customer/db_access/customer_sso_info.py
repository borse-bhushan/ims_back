"""
CustomerSSOInfo manager module.
This module contains the CustomerSSOInfoManager class, which is responsible for managing
the CustomerSSOInfo model.
It provides methods for creating, updating, deleting, and retrieving customer records.
"""

from base.db_access import manager
from ..db_models import CustomerSSOInfo


class CustomerSSOInfoManager(manager.Manager[CustomerSSOInfo]):
    """
    Manager class for the CustomerSSOInfo model.
    """

    model = CustomerSSOInfo


customer_sso_info_manager = CustomerSSOInfoManager()
