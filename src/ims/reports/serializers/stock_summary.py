from rest_framework import serializers

from utils.messages import error
from utils.exceptions import codes

from product.db_access import product_manager


class StockSummaryQuerySerializer(serializers.Serializer):

    product_id = serializers.UUIDField()

    def validate_product_id(self, value):
        """
        Validate product_id field.
        - For create and update: product_id must exist.
        """

        if not product_manager.exists(query={"product_id": value}):
            raise serializers.ValidationError(
                error.NO_DATA_FOUND,
                code=codes.NO_DATA_FOUND,
            )

        return value
