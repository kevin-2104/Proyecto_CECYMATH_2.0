from django.urls import path
from .views import sume

urlpatterns = [
    path('suma/', sume, name='suma'),
]