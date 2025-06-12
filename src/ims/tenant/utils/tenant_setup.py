import copy

"""
A class to handle the setup of a new tenant in the system.

"""

from django.core.management import call_command

from utils import settings

from ..db_access import tenant_manager
from ..constants import DatabaseStrategyEnum
from auth_user.db_access import user_manager


class NewTenantSetup:
    """
    This class manages the database setup for new tenants, particularly handling
    different database strategies (shared vs separate databases) and performing
    necessary migrations.

    Args:
        tenant_config_obj: Configuration object containing tenant settings and properties.

    Attributes:
        tenant_config_obj: Stored tenant configuration object.
        DATABASES: Dictionary of database configurations loaded from settings.



    """

    def __init__(self, tenant_config_obj, request):
        self.request = request
        self.tenant_config_obj = tenant_config_obj

    def setup(self):
        """
        Sets up the database for a new tenant.
            - For shared database strategy, returns True without additional setup
            - For separate database strategy:
                * Creates a new database configuration
                * Names the database using tenant code
                * Runs database migrations
            Returns:
                bool: True if setup is successful
        """

        if self.tenant_config_obj.database_strategy == DatabaseStrategyEnum.SHARED:
            return True

        tenant_obj = tenant_manager.get(
            query={"tenant_id": self.tenant_config_obj.tenant_id}
        )

        set_database_to_global_settings(tenant_obj)

        call_command("migrate", database=tenant_obj.tenant_code)

        self.create_super_admin_in_new_tenant(tenant_obj)

        return True

    def create_super_admin_in_new_tenant(self, tenant_obj):
        user = self.request.user
        user_manager.upsert(
            data={
                "email": user.email,
                "user_id": user.user_id,
                "role_id": user.role_id,
                "password": user.password,
                "last_name": user.last_name,
                "first_name": user.first_name,
                "date_joined": user.date_joined,
                "phone_number": user.phone_number,
                "profile_photo": user.profile_photo,
            },
            query={"email": user.email},
            using=tenant_obj.tenant_code,
        )
        return True


def set_database_to_global_settings(tenant_obj):
    """
    Configures and adds a new database configuration for a specific tenant to the global settings.
    """

    DATABASES = settings.read("DATABASES")

    if tenant_obj.tenant_code in DATABASES:
        return True

    new_db = copy.deepcopy(DATABASES["default"])

    new_db["NAME"] = f"{tenant_obj.tenant_code}.sqlite3"

    DATABASES[tenant_obj.tenant_code] = new_db

    return True
