from django.db import models

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
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.TextField()
    generos = models.ManyToManyField(Genero, related_name='juegos')
    plataformas = models.ManyToManyField(Plataforma, related_name='juegos')

    def __str__(self):
        return self.nombre
