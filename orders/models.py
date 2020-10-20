from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F, Sum, FloatField
from products.models import Product

User = get_user_model()

class Client(models.Model):
    name = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    dpi = models.CharField(max_length=12)
    number = models.CharField(max_length=15)    
    address = models.CharField(max_length=200)
    nit = models.IntegerField()
    saldo = models.FloatField()
    limit_credit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'client'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total(self):
        return self.orderline_set.aggregate(
            total=Sum(F("product__price") * F("quantity"), output_field=FloatField())
        )["total"] or FloatField(0)

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['id']

class OrderLine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

    class Meta:
        db_table = 'orderlines'
        verbose_name = 'No. pedido'
        verbose_name_plural = 'No. pedidos'
        ordering = ['id']
