from django.urls import path
from . import views

urlpatterns = [
    path("multiplicacion/", views.multiplicacion, name="multiplicacion"),
]