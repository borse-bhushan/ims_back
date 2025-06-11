"""
Stock viewset for managing Stocks.
"""

from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from base.views.base import CreateView, ListView, RetrieveView, DeleteView

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

from .db_access import stock_manager
from .serializers import StockQuerySerializer, StockSerializer
from .serializers.swagger import (
    StockResponseSerializer,
    StockListResponseSerializer,
    stock_list_success_example,
    stock_create_success_example,
    stock_get_by_id_success_example,
    stock_delete_success_example,
)

MODULE = "Stock"


class StockViewSet(CreateView, ListView, RetrieveView, DeleteView, viewsets.ViewSet):
    """
    ViewSet for managing stock.
    """

    manager = stock_manager
    lookup_field = "stock_id"
    serializer_class = StockSerializer
    list_serializer_class = StockQuerySerializer

    search_fields = ["reference_number"]
    filter_fields = ["product_id", "supplier_id", "movement_type"]

    get_authenticators = get_authentication_classes

    @classmethod
    def get_method_view_mapping(cls, with_path_id=False):
        if with_path_id:
            return {
                **DeleteView.get_method_view_mapping(),
                **RetrieveView.get_method_view_mapping(),
            }

        return {
            **ListView.get_method_view_mapping(),
            **CreateView.get_method_view_mapping(),
        }

    @extend_schema(
        responses={201: StockResponseSerializer, **responses_400, **responses_401},
        examples=[
            stock_create_success_example,
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
            200: StockListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            stock_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"List {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @extend_schema(
        responses={200: StockResponseSerializer, **responses_404, **responses_401},
        examples=[
            stock_get_by_id_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={204: SuccessResponseSerializer, **responses_404, **responses_401},
        examples=[
            stock_delete_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
