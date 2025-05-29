"""
This file is used to define the urls for the monitor app.
"""

# Third Party Library Imports
from django.urls import path

# Local Imports
from monitor import views


urlpatterns = [
    path("health", views.MonitorView.as_view(), name="monitor"),
]
