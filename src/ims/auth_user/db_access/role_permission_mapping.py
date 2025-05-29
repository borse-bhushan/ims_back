"""
RolePermissionMappingManager
it provides an interface to interact with the RolePermissionMapping model and perform
"""

from base.db_access import manager
from ..db_models import RolePermissionMapping


class RolePermissionMappingManager(manager.Manager[RolePermissionMapping]):
    """
    Manager class for the RolePermissionMapping model.
    """

    model = RolePermissionMapping


role_permission_mapping_manager = RolePermissionMappingManager()
