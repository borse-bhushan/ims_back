from rest_framework import serializers
from ..constants import DEFAULT_PAGE_SIZE, DEFAULT_PAGE_NUMBER

class QuerySerializer(serializers.Serializer):
    page = serializers.IntegerField(default=DEFAULT_PAGE_NUMBER, min_value=1)
    page_size = serializers.IntegerField(default=DEFAULT_PAGE_SIZE, min_value=1)
