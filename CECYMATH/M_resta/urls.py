from django.urls import path
from . import views

urlpatterns = [
    path("resta/", views.resta, name="resta"),
]
