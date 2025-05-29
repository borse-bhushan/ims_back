"""
Load the pre requesit data.
"""

import json


from auth_user.db_access import user_manager

from tenant.db_access import tenant_manager
from tenant.utils.helpers import set_tenant_details_to_request_thread


def load_data():
    """
    Load the pre requesit data.
    """
    load_data_obj = LoadDataFromFiles()
    load_data_obj.delete_all_records()

    load_data_obj.load_tenant_data()

    tenant_manager_obj = tenant_manager.disable_tenant_aware()
    tenant_obj = tenant_manager_obj.get(query={})

    set_tenant_details_to_request_thread(tenant_obj)

    load_data_obj.load_user_data()

    return True


class LoadDataFromFiles:
    """
    Class to load the data from json files.
    """

    def load_user_data(self):
        """
        Load the user data from the json file and create user.
        """
        data = self.read_file("user")
        user_data = data.get("data")

        return user_manager.create(data=user_data, many=True)

    def load_tenant_data(self):
        """
        Load the tenant data from the json file and create tenant.
        """
        data = self.read_file("tenant")
        tenant_data = data.get("data")
        tenant_manager_obj = tenant_manager.disable_tenant_aware()
        data = tenant_manager_obj.create(data=tenant_data, many=True)
        return data

    def delete_all_records(self):
        """
        Deletes all the records from models
        """

        user_manager_obj = user_manager.disable_tenant_aware()
        user_manager_obj.delete(soft_delete=False, force_delete=True)

        tenant_manager_obj = tenant_manager.disable_tenant_aware()
        tenant_manager_obj.delete(soft_delete=False, force_delete=True)

    def read_file(self, file_path):
        """
        Reads the json file from the utils/load_data/json_data directory.
        """
        with open(
            f"utils/load_data/json_data/{file_path}.json",
            "r",
            encoding="UTF-8",
        ) as conf_file:
            return json.load(conf_file)
