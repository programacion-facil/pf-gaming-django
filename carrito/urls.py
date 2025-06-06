from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.indice_carrito, name='indice'),
    path('agregar/<int:juego_id>/', views.agregar_al_carrito, name='agregar'),
    path('eliminar/<int:juego_id>/', views.eliminar, name='eliminar'),
    path('limpiar/', views.limpiar_carrito, name='limpiar'),
]
