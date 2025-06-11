"""
Supplier viewset for managing Suppliers.
"""

from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from base.views.base import BaseView

from auth_user.constants import MethodEnum
from authentication import get_authentication_classes, register_permission

from utils.swagger import (
    responses_400,
    responses_404,
    responses_401,
    responses_400_example,
    responses_404_example,
    responses_401_example,
    SuccessResponseSerializer,
)

from .db_access import supplier_manager
from .serializers import SupplierQuerySerializer, SupplierSerializer
from .serializers.swagger import (
    SupplierResponseSerializer,
    SupplierListResponseSerializer,
    supplier_list_success_example,
    supplier_create_success_example,
    supplier_update_success_example,
    supplier_get_by_id_success_example,
    supplier_delete_success_example,
)

MODULE = "Supplier"


class SupplierViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for managing supplier.
    """

    manager = supplier_manager
    lookup_field = "supplier_id"
    serializer_class = SupplierSerializer
    list_serializer_class = SupplierQuerySerializer
    search_fields = ["supplier_code", "supplier_name"]

    get_authenticators = get_authentication_classes

    @extend_schema(
        responses={201: SupplierResponseSerializer, **responses_400, **responses_401},
        examples=[
            supplier_create_success_example,
            responses_400_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses={
            200: SupplierListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            supplier_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"List {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: SupplierResponseSerializer, **responses_404, **responses_401},
        examples=[
            supplier_get_by_id_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={
            200: SupplierResponseSerializer,
            **responses_400,
            **responses_404,
            **responses_401,
        },
        examples=[
            supplier_update_success_example,
            responses_404_example,
            responses_401_example,
            responses_400_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.PUT, f"Update {MODULE}")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        responses={204: SuccessResponseSerializer, **responses_404, **responses_401},
        examples=[
            supplier_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
