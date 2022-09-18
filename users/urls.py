# Django
from django.urls import path, include
from users.views import rabbit_test

urlpatterns = [path("rabbit_test/", rabbit_test)]
