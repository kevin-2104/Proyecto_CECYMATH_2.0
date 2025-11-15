from django.urls import path
from . import views

urlpatterns = [
    path("", views.multiplicacion, name="multiplicacion")
]
