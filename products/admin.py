from django.contrib import admin
from .models import Category, Producer, Product

admin.site.register([Category, Producer, Product])
