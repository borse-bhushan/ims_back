"""
This module provides utilities for registering and managing
permissions for different modules and their actions.
"""

from auth_user.db_access import permission_manager

from tenant.utils.tenant_conf import get_tenant_db_name


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

        self.__modules_and_there_actions[module] = action_list
        return True

    def load_permissions_for_tenant(self, tenant_id, request):
        """
        Loads all registered modules and their actions into the
        permission manager for a single tenant.
        """

        db_name = get_tenant_db_name(tenant_id)

        for module, action_and_name_list in self.__modules_and_there_actions.items():
            for action_and_name in action_and_name_list:
                self.__upsert_permission(
                    module, action_and_name, db_name, request, tenant_id
                )

    def __upsert_permission(self, module, action_and_name, db_name, request, tenant_id):
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
            using=db_name,
        )


load_permission = LoadPermission()
