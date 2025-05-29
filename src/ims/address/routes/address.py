"""
Address URL routing module.
"""

from django.urls import path
from ..views import AddressViewSet


urlpatterns = [
    path(
        "address",
        AddressViewSet.as_view(AddressViewSet.get_method_view_mapping()),
        name="address",
    ),
    path(
        "address/<str:address_id>",
        AddressViewSet.as_view(AddressViewSet.get_method_view_mapping(True)),
        name="address",
    ),
]
