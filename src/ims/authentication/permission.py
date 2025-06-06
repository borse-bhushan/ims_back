"""
Permission decorator for checking user permissions.
This module provides a decorator to register and check user permissions
"""

from functools import wraps

from utils.exceptions import PermissionDenied
from audit_logs.helpers import create_audit_log_entry

from auth_user.constants import RoleEnum
from auth_user.db_access import permission_manager, role_permission_mapping_manager

from tenant.utils.helpers import is_request_tenant_aware


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
            """
            create_audit_log_entry(
                action=action,
                request=request,
                module_name=module,
            )

            if not check:
                return view(self, request, *args, **kwargs)

            is_super_admin = RoleEnum.SUPER_ADMIN == request.user.role_id

            if not create_permission:

                if not is_super_admin:
                    raise PermissionDenied()

                return view(self, request, *args, **kwargs)

            if not m_kwargs.get("permission_obj"):
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
            is_company_admin = False
            if is_request_tenant_aware():
                is_company_admin = RoleEnum.COMPANY_ADMIN == request.user.role_id

            if (
                not is_super_admin
                and not is_company_admin
                and not role_permission_mapping_manager.exists(
                    query={
                        "role_id": request.user.role_id,
                        "permission_id": m_kwargs["permission_obj"].permission_id,
                    }
                )
            ):
                raise PermissionDenied()

            return view(self, request, *args, **kwargs)

        return wrapper

    return decorator
