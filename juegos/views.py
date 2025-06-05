from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Juego, Genero, Plataforma, Resena
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

    resena_usuario = None
    if request.user.is_authenticated:
        resena_usuario = juego.resenas.filter(usuario=request.user).first()

    resenas = juego.resenas.all()
    total_resenas = resenas.count()
    if total_resenas > 0:
        suma_calificaciones = sum(r.calificacion for r in resenas)
        promedio_calificacion = suma_calificaciones / total_resenas
    else:
        promedio_calificacion = 0

    datos_plantilla = {
        'juego': juego,
        'resena_usuario': resena_usuario,
        'titulo': juego.nombre,
        'estrellas': list(range(1, 6)),
        'total_resenas': total_resenas,
        'promedio_calificacion': promedio_calificacion,
    }

    plantilla_principal = {
        'title': juego.nombre
    }

    return render(request, 'juegos/mostrar.html', {
        'datos_plantilla': datos_plantilla,
        'plantilla_principal': plantilla_principal
    })


@login_required
def crear_resena(request, juego_id):
    juego = get_object_or_404(Juego, pk=juego_id)
    if request.method == 'POST':
        texto = request.POST.get('texto', '').strip()
        calificacion = request.POST.get('calificacion')
        if texto and calificacion:
            Resena.objects.create(
                juego=juego,
                usuario=request.user,
                texto=texto,
                calificacion=calificacion
            )
    return redirect('juegos.mostrar', id=juego.id)

@login_required
def editar_resena(request, juego_id, resena_id):
    resena = get_object_or_404(Resena, pk=resena_id, juego_id=juego_id)
    if resena.usuario != request.user:
        return HttpResponseForbidden("No puedes editar esta resena.")

    if request.method == 'POST':
        resena.texto = request.POST.get('texto', resena.texto)
        resena.calificacion = request.POST.get('calificacion', resena.calificacion)
        resena.save()
        return redirect('juegos.mostrar', id=juego_id)

    datos_plantilla = {'resena': resena, 'juego': resena.juego}
    return render(request, 'juegos/review_edit.html', datos_plantilla)


@login_required
def eliminar_resena(request, juego_id, resena_id):
    resena = get_object_or_404(Resena, pk=resena_id, juego_id=juego_id)
    if resena.usuario != request.user:
        return HttpResponseForbidden("No puedes eliminar esta resena.")
    resena.delete()
    return redirect('juegos.mostrar', id=juego_id)


def detalle_juego(request, juego_id):
    juego = Juego.objects.get(id=juego_id)
    resena_usuario = None
    if request.user.is_authenticated:
        resena_usuario = juego.resenas.filter(usuario=request.user).first()
    datos_plantilla = {
        'juego': juego,
        'resena_usuario': resena_usuario,
    }
    return render(request, 'tu_template.html', {'datos_plantilla': datos_plantilla})
