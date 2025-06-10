"""
tenant URL routing module.
"""

from django.urls import path

from utils.tenant_aware_path import add_to_tenant_aware_excluded_path_list

from .views import TenantViewSet, TenantDetailsViewSet, TenantConfigurationViewSet

urlpatterns = [
    path(
        add_to_tenant_aware_excluded_path_list("tenant/<str:tenant_id>/configuration"),
        TenantConfigurationViewSet.as_view(
            TenantConfigurationViewSet.get_method_view_mapping()
        ),
        name="tenant-configuration",
    ),
    path(
        add_to_tenant_aware_excluded_path_list("tenant"),
        TenantViewSet.as_view(TenantViewSet.get_method_view_mapping()),
        name="tenant",
    ),
    path(
        add_to_tenant_aware_excluded_path_list("tenant/<str:tenant_id>"),
        TenantViewSet.as_view(TenantViewSet.get_method_view_mapping(True)),
        name="tenant-detail",
    ),
    path(
        add_to_tenant_aware_excluded_path_list("tenant/<str:tenant_code>/details"),
        TenantDetailsViewSet.as_view(TenantDetailsViewSet.get_method_view_mapping()),
        name="tenant-detail",
    ),
]
