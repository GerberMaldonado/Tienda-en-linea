from django.contrib import admin
from .models import OrderLine, Order, Client

admin.site.register([Order, OrderLine, Client])
