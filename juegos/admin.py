from django.contrib import admin
from .models import Juego, Plataforma, Genero

# Registra los modelos para que aparezcan en el panel de administración
admin.site.register(Juego)
admin.site.register(Plataforma)
admin.site.register(Genero)
