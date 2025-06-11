"""
Category viewset for managing Categories.
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


from .db_access import category_manager
from .serializers import CategorySerializer, CategoryQuerySerializer
from .serializers.swagger import (
    CategoryResponseSerializer,
    CategoryListResponseSerializer,
    category_create_success_example,
    category_list_success_example,
    category_get_by_id_success_example,
    category_update_success_example,
    category_delete_success_example,
)

MODULE = "Category"


class CategoryViewSet(BaseView, viewsets.ViewSet):
    """
    ViewSet for managing category.
    """

    manager = category_manager
    lookup_field = "category_id"
    serializer_class = CategorySerializer
    list_serializer_class = CategoryQuerySerializer
    search_fields = ["category_code", "category_name"]

    get_authenticators = get_authentication_classes

    @extend_schema(
        responses={201: CategoryResponseSerializer, **responses_400, **responses_401},
        examples=[
            category_create_success_example,
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
            200: CategoryListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            category_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"List {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: CategoryResponseSerializer, **responses_404, **responses_401},
        examples=[
            category_get_by_id_success_example,
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
            200: CategoryResponseSerializer,
            **responses_400,
            **responses_404,
            **responses_401,
        },
        examples=[
            category_update_success_example,
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
            category_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
