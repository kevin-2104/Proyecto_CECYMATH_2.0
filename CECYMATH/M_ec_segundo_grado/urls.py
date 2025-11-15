from django.urls import path
from . import views

urlpatterns = [
    path("", views.ec_segundo, name="ec_segundo")
]
