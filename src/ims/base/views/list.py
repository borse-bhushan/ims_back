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
    list_serializer_class = QuerySerializer

    @classmethod
    def get_method_view_mapping(cls):
        return {constants.GET: "list_all"}

    def get_list(self, objects, **_):
        """
        Convert a list of objects to a dictionary format.
        """
        return [obj.to_dict() for obj in objects]

    def list_all(self, request):
        """
        Retrieve object list based query params provided in the request data.
        Args:
            request (Request): The HTTP request object containing the data.
        Returns:
            object: The list of retrieved objects if found.
        """

        query = request.query_params.dict()

        if self.is_pagination:

            serializer = self.list_serializer_class(data=query)
            is_valid = serializer.is_valid()
            if not is_valid:
                raise ValidationError(serializer.errors)

            query_params = serializer.validated_data

            pagination = {
                "page": query_params["page"],
                "page_size": query_params["page_size"],
            }

            objects, pagination = self.manager.list_with_pagination(
                query={},
                pagination=pagination,
            )
            if not objects:
                raise NoDataFoundError()

            return generate_response(
                data={
                    "list": self.get_list(objects=objects, request=request),
                    "pagination": pagination,
                }
            )

        if self.list_serializer_class:
            serializer = self.list_serializer_class(data=query)
            is_valid = serializer.is_valid()
            if not is_valid:
                raise ValidationError(serializer.errors)

            query = serializer.validated_data

        query.pop("page", None)
        query.pop("page_size", None)

        objects = self.manager.list(query=query)
        if not objects:
            raise NoDataFoundError()

        return generate_response(data=self.get_list(objects=objects, request=request))
