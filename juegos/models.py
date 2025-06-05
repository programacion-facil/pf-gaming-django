from django.db import models
from django.contrib.auth.models import User

class Plataforma(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    generos = models.ManyToManyField(Genero)
    plataformas = models.ManyToManyField(Plataforma)

    def __str__(self):
        return self.nombre
    
class Resena(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name='resenas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    calificacion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1-5 estrellas
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['juego', 'usuario'], name='unique_review_per_user_per_game')
        ]

    def __str__(self):
        return f"{self.usuario.username} - {self.juego.nombre} ({self.calificacion}⭐)"
