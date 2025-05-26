from django.shortcuts import render


def index(request):
    plantilla_principal = {'title': 'PF Gaming'}
    return render(request, 'home/index.html', {
        'plantilla_principal': plantilla_principal
    })

def faq(request):
    plantilla_principal = {'title': 'Preguntas frecuentes'}
    return render(request, 'home/faq.html', {
        'plantilla_principal': plantilla_principal
    })