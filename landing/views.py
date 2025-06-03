from django.shortcuts import render
from productos.models import Producto

def landing_page(request):
    Productos = Producto.objects.all()
    return render(request, 'landing/landing.html', {
        'productos': Productos
    })
