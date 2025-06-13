"""
Check if a tenant is using a shared database configuration.
"""

from utils import settings

from ..constants import DatabaseStrategyEnum
from .tenant_setup import set_database_to_global_settings
from .helpers import get_tenant_details_from_request_thread
from ..db_access import tenant_configuration_manager, tenant_manager

DEFAULT = "default"


def get_tenant_db_name(tenant):
    """
    Retrieve the database name for a given tenant.
    This function determines the appropriate database name for a tenant based on their
    configuration and database strategy. It handles both direct tenant objects and
    tenant IDs as input.
    Args:
        tenant: Either a tenant object or a tenant ID string. If a tenant ID is provided,
               the function will attempt to retrieve the corresponding tenant object.
    Returns:
        str: The database name to use for the tenant. This will be either:
             - The tenant's code if it exists in DATABASES
             - A new database name if the tenant uses a dedicated database
             - The default database name if the tenant uses a shared database
    Raises:
        None explicitly, but may raise exceptions from underlying functions
    Notes:
        - If tenant is not found in the request thread, it will attempt to fetch from database
        - The function checks the tenant's database strategy (shared vs dedicated)
        - For dedicated databases, it sets up the database configuration in global settings
    """

    _tenant = tenant
    if not isinstance(_tenant, tenant_manager.model):
        _tenant = get_tenant_details_from_request_thread(raise_err=False, g_t_obj=True)[
            "tenant_obj"
        ]

        if not _tenant:
            _tenant = tenant_manager.disable_tenant_aware().get(
                query={
                    "tenant_id": tenant,
                },
                using=DEFAULT,
            )

    DATABASES = settings.read("DATABASES")
    if _tenant.tenant_code in DATABASES:
        return _tenant.tenant_code

    tenant_config_obj = tenant_configuration_manager.disable_tenant_aware().get(
        {
            "tenant_id": _tenant.tenant_id,
        }
    )

    is_shared = tenant_config_obj.database_strategy == DatabaseStrategyEnum.SHARED
    if not is_shared:
        return set_database_to_global_settings(_tenant)

    return DEFAULT
