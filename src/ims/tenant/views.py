"""
Tenant viewset for managing Tenants.
"""

from rest_framework import viewsets
from drf_spectacular.utils import extend_schema


from base.views.base import BaseView, RetrieveView, CreateView

from utils.constants import BASE_PATH
from utils.swagger import (
    responses_400,
    responses_404,
    responses_401,
    responses_400_example,
    responses_404_example,
    responses_401_example,
    SuccessResponseSerializer,
)

from auth_user.constants import MethodEnum
from authentication import get_default_authentication_class, register_permission


from .db_access import tenant_manager, tenant_configuration_manager
from .serializers import (
    TenantSerializer,
    TenantQuerySerializer,
    TenantConfigurationSerializer,
)

from .utils.tenant_setup import NewTenantSetup

from .serializers.swagger.tenant import (
    TenantResponseSerializer,
    TenantListResponseSerializer,
    tenant_list_success_example,
    tenant_create_success_example,
    tenant_update_success_example,
    tenant_get_by_id_success_example,
    tenant_delete_success_example,
)


from .serializers.swagger.tenant_conf import (
    tenant_config_create_success_example,
    tenant_config_get_by_id_success_example,
    TenantConfigurationResponseSerializer,
    TenantConfigurationDataSerializer,
)

from .serializers.swagger.tenant_details import (
    TenantDomainConfigResponseSerializer,
    tenant_domain_config_get_by_id_success_example,
)

MODULE = "Tenant"
MODULE_DETAILS = "Tenant Details"
MODULE_CONF = "Tenant Configuration"


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

    @extend_schema(
        responses={201: TenantResponseSerializer, **responses_400, **responses_401},
        examples=[
            tenant_create_success_example,
            responses_400_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(
        MODULE,
        MethodEnum.POST,
        f"Create {MODULE}",
        create_permission=False,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses={
            200: TenantListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            tenant_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(
        MODULE,
        MethodEnum.GET,
        f"List {MODULE}",
        create_permission=False,
    )
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: TenantResponseSerializer, **responses_404, **responses_401},
        examples=[
            tenant_get_by_id_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(
        MODULE,
        MethodEnum.GET,
        f"Get {MODULE}",
        create_permission=False,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={
            200: TenantResponseSerializer,
            **responses_400,
            **responses_404,
            **responses_401,
        },
        examples=[
            tenant_update_success_example,
            responses_404_example,
            responses_401_example,
            responses_400_example,
        ],
        tags=[MODULE],
    )
    @register_permission(
        MODULE,
        MethodEnum.PUT,
        f"Update {MODULE}",
        create_permission=False,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        responses={204: SuccessResponseSerializer, **responses_404, **responses_401},
        examples=[
            tenant_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
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

    @extend_schema(
        responses={
            200: TenantDomainConfigResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            tenant_domain_config_get_by_id_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE_DETAILS],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

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

    def post_save(self, obj, request, **kwargs):
        NewTenantSetup(obj, request).setup()
        return super().post_save(obj, **kwargs)

    def is_create_data_valid(self, request, *args, **kwargs):
        request.data["tenant_id"] = kwargs["tenant_id"]
        return super().is_create_data_valid(request, *args, **kwargs)

    @extend_schema(
        request=TenantConfigurationDataSerializer,
        responses={
            201: TenantConfigurationResponseSerializer,
            **responses_400,
            **responses_401,
        },
        examples=[
            tenant_config_create_success_example,
            responses_400_example,
            responses_401_example,
        ],
        tags=[MODULE_CONF],
    )
    @register_permission(
        MODULE_CONF,
        MethodEnum.POST,
        f"Create {MODULE_CONF}",
        create_permission=False,
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def get_details_query(self, **kwargs):
        return {"tenant_id": kwargs["tenant_id"]}

    @extend_schema(
        responses={
            200: TenantConfigurationResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            tenant_config_get_by_id_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE_CONF],
    )
    @register_permission(
        MODULE_CONF,
        MethodEnum.GET,
        f"Get {MODULE_CONF}",
        create_permission=False,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def save(self, data, **_):
        """
        Save the tenant configuration data.
        """

        return self.manager.upsert(data=data, query={"tenant_id": data["tenant_id"]})
