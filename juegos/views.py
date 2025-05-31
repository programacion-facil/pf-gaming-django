from django.shortcuts import render, get_object_or_404
from .models import Juego, Genero, Plataforma
from django.db.models import Q

def index(request):
    query = request.GET.get('q', '').strip()
    juegos = Juego.objects.all().prefetch_related('generos', 'plataformas')

    if query:
        palabras = query.split()
        filtro = Q()
        for palabra in palabras:
            filtro |= (
                Q(nombre__icontains=palabra) |
                Q(descripcion__icontains=palabra) |
                Q(generos__nombre__icontains=palabra) |
                Q(plataformas__nombre__icontains=palabra)
            )
        juegos = juegos.filter(filtro).distinct()

    datos_plantilla = {
        'titulo': 'Catálogo de videojuegos',
        'juegos': juegos
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

