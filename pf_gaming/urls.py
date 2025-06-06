from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('juegos/', include('juegos.urls')),
    path('cuentas/', include('cuentas.urls')), 
    path('carrito/', include('carrito.urls', namespace='carrito')),
]
