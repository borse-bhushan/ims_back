"""
Tenant viewset for managing Tenants.
"""

from rest_framework import viewsets

from base.views.base import BaseView, RetrieveView

from utils.constants import BASE_PATH
from utils import functions as common_functions

from auth_user.constants import MethodEnum
from authentication import get_authentication_classes, register_permission


from .serializers import TenantSerializer, TenantQuerySerializer
from .db_access import tenant_manager


MODULE = "Tenant"
MODULE_DETAILS = "Tenant Details"


class TenantViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for managing tenant.
    """

    manager = tenant_manager
    lookup_field = "tenant_id"
    serializer_class = TenantSerializer
    authentication_classes = get_authentication_classes()

    list_serializer_class = TenantQuerySerializer
    search_fields = ["tenant_code", "tenant_name"]

    def add_common_data(self, data, request, *args, **kwargs):
        """
        Adds common data to the request data.
        """

        user_id = request.user.user_id

        client_info = common_functions.get_client_info(request)

        data["created_by"] = user_id
        data["updated_by"] = user_id
        data["client_ip"] = client_info["client_ip"]
        data["client_user_agent"] = client_info["client_user_agent"]

        return data

    @register_permission(
        MODULE,
        MethodEnum.POST,
        f"Create {MODULE}",
        create_permission=False,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @register_permission(
        MODULE,
        MethodEnum.GET,
        f"Get {MODULE}",
        create_permission=False,
    )
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @register_permission(
        MODULE,
        MethodEnum.GET,
        f"Get {MODULE}",
        create_permission=False,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @register_permission(
        MODULE,
        MethodEnum.PUT,
        f"Update {MODULE}",
        create_permission=False,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @register_permission(
        MODULE,
        MethodEnum.DELETE,
        f"Delete {MODULE}",
        create_permission=False,
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class TenantDetialsViewSet(RetrieveView, viewsets.ViewSet):
    """
    ViewSet for managing tenant details.
    """

    manager = tenant_manager
    lookup_field = "tenant_code"

    def get_details(self, obj, **kwargs):
        """
        Get the details of the object in dictionary format.
        """

        request = kwargs["request"]
        tenant_details = obj.to_dict()
        return {
            "host": request.get_host(),
            "sub_domain": tenant_details["tenant_code"],
            "api_host": f"{request.scheme}://{tenant_details['tenant_code']}.{request.get_host()}",
            "base_path": BASE_PATH.removesuffix("/"),
        }
