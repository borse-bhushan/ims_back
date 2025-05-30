"""
Permission decorator for checking user permissions.
This module provides a decorator to register and check user permissions
"""

from functools import wraps

from utils.exceptions import PermissionDenied
from audit_logs.helpers import create_audit_log_entry

from auth_user.constants import RoleEnum
from auth_user.db_access import permission_manager, role_permission_mapping_manager


def register_permission(
    module: str,
    action: str,
    name: str,
    check: bool = True,
    create_permission: bool = True,
    **m_kwargs,
):
    """
    Register a permission with the given module, action, and name.
    """

    def decorator(view):
        """
        Decorator to check if the user has the permission before executing the view.
        """

        @wraps(view)
        def wrapper(self, request, *args, **kwargs):
            """
            Wrapper function to check if the user has the permission before executing the view.
            If check is False, it will not check the permission.
            If check is True, it will check the permission.
            If the user does not have the permission, it will raise a PermissionDenied exception.
            If the user has the permission, it will execute the view.
            """
            create_audit_log_entry(
                action=action,
                request=request,
                module_name=module,
            )
            if check:

                if create_permission and not m_kwargs.get("permission_obj"):
                    m_kwargs["permission_obj"] = permission_manager.upsert(
                        data={
                            "name": name,
                            "action": action,
                            "module": module,
                        },
                        query={
                            "action": action,
                            "module": module,
                        },
                    )

                is_super_admin = RoleEnum.SUPER_ADMIN == request.user.role_id

                if not create_permission and not is_super_admin:
                    raise PermissionDenied()

                if not is_super_admin and not role_permission_mapping_manager.exists(
                    query={
                        "role_id": request.user.role_id,
                        "permission_id": m_kwargs["permission_obj"].permission_id,
                    }
                ):
                    raise PermissionDenied()

            return view(self, request, *args, **kwargs)

        return wrapper

    return decorator
