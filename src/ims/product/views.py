"""
Product viewset for managing Products.
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
    SuccessResponseSerializer
)


from .db_access import product_manager
from .serializers import ProductQuerySerializer, ProductSerializer
from .serializers.swagger import (
    ProductResponseSerializer,
    ProductListResponseSerializer,
    product_list_success_example,
    product_create_success_example,
    product_update_success_example,
    product_delete_success_example,
    product_get_by_id_success_example,
)

MODULE = "Product"


class ProductViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for managing product.
    """

    manager = product_manager
    lookup_field = "product_id"
    serializer_class = ProductSerializer
    list_serializer_class = ProductQuerySerializer
    search_fields = ["product_code", "product_name"]

    get_authenticators = get_authentication_classes

    @extend_schema(
        responses={201: ProductResponseSerializer, **responses_400, **responses_401},
        examples=[
            product_create_success_example,
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
            200: ProductListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            product_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"List {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: ProductResponseSerializer, **responses_404, **responses_401},
        examples=[
            product_get_by_id_success_example,
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
            200: ProductResponseSerializer,
            **responses_400,
            **responses_404,
            **responses_401,
        },
        examples=[
            product_update_success_example,
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
            product_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
