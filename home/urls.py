from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home.index'),
    path('faq/', views.faq, name='home.faq'),
]