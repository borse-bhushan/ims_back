"""
Stock URL routing module.
"""

from django.urls import path


from .views import StockViewSet

urlpatterns = [
    path(
        "stock",
        StockViewSet.as_view(StockViewSet.get_method_view_mapping()),
        name="stock",
    ),
    path(
        "stock/<str:stock_id>",
        StockViewSet.as_view(StockViewSet.get_method_view_mapping(True)),
        name="stock-detail",
    ),
]
