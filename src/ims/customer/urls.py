from django.urls import path, include

urlpatterns = [
    path("", include("customer.routes.customer")),
]
