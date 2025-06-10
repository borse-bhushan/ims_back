"""
Tenant viewset for managing Tenants.
"""

from rest_framework import viewsets

from base.views.base import BaseView, RetrieveView, CreateView

from utils.constants import BASE_PATH

from auth_user.constants import MethodEnum
from authentication import get_default_authentication_class, register_permission


from .db_access import tenant_manager, tenant_configuration_manager
from .serializers import (
    TenantSerializer,
    TenantQuerySerializer,
    TenantConfigurationSerializer,
)


MODULE = "Tenant"
MODULE_DETAILS = "Tenant Details"
TENANT_CONF = "Tenant Configuration"


class TenantViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for managing tenant.
    """

    manager = tenant_manager
    lookup_field = "tenant_id"
    serializer_class = TenantSerializer
    list_serializer_class = TenantQuerySerializer
    search_fields = ["tenant_code", "tenant_name"]

    get_authenticators = get_default_authentication_class

    def add_common_data(self, data, request, *args, **kwargs):
        """
        Adds common data to the request data.
        """

        user_id = request.user.user_id

        data["created_by"] = user_id
        data["updated_by"] = user_id

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
        f"List {MODULE}",
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


class TenantDetailsViewSet(RetrieveView, viewsets.ViewSet):
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
            "base_path": BASE_PATH.removesuffix("/"),
            "sub_domain": tenant_details[self.lookup_field],
            "api_host": f"{request.scheme}://{tenant_details[self.lookup_field]}.{request.get_host()}",
        }


class TenantConfigurationViewSet(CreateView, RetrieveView, viewsets.ViewSet):
    """
    ViewSet for managing tenant configuration.
    """

    manager = tenant_configuration_manager
    serializer_class = TenantConfigurationSerializer

    get_authenticators = get_default_authentication_class

    @classmethod
    def get_method_view_mapping(cls, **_):
        """
        Returns a mapping of HTTP methods to view methods for this class.
        """
        return {
            **CreateView.get_method_view_mapping(),
            **RetrieveView.get_method_view_mapping(),
        }

    def is_create_data_valid(self, request, *args, **kwargs):
        request.data["tenant_id"] = kwargs["tenant_id"]
        return super().is_create_data_valid(request, *args, **kwargs)

    @register_permission(
        TENANT_CONF,
        MethodEnum.POST,
        f"Create {TENANT_CONF}",
        create_permission=False,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_details_query(self, **kwargs):
        return {"tenant_id": kwargs["tenant_id"]}

    @register_permission(
        TENANT_CONF,
        MethodEnum.GET,
        f"Get {TENANT_CONF}",
        create_permission=False,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def save(self, data, **_):
        """
        Save the tenant configuration data.
        """

        return self.manager.upsert(data=data, query={"tenant_id": data["tenant_id"]})
