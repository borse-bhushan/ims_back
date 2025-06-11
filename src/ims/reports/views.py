from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from auth_user.constants import MethodEnum

from authentication.permission import register_permission
from authentication.auth import get_authentication_classes

from utils.response import generate_response
from utils.exceptions import ValidationError

from utils.swagger import (
    responses_404,
    responses_401,
    responses_404_example,
    responses_401_example,
)


from stock.db_access import stock_manager
from product.db_access import product_manager

from .serializers import StockSummaryQuerySerializer
from .serializers.stock_summery_swag import (
    ReportListResponseSerializer,
    report_list_success_example,
)

MODULE = "Reports"


class ReportViewSet(viewsets.ViewSet):
    """
    ViewSet for handling reports.
    """

    get_authenticators = get_authentication_classes

    @extend_schema(
        responses={
            200: ReportListResponseSerializer,
            **responses_404,
            **responses_401,
        },
        examples=[
            report_list_success_example,
            responses_404_example,
            responses_401_example,
        ],
        tags=[MODULE],
    )
    @register_permission(
        f"{MODULE} Stock Summary",
        MethodEnum.GET,
        "Get Stock Summary",
    )
    def get_stock_summary(self, request):
        """
        Endpoint to get stock summary.
        """

        stock_summary_filter = StockSummaryQuerySerializer(
            data=request.query_params.dict() or {}, partial=True
        )

        if not stock_summary_filter.is_valid():
            raise ValidationError(stock_summary_filter.errors)

        stock_summary = stock_manager.get_stock_summary(
            query=stock_summary_filter.validated_data
        )

        product_id_list = []
        for obj in stock_summary:
            product_id_list.append(obj["product_id"])

        product_obj_mapping = product_manager.get_objects_mapping(
            query={
                "product_id__in": product_id_list,
            }
        )

        data_list = []
        for obj in stock_summary:
            data_dict = {}
            data_dict["movement_type"] = obj["movement_type"]
            data_dict["total_quantity"] = obj["total_quantity"]
            data_dict["product"] = product_obj_mapping[obj["product_id"]].to_dict()
            data_list.append(data_dict)

        return generate_response(data=data_list)
