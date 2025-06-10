from rest_framework import viewsets

from auth_user.constants import MethodEnum

from authentication.auth import get_authentication_classes
from authentication.permission import register_permission

from utils.response import generate_response

from stock.db_access import stock_manager

MODULE_NAME = "Reports"


class ReportViewSet(viewsets.ViewSet):
    """
    ViewSet for handling reports.
    """

    get_authenticators = get_authentication_classes

    @register_permission(
        f"{MODULE_NAME} Stock Summary",
        MethodEnum.GET,
        "Get Stock Summary",
    )
    def get_stock_summary(self, request):
        """
        Endpoint to get stock summary.
        """

        stock_summary = stock_manager.get_stock_summary({})

        return generate_response()
