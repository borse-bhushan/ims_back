from rest_framework import serializers
from ..constants import DEFAULT_PAGE_SIZE, DEFAULT_PAGE_NUMBER


class QuerySerializer(serializers.Serializer):
    """
    A base serializer for handling query parameters with pagination.
    """

    page = serializers.IntegerField(default=DEFAULT_PAGE_NUMBER, min_value=1)
    page_size = serializers.IntegerField(default=DEFAULT_PAGE_SIZE, min_value=1)

    def to_internal_value(self, data):
        """
        Override to_internal_value to ensure that page and page_size are set
        to default values if not provided in the input data.
        """

        data = data.copy()

        if "page" not in data:
            data["page"] = DEFAULT_PAGE_NUMBER

        if "page_size" not in data:
            data["page_size"] = DEFAULT_PAGE_SIZE

        return super().to_internal_value(data)
