from django.urls import path

from .views import ReportViewSet

urlpatterns = [
    path(
        "report/stock-summary",
        ReportViewSet.as_view({"get": "get_stock_summary"}),
        name="stock-summary",
    ),
]
