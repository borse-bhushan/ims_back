"""
Load the pre requesit data.
"""

# import json


# from auth_user.constants import RoleEnum
# from auth_user.db_access import (
#     role_manager,
#     permission_manager,
#     user_manager,
#     user_role_mapping_manager,
#     role_permission_mapping_manager,
# )
# from tenant.db_access import tenant_manager
# from customer.db_access import customer_manager, customer_sso_info_manager
# from customer.helpers import set_customer_tenant_details_to_request_thread


def load_data():
    """
    Load the pre requesit data.
    """
    # load_data_obj = LoadDataFromFiles()
    # load_data_obj.delete_all_records()

    # load_data_obj.load_tenant_data()

    # tenant_manager.disable_tenant_aware()
    # tenant_obj = tenant_manager.get(query={})
    # tenant_manager.enable_tenant_aware()

    # load_data_obj.load_customer_data(
    #     tenant_id=tenant_obj.tenant_id,
    # )

    # customer_manager.disable_tenant_aware()
    # customer_id = customer_manager.get(query={"tenant_id": tenant_obj.tenant_id})
    # customer_manager.enable_tenant_aware()

    # set_customer_tenant_details_to_request_thread(tenant_obj)

    # role_data = load_data_obj.load_role_data()
    # permission_data = load_data_obj.load_permission_data()
    # user_data = load_data_obj.load_user_data()

    # load_data_obj.load_user_roles_mapping_data(user_data, role_data)
    # load_data_obj.load_role_permissions_mapping_data(role_data, permission_data)
    return True


# class LoadDataFromFiles:

#     def load_role_data(self):
#         data = self.read_file("role")
#         role_data = data.get("data")

#         return role_manager.create(data=role_data, many=True)

#     def load_permission_data(self):
#         data = self.read_file("permission")
#         permission_data = data.get("data")

#         return permission_manager.create(data=permission_data, many=True)

#     def load_user_data(self):
#         data = self.read_file("user")
#         user_data = data.get("data")

#         return user_manager.create(data=user_data, many=True)

#     def load_user_roles_mapping_data(self, user_data, role_data):
#         for user in user_data:
#             for role in role_data:
#                 user_role_mapping_manager.create(
#                     data={
#                         "user_id": user.user_id,
#                         "role_id": role.role_id,
#                     }
#                 )

#     def load_role_permissions_mapping_data(self, role_data, permission_data):
#         for permission in permission_data:
#             for role in role_data:
#                 if role.role_code == RoleEnum.SUPER_COMPANY_ADMIN:
#                     continue
#                 role_permission_mapping_manager.create(
#                     data={
#                         "permission_id": permission.permission_id,
#                         "role_id": role.role_id,
#                     }
#                 )

#     def load_tenant_data(self):
#         data = self.read_file("tenant")
#         tenant_data = data.get("data")
#         tenant_manager.disable_tenant_aware()
#         data = tenant_manager.create(data=tenant_data, many=True)
#         tenant_manager.enable_tenant_aware()
#         return data

#     def load_customer_data(self, tenant_id=None):
#         data = self.read_file("customer")
#         customer_data = data.get("data")
#         for customer in customer_data:
#             customer["tenant_id"] = tenant_id

#         customer_manager.disable_tenant_aware()
#         data = customer_manager.create(data=customer_data, many=True)
#         customer_manager.enable_tenant_aware()
#         return data

#     def load_customer_sso_info_data(self, tenant_id=None, customer_id=None):
#         data = self.read_file("customer_sso_info")
#         customer_sso_info_data = data.get("data")
#         for customer_sso_info in customer_sso_info_data:
#             customer_sso_info["tenant_id"] = tenant_id
#             customer_sso_info["customer_id"] = customer_id

#         customer_sso_info_manager.disable_tenant_aware()
#         data = customer_sso_info_manager.create(
#             many=True,
#             data=customer_sso_info_data,
#         )

#         obj = customer_sso_info_manager.get(
#             query={"tenant_id": tenant_id, "customer_id": customer_id}
#         )
#         customer_sso_info_manager.enable_tenant_aware()
#         return obj

#     def delete_all_records(self):
#         """
#         Deletes all the records of Role, User, Permission, RolePermissionMapping, UserRoleMapping models
#         """

#         role_permission_mapping_manager.disable_tenant_aware()
#         role_permission_mapping_manager.delete(soft_delete=False, force_delete=True)
#         role_permission_mapping_manager.enable_tenant_aware()

#         user_role_mapping_manager.disable_tenant_aware()
#         user_role_mapping_manager.delete(soft_delete=False, force_delete=True)
#         user_role_mapping_manager.enable_tenant_aware()

#         permission_manager.disable_tenant_aware()
#         permission_manager.delete(soft_delete=False, force_delete=True)
#         permission_manager.enable_tenant_aware()

#         user_manager.disable_tenant_aware()
#         user_manager.delete(soft_delete=False, force_delete=True)
#         user_manager.enable_tenant_aware()

#         role_manager.disable_tenant_aware()
#         role_manager.delete(soft_delete=False, force_delete=True)
#         role_manager.enable_tenant_aware()

#         customer_sso_info_manager.disable_tenant_aware()
#         customer_sso_info_manager.delete(soft_delete=False, force_delete=True)
#         customer_sso_info_manager.enable_tenant_aware()

#         customer_manager.disable_tenant_aware()
#         customer_manager.delete(soft_delete=False, force_delete=True)
#         customer_manager.enable_tenant_aware()

#         tenant_manager.disable_tenant_aware()
#         tenant_manager.delete(soft_delete=False, force_delete=True)

#     def read_file(self, file_path):
#         with open(f"utils/load_data/json_data/{file_path}.json", "r") as conf_file:
#             return json.load(conf_file)
