"""
Product URL routing module.
"""

from django.urls import path


from .views import ProductViewSet

urlpatterns = [
    path(
        "product",
        ProductViewSet.as_view(ProductViewSet.get_method_view_mapping()),
        name="product",
    ),
    path(
        "product/<str:product_id>",
        ProductViewSet.as_view(ProductViewSet.get_method_view_mapping(True)),
        name="product-detail",
    ),
]
