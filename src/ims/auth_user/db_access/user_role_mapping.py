"""
User Role Mapping Manager
It provides an interface to interact with the UserRoleMapping model and perform
"""

from base.db_access import manager

from ..db_models import UserRoleMapping



class UserRoleMappingManager(manager.Manager[UserRoleMapping]):
    """
    Manager class for the UserRoleMapping model.
    """

    model = UserRoleMapping


user_role_mapping_manager = UserRoleMappingManager()
