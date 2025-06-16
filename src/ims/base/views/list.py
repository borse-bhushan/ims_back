"""
This module contains the BaseListView class, which provides a base implementation
for retrieving objects based on query parameters. It raises a 404 error if the object is not found.
"""

from base import constants
from base.db_access import Manager
from base.serializers import QuerySerializer

from utils.response import generate_response
from utils.exceptions import NoDataFoundError
from utils.exceptions.exceptions import ValidationError


class ListView:
    """
    A base view class for retrieving objects with query params.
    Attributes:
        manager (object): The manager instance responsible for handling database queries.
    """

    filter_fields = []
    manager: Manager = None
    is_pagination: bool = True
    list_serializer_class: QuerySerializer | None = QuerySerializer

    search_fields = []
    filter_fields = []

    only_fields = []
    order_by_fields = []

    @classmethod
    def get_method_view_mapping(cls):
        """
        Returns a dictionary mapping HTTP methods to their corresponding view methods.
        """
        return {constants.GET: "list_all"}

    def get_list(self, objects, **_):
        """
        Convert a list of objects to a dictionary format.
        """
        return [obj.to_dict() for obj in objects]

    def search_query(self, query_params: dict, **_):
        """
        Generate a search query based on the provided query parameters.
        """

        search_query = []

        for field in self.search_fields:
            value = str(query_params.get(field, "")).strip()

            if not value:
                continue

            search_query.append({f"{field}__icontains": value})

        return search_query

    def filter_query(self, query_params: dict, **_):
        """
        Generate a filter query based on the provided query parameters.
        """
        filter_query = {}

        for field in self.filter_fields:
            value = str(query_params.get(field, "")).strip()

            if not value:
                continue

            filter_query[field] = value

        return filter_query

    def list_all(self, request):
        """
        Retrieve object list based query params provided in the request data.
        Args:
            request (Request): The HTTP request object containing the data.
        Returns:
            object: The list of retrieved objects if found.
        """

        query = request.query_params.dict() or {}

        if self.is_pagination:
            return self.get_with_pagination(request, query)

        return self.get_without_pagination(request, query)

    def get_without_pagination(self, request, query_params):
        """
        Retrieve object list without pagination based on query params provided in the request data.
        """

        if self.list_serializer_class is not None:
            serializer = self.list_serializer_class(data=query_params, partial=True)
            is_valid = serializer.is_valid()
            if not is_valid:
                raise ValidationError(serializer.errors)

            query_params = serializer.validated_data

        query_objects = self.get_query_obj(request=request)

        query_objects = self.get_search_and_filter_query(
            query_params=query_params,
            query_objects=query_objects,
        )

        objects = self.manager.list(
            query=query_objects, using=self.using(request=request)
        )
        if not objects:
            raise NoDataFoundError()

        return generate_response(data=self.get_list(objects=objects, request=request))

    def get_query_obj(self, request, **_):
        return {}

    def using(self, **kwargs):
        return None

    def get_with_pagination(self, request, query):
        """
        Retrieve object list with pagination based on query params provided in the request data.
        """

        serializer = self.list_serializer_class(data=query, partial=True)
        is_valid = serializer.is_valid()
        if not is_valid:
            raise ValidationError(serializer.errors)

        query_params = serializer.validated_data

        query_objects = self.get_query_obj(request=request)

        query_objects = self.get_search_and_filter_query(
            query_params=query_params,
            query_objects=query_objects,
        )

        pagination = {
            "page": query_params["page"],
            "page_size": query_params["page_size"],
        }

        objects, pagination = self.manager.list_with_pagination(
            query=query_objects,
            pagination=pagination,
            only=self.only_fields,
            order_by=self.order_by_fields,
            using=self.using(request=request),
        )

        if not objects:
            raise NoDataFoundError()

        return generate_response(
            data={
                "list": self.get_list(objects=objects, request=request),
                "pagination": pagination,
            }
        )

    def get_search_and_filter_query(self, query_params, query_objects):
        """
        Combine search and filter queries based on the provided query parameters.
        """
        if self.filter_fields:
            filter_query = self.filter_query(query_params=query_params)
            if filter_query:
                query_objects.update(filter_query)

        if self.search_fields:
            search_query = self.search_query(query_params=query_params)
            if search_query:
                query_objects["OR"] = search_query

        return query_objects
