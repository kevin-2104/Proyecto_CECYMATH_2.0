"""
URL configuration for CECYMATH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('core.urls')),
    path('M_ar_y_p_fig_planas/', include('M_ar_y_p_fig_planas.urls')),
    path('M_divicion/', include('M_divicion.urls')),
    path('M_ec_primer_grado/', include('M_ec_primer_grado.urls')),
    path('M_ec_segundo_grado/', include('M_ec_segundo_grado.urls')),
    path('M_factorizacion/', include('M_factorizacion.urls')),
    path('M_jer_operaciones/', include('M_jer_operaciones.urls')),
    path('M_multiplicacion/', include('M_multiplicacion.urls')),
    path('M_op_polinomios/', include('M_op_polinomios.urls')),
    path('M_recta_numérica/', include('M_recta_numerica.urls')),
    path('M_resta/', include('M_resta.urls')),
    path('M_suma/', include('M_suma.urls')),
]
