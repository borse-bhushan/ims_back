"""
This module provides utilities for registering and managing
permissions for different modules and their actions.
"""

from auth_user.db_access import permission_manager


class LoadPermission:
    """
    RegisterPermission: Handles the registration of modules and their
        associated actions, and loads them into the permission manager.

    Attributes:
        __modules_and_there_actions (dict): A private class-level dictionary
        that stores modules as keys and their actions as values.
    """

    __modules_and_there_actions = {}

    def register_module_and_action(self, module, action, name):
        """
        Adds an action and its name to the specified module in the internal dictionary.
        """

        action_list: list = self.__modules_and_there_actions.get(module, [])

        action_list.append({"action": action, "name": name})

        return True

    def load_module_and_actions_for_tenants(
        self, tenant_id_or_list: list | str, request
    ):
        """
        Loads all registered modules and their actions into the permission manager in bulk.
        """

        if isinstance(tenant_id_or_list, str):
            tenant_id_or_list = [tenant_id_or_list]

        for tenant_id in tenant_id_or_list:
            self.__load_permissions_for_tenant(tenant_id, request)
        return True

    def __load_permissions_for_tenant(self, tenant_id, request):
        """
        Loads all registered modules and their actions into the
        permission manager for a single tenant.
        """
        for module, action_and_name_list in self.__modules_and_there_actions.items():
            for action_and_name in action_and_name_list:
                self.__upsert_permission(module, action_and_name, tenant_id, request)

    def __upsert_permission(self, module, action_and_name, tenant_id, request):
        """
        Upserts a single permission into the permission manager.
        """
        permission_manager.upsert(
            data={
                "module": module,
                **action_and_name,
                "tenant_id": tenant_id,
                "created_by": request.user.user_id,
            },
            query={
                "module": module,
                "tenant_id": tenant_id,
                "action": action_and_name["action"],
            },
        )


load_permission = LoadPermission()
