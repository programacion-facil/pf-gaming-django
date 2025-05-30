from django.shortcuts import render, get_object_or_404
from .models import Juego, Genero, Plataforma


def index(request):
    juegos = Juego.objects.all().prefetch_related('generos', 'plataformas')
    datos_plantilla = {
        'titulo': 'Catálogo de videojuegos',
        'juegos': juegos  # Ahora es un QuerySet con objetos Juego y relaciones precargadas
    }
    plantilla_principal = {
        'title': 'Catálogo de videojuegos'
    }
    return render(request, 'juegos/index.html', {
        'datos_plantilla': datos_plantilla,
        'plantilla_principal': plantilla_principal
    })


def mostrar(request, id):
    juego = get_object_or_404(Juego.objects.prefetch_related('generos', 'plataformas'), pk=id)

    datos_plantilla = {
        'juego': juego,
        'titulo': juego.nombre
    }
    plantilla_principal = {
        'title': juego.nombre
    }
    return render(request, 'juegos/mostrar.html', {
        'datos_plantilla': datos_plantilla,
        'plantilla_principal': plantilla_principal
    })

