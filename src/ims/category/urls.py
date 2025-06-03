"""
Category URL routing module.
"""

from django.urls import path


from .views import CategoryViewSet

urlpatterns = [
    path(
        "category",
        CategoryViewSet.as_view(CategoryViewSet.get_method_view_mapping()),
        name="category",
    ),
    path(
        "category/<str:category_id>",
        CategoryViewSet.as_view(CategoryViewSet.get_method_view_mapping(True)),
        name="category-detail",
    ),
]
