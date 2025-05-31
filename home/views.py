from django.shortcuts import render
from juegos.models import Juego

def index(request):
    juegos_por_categoria = {
        'Más vendidos': Juego.objects.filter(id__in=[1, 2, 3]),
        'Recomendados': Juego.objects.filter(id__in=[6, 1, 7]),
        'Novedades': Juego.objects.filter(id__in=[4, 9, 10]),
    }

    return render(request, 'home/index.html', {
        'categorias': juegos_por_categoria
    })


def faq(request):
    plantilla_principal = {'title': 'Preguntas frecuentes'}
    return render(request, 'home/faq.html', {
        'plantilla_principal': plantilla_principal
    })