"""
Product viewset for managing Products.
"""

from rest_framework import viewsets

from base.views.base import BaseView

from auth_user.constants import MethodEnum
from authentication import get_authentication_classes, register_permission


from .db_access import product_manager
from .serializers import ProductQuerySerializer, ProductSerializer


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
    authentication_classes = get_authentication_classes()

    @register_permission(MODULE, MethodEnum.POST, f"Create {MODULE}")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.GET, f"List {MODULE}")
    def list_all(self, request, *args, **kwargs):
        return super().list_all(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.GET, f"Get {MODULE}")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.PUT, f"Update {MODULE}")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @register_permission(MODULE, MethodEnum.DELETE, f"Delete {MODULE}")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
