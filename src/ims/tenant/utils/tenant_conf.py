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
    Check if a tenant is using a shared database configuration.
    This function determines whether a given tenant uses a shared database strategy by:
    1. Checking if tenant has a dedicated database configuration
    2. If not, retrieving tenant configuration to check database strategy
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
