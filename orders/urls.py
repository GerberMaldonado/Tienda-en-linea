from django.urls import path
from .views import *
from fact.views import CrearClient, Create_Client
from django.contrib.auth.decorators import login_required


urlpatterns = [
    #path('crear-facturacion/', CrearClient, name='CrearClient'),
    path('proceso-facturacion/', Create_Client, name='process_fact'),    
    path('proceso-pedido/', process_order, name='process_order'),
    path('me/', login_required(OrderList.as_view(), login_url='/autenticacion/acceder'), name='order_list'),
    path('<int:pk>', login_required(OrderDetail.as_view(), login_url='/autenticacion/acceder'), name='order_detail'),
]
