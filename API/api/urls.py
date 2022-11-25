from django.urls import path, include
from .view import helloAPI

urlpatterns = [
    path("hello/", helloAPI),
    ]