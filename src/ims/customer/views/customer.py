"""
Customer viewset for managing customers.
"""

from rest_framework import viewsets

from base.views.base import BaseView
from auth_user.constants import MethodEnum
from utils import functions as common_functions
from authentication import get_authentication_classes, register_permission


from ..serializers import (
    CreateCustomerSerializer,
)
from ..db_access import customer_manager


MODULE_NAME = "Customer"


class CustomerViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for managing customers.
    """

    manager = customer_manager
    lookup_field = "customer_id"
    serializer_class = CreateCustomerSerializer
    authentication_classes = get_authentication_classes()

    def add_common_data(self, data: dict | list, request, many=False):
        """
        Adds common metadata fields to the object, such as `created_by` and `updated_by`.

        Args:
            data (dict | list): The input data to be updated with common metadata.
            request (Request): The HTTP request containing user information.
            many (bool): Determines if multiple objects are being processed.

        Returns:
            dict | list: The updated data with additional metadata fields.
        """
        user = request.user

        user_id = user.user_id
        tenant_id = user.tenant.tenant_id

        client_info = common_functions.get_client_info(request)

        data["created_by"] = user_id
        data["updated_by"] = user_id
        data["tenant_id"] = tenant_id
        data["client_ip"] = client_info["client_ip"]
        data["client_user_agent"] = client_info["client_user_agent"]

        return data

    @register_permission(MODULE_NAME, MethodEnum.POST, f"Create {MODULE_NAME}")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @register_permission(MODULE_NAME, MethodEnum.GET, f"Get {MODULE_NAME}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @register_permission(MODULE_NAME, MethodEnum.GET, f"Get {MODULE_NAME}")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @register_permission(MODULE_NAME, MethodEnum.PUT, f"Update {MODULE_NAME}")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @register_permission(MODULE_NAME, MethodEnum.DELETE, f"Delete {MODULE_NAME}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
