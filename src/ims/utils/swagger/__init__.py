"""
Swagger utility functions and classes for FastAPI applications.
These functions help in generating OpenAPI documentation for FastAPI endpoints.
"""

from .response import (
    responses_200,
    responses_400,
    responses_401,
    responses_404,
    responses_500,
    responses_400_example,
    responses_401_example,
    responses_404_example,
    responses_500_example,
    SuccessResponseSerializer,
    PaginationSerializer
)

__all__ = [
    "responses_200",
    "responses_400",
    "responses_401",
    "responses_404",
    "responses_500",
    "responses_400_example",
    "responses_401_example",
    "responses_404_example",
    "responses_500_example",
    "SuccessResponseSerializer",
    "PaginationSerializer"
]
