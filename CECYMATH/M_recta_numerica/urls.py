from django.urls import path
from . import views

urlpatterns = [
    path("recta/", views.recta, name="recta"),
]