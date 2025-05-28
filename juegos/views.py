from django.shortcuts import render
from django.http import HttpResponse

juegos = [
    {
        'id': 1,
        'nombre': 'Grand Theft Auto VI',
        'precio': 69.99,
        'descripcion': 'La esperada nueva entrega de GTA, con una historia intensa y mundo abierto impresionante.',
        'genero': 'Acción / Aventura',
        'plataformas': ['PS5', 'Xbox Series X/S']
    },
    {
        'id': 2,
        'nombre': 'Elden Ring: Shadow of the Erdtree',
        'precio': 49.99,
        'descripcion': 'Expansión masiva del aclamado RPG de mundo abierto, con nuevas zonas y jefes.',
        'genero': 'RPG / Acción',
        'plataformas': ['PC', 'PS5', 'Xbox Series X/S']
    },
    {
        'id': 3,
        'nombre': 'The Legend of Zelda: Echoes of the Past',
        'precio': 59.99,
        'descripcion': 'Una nueva aventura épica de Zelda que expande el universo de Breath of the Wild.',
        'genero': 'Aventura / Puzzle',
        'plataformas': ['Nintendo Switch']
    },
    {
        'id': 4,
        'nombre': 'Starfield',
        'precio': 59.99,
        'descripcion': 'Exploración espacial y RPG de próxima generación por Bethesda.',
        'genero': 'RPG / Ciencia ficción',
        'plataformas': ['PC', 'Xbox Series X/S']
    },
    {
        'id': 5,
        'nombre': 'Hogwarts Legacy',
        'precio': 59.99,
        'descripcion': 'Explora el mundo mágico de Harry Potter en este RPG de mundo abierto ambientado en el siglo XIX.',
        'genero': 'RPG / Aventura',
        'plataformas': ['PC', 'PS5', 'Xbox Series X/S']
    },
    {
        'id': 6,
        'nombre': 'Resident Evil 4 Remake',
        'precio': 49.99,
        'descripcion': 'Reimaginación moderna del clásico survival horror con gráficos y mecánicas renovadas.',
        'genero': 'Terror / Acción',
        'plataformas': ['PC', 'PS5', 'Xbox Series X/S']
    },
    {
        'id': 7,
        'nombre': 'Final Fantasy XVI',
        'precio': 69.99,
        'descripcion': 'Un nuevo capítulo en la legendaria saga de RPG con un enfoque más orientado a la acción.',
        'genero': 'RPG / Fantasía',
        'plataformas': ['PS5']
    },
    {
        'id': 8,
        'nombre': 'Spider-Man 2',
        'precio': 69.99,
        'descripcion': 'Continúa la aventura de Peter Parker y Miles Morales en una épica historia de superhéroes.',
        'genero': 'Acción / Aventura',
        'plataformas': ['PS5']
    },
    {
        'id': 9,
        'nombre': 'Forza Motorsport',
        'precio': 59.99,
        'descripcion': 'Simulación de carreras con gráficos de última generación y física realista.',
        'genero': 'Carreras / Simulación',
        'plataformas': ['PC', 'Xbox Series X/S']
    },
    {
        'id': 10,
        'nombre': 'Metroid Prime 4',
        'precio': 59.99,
        'descripcion': 'El regreso de Samus Aran en una nueva aventura de exploración y combate en primera persona.',
        'genero': 'Acción / Ciencia ficción',
        'plataformas': ['Nintendo Switch']
    },
]

def index(request):
    datos_plantilla = {
        'titulo': 'Catálogo de videojuegos',
        'juegos': juegos
    }
    plantilla_principal = {
        'title': 'Catálogo de videojuegos'
    }
    return render(request, 'juegos/index.html', {
        'datos_plantilla': datos_plantilla,
        'plantilla_principal': plantilla_principal
    })

def mostrar(request, id):
    juego = next((j for j in juegos if j['id'] == id), None)
    if not juego:
        return HttpResponse("<h1>Juego no encontrado</h1><p>El juego solicitado no existe.</p>")
    
    datos_plantilla = {
        'juego': juego,
        'titulo': juego['nombre']
    }
    plantilla_principal = {
        'title': juego['nombre']
    }
    return render(request, 'juegos/mostrar.html', {
        'datos_plantilla': datos_plantilla,
        'plantilla_principal': plantilla_principal
    })
