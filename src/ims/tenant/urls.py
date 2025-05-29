"""
tenant URL routing module.
"""

from django.urls import path

from .views import TenantViewSet

urlpatterns = [
    path(
        "tenant",
        TenantViewSet.as_view(TenantViewSet.get_method_view_mapping()),
        name="tenant",
    ),
    path(
        "tenant/<str:tenant_id>",
        TenantViewSet.as_view(TenantViewSet.get_method_view_mapping(True)),
        name="tenant-detail",
    ),
]
