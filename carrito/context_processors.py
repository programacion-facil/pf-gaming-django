from .models import Carrito

def carrito_total_items(request):
    if request.user.is_authenticated:
        carrito = Carrito.objects.filter(usuario=request.user).first()
        total_items = sum(item.cantidad for item in carrito.items.all()) if carrito else 0
    else:
        carrito_sesion = request.session.get('carrito', {})
        total_items = sum(item['cantidad'] for item in carrito_sesion.values())
    return {'carrito_total_items': total_items}
