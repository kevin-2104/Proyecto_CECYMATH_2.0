from django.urls import path
from . import views

urlpatterns = [
    path("", views.ec_primer, name="ec_primer"),
]