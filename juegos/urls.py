from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='juegos.index'),
    path('<int:id>/', views.mostrar, name='juegos.mostrar'),
    # Rutas para las reseñas
    path('<int:juego_id>/resenas/crear/', views.crear_resena, name='resenas.crear'),
    path('<int:juego_id>/resenas/<int:resena_id>/editar/', views.editar_resena, name='resenas.editar'),
    path('<int:juego_id>/resenas/<int:resena_id>/eliminar/', views.eliminar_resena, name='resenas.eliminar'),
]
