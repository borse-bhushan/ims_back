"""
This file is used to define the urls for the monitor app.
"""

from django.urls import path

from monitor import views


urlpatterns = [
    path("health", views.MonitorView.as_view(), name="monitor"),
]
