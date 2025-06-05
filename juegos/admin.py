from django.contrib import admin
from .models import Juego, Plataforma, Genero, Resena

# Registra los modelos para que aparezcan en el panel de administración
admin.site.register(Juego)
admin.site.register(Plataforma)
admin.site.register(Genero)

@admin.register(Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('juego', 'usuario', 'calificacion', 'creado_en')
    list_filter = ('calificacion', 'creado_en')
    search_fields = ('texto', 'usuario__username', 'juego__nombre')
