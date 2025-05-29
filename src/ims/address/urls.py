"""
Address URL Configuration
This module contains the URL routing for the Addresss app.
"""

from django.urls import path, include

urlpatterns = [path("", include("address.routes.address"))]
