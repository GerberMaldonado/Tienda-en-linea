from django.urls import path
from .views import *

app_name = "cart"

urlpatterns = [
    path('agregar_producto/<int:product_id>/', add_product, name='add_product'),
    path('eliminar_producto/<int:product_id>/', remove_product, name='remove_product'),
    path('decremento_producto/<int:product_id>/', decrement_product, name='decrement_product'),
    path('limpiar/', clear_cart, name='clear_cart'),
]
