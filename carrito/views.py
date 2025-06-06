from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from juegos.models import Juego
from .models import Carrito, ItemCarrito

# ---- AGREGAR ----

def agregar_al_carrito(request, juego_id):
    juego = get_object_or_404(Juego, pk=juego_id)

    if request.user.is_authenticated:
        # Carrito persistente
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        item, created = ItemCarrito.objects.get_or_create(carrito=carrito, juego=juego)
        if not created:
            item.cantidad += 1
            item.save()
    else:
        # Carrito en sesión
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

# ---- MOSTRAR ----

def indice_carrito(request):
    juegos = []
    total = 0

    if request.user.is_authenticated:
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        items = carrito.items.select_related('juego').all()

        for item in items:
            subtotal = item.subtotal()
            total += subtotal
            juegos.append({
                'id': item.juego.id,
                'nombre': item.juego.nombre,
                'precio': float(item.juego.precio),
                'cantidad': item.cantidad,
                'subtotal': subtotal,
            })

    else:
        carrito = request.session.get('carrito', {})
        for juego_id_str, item in carrito.items():
            subtotal = item['precio'] * item['cantidad']
            total += subtotal
            juegos.append({
                'id': juego_id_str,
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

# ---- LIMPIAR ----

def limpiar_carrito(request):
    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()
        if carrito:
            carrito.items.all().delete()
            messages.success(request, "El carrito ha sido vaciado.")
        else:
            messages.info(request, "El carrito ya estaba vacío.")
    else:
        if 'carrito' in request.session:
            del request.session['carrito']
            messages.success(request, "El carrito ha sido vaciado.")
        else:
            messages.info(request, "El carrito ya estaba vacío.")

    return redirect('carrito:indice')

# ---- ELIMINAR ----

def eliminar(request, juego_id):
    if request.user.is_authenticated:
        carrito = get_object_or_404(Carrito, usuario=request.user)
        try:
            item = ItemCarrito.objects.get(carrito=carrito, juego_id=juego_id)
            item.delete()
            messages.success(request, "Juego eliminado del carrito.")
        except ItemCarrito.DoesNotExist:
            messages.warning(request, "El juego no estaba en el carrito.")
    else:
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
