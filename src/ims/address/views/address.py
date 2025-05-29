"""
Address viewset for managing departments.
"""

from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from base.views.base import BaseView
from auth_user.constants import MethodEnum
from address.serializers.swagger import AddressResponseSerializer
from authentication import get_authentication_classes, register_permission
from utils.swagger import (
    responses_400,
    responses_404,
    responses_401,
    responses_400_example,
    responses_404_example,
    responses_401_example,
)

from ..serializers import (
    CreateAddressSerializer,
    AddressListResponseSerializer,
    address_create_success_example,
    address_list_success_example,
    address_getById_success_example,
    address_update_success_example,
    address_delete_success_example,
)
from ..db_access import address_manager


MODULE_NAME = "Address"


class AddressViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for managing address.
    """

    authentication_classes = get_authentication_classes()
    manager = address_manager
    serializer_class = CreateAddressSerializer
    lookup_field = "address_id"

    @extend_schema(
        responses={201: AddressResponseSerializer, **responses_400, **responses_401},
        examples=[
            address_create_success_example,
            responses_400_example,
            responses_401_example,
        ],
        tags=[MODULE_NAME],
    )
    @register_permission(MODULE_NAME, MethodEnum.POST, f"Create {MODULE_NAME}")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        responses={
            200: AddressListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            address_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE_NAME],
    )
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: AddressResponseSerializer, **responses_404, **responses_401},
        examples=[
            address_getById_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE_NAME],
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={200: AddressResponseSerializer, **responses_404, **responses_401},
        examples=[
            address_update_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE_NAME],
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        responses={204: AddressResponseSerializer, **responses_404, **responses_401},
        examples=[
            address_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE_NAME],
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
