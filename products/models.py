from django.db import models

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=300)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-id']

# Producer Model
class Producer(models.Model):
    name = models.CharField(max_length=300)
    available = models.BooleanField(default=False)
    number = models.CharField(max_length=15)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'producers'
        verbose_name = 'Fabricante'
        verbose_name_plural = 'Fabricantes'
        ordering = ['-id']

        
# Product Model
class Product(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', blank=True)
    excerpt = models.TextField(max_length=200, verbose_name='Extracto')
    detail = models.TextField(max_length=1000, verbose_name='Información del producto')
    price = models.FloatField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'products'
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['id']
