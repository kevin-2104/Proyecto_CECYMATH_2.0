from django.urls import path
from . import views

urlpatterns = [
    path("polinomios/", views.polinomios, name="polinomios"),
]