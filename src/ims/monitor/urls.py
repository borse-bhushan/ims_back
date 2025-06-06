"""
This file is used to define the urls for the monitor app.
"""

from django.urls import path

from utils.tenant_aware_path import add_to_tenant_aware_excluded_path_list

from monitor import views


urlpatterns = [
    path(
        add_to_tenant_aware_excluded_path_list("health"),
        views.MonitorView.as_view(),
        name="monitor",
    ),
]
