"""
tenant URL routing module.
"""

from django.urls import path

from utils.exclude_path import add_excluded_path

from .views import TenantViewSet, TenantDetialsViewSet

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
    path(
        add_excluded_path("tenant/<str:tenant_code>/details"),
        TenantDetialsViewSet.as_view(TenantDetialsViewSet.get_method_view_mapping()),
        name="tenant-detail",
    ),
]
