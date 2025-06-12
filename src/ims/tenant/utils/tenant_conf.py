"""
Check if a tenant is using a shared database configuration.
"""

from utils import settings

from ..constants import DatabaseStrategyEnum
from ..db_access import tenant_configuration_manager
from .tenant_setup import set_database_to_global_settings


def is_tenant_using_shared_db(tenant_obj):
    """
    Check if a tenant is using a shared database configuration.
    This function determines whether a given tenant uses a shared database strategy by:
    1. Checking if tenant has a dedicated database configuration
    2. If not, retrieving tenant configuration to check database strategy
    """

    DATABASES = settings.read("DATABASES")
    if tenant_obj.tenant_code in DATABASES:
        return True

    tenant_config_obj = tenant_configuration_manager.disable_tenant_aware().get(
        {"tenant_id": tenant_obj.tenant_id}
    )

    is_shared = tenant_config_obj.database_strategy == DatabaseStrategyEnum.SHARED
    if is_shared:
        return True

    set_database_to_global_settings(tenant_obj)

    return False
