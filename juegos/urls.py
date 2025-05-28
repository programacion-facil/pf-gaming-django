from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='juegos.index'),
    path('<int:id>/', views.mostrar, name='juegos.mostrar'),
]
