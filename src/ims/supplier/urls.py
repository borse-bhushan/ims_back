"""
Supplier URL routing module.
"""

from django.urls import path


from .views import SupplierViewSet

urlpatterns = [
    path(
        "supplier",
        SupplierViewSet.as_view(SupplierViewSet.get_method_view_mapping()),
        name="supplier",
    ),
    path(
        "supplier/<str:supplier_id>",
        SupplierViewSet.as_view(SupplierViewSet.get_method_view_mapping(True)),
        name="supplier-detail",
    ),
]
