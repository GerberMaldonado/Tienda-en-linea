from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('home.urls')),
    path('acerca-de/', include('about.urls')),
    path('contactanos/', include('contac.urls')),
    path('facturacion/', include('fact.urls')),
    path('administracion/', include('administracion.urls')),    
    path('admin/', admin.site.urls),
    path('autenticacion/', include('autenticacion.urls')),
    path('productos/', include('products.urls')),
    path('carrito/', include('cart.urls')),
    path('pedidos/', include('orders.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)