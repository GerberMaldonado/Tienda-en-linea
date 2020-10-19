from django.urls import path
from .views import *

app_name = 'autenticacion'

urlpatterns = [
    path('registro/', VistaRegistro.as_view(), name="registro"),
    path('acceder/', acceder, name="acceder"),
    path('salir/', salir, name="salir"),
]
