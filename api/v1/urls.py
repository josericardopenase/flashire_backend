# Django
from django.urls import path, include

urlpatterns = [
    path("users/", include("users.urls")),
    path("metrics/", include("metrics.urls")),
]
