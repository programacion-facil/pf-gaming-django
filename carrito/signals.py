from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.contrib import messages
from .models import Carrito, ItemCarrito
from juegos.models import Juego

@receiver(user_logged_in)
def fusionar_carrito_sesion_con_db(sender, user, request, **kwargs):
    carrito_sesion = request.session.get('carrito', {})
    if not carrito_sesion:
        return  # No hay nada que fusionar

    carrito_db, created = Carrito.objects.get_or_create(usuario=user)

    for juego_id_str, item_data in carrito_sesion.items():
        juego_id = int(juego_id_str)
        juego = Juego.objects.get(pk=juego_id)

        item_db, created = ItemCarrito.objects.get_or_create(carrito=carrito_db, juego=juego)
        if created:
            item_db.cantidad = item_data['cantidad']
        else:
            item_db.cantidad += item_data['cantidad']
        item_db.save()

    # Vaciar carrito de sesión después de fusionar
    del request.session['carrito']
    request.session.modified = True

    messages.info(request, "Se han añadido los juegos del carrito de invitado a tu carrito de usuario.")
