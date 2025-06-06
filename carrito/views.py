from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from juegos.models import Juego

def agregar_al_carrito(request, juego_id):
    juego = get_object_or_404(Juego, pk=juego_id)
    carrito = request.session.get('carrito', {})

    juego_id_str = str(juego.id)
    if juego_id_str in carrito:
        carrito[juego_id_str]['cantidad'] += 1
    else:
        carrito[juego_id_str] = {
            'nombre': juego.nombre,
            'precio': float(juego.precio),
            'cantidad': 1
        }

    request.session['carrito'] = carrito
    request.session.modified = True
    messages.success(request, f"'{juego.nombre}' añadido al carrito.")
    return redirect('juegos.index')

def indice_carrito(request):
    carrito = request.session.get('carrito', {})
    juegos = []
    total = 0

    for juego_id_str, item in carrito.items():
        subtotal = item['precio'] * item['cantidad']
        total += subtotal
        juegos.append({
            'id': juego_id_str,  # <-- esto es lo que faltaba
            'nombre': item['nombre'],
            'precio': item['precio'],
            'cantidad': item['cantidad'],
            'subtotal': subtotal,
        })

    datos_plantilla = {
        'juegos': juegos,
        'total': total,
        'titulo': 'Carrito de compras'
    }

    plantilla_principal = {
        'title': 'Carrito de compras'
    }

    return render(request, 'carrito/index.html', {
        'datos_plantilla': datos_plantilla,
        'plantilla_principal': plantilla_principal
    })


def limpiar_carrito(request):
    if 'carrito' in request.session:
        del request.session['carrito']
        messages.success(request, "El carrito ha sido vaciado.")
    else:
        messages.info(request, "El carrito ya estaba vacío.")
    return redirect('carrito:indice')

def eliminar(request, juego_id):
    carrito = request.session.get('carrito', {})

    juego_id_str = str(juego_id)
    if juego_id_str in carrito:
        del carrito[juego_id_str]
        request.session['carrito'] = carrito
        request.session.modified = True
        messages.success(request, "Juego eliminado del carrito.")
    else:
        messages.warning(request, "El juego no estaba en el carrito.")

    return redirect('carrito:indice')
