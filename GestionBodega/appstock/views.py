from multiprocessing import context
from django.shortcuts import render
from .models import productos

def stock(request):
    product = productos.objects.all()
    context = {'lista': 'Lista de Productos', 'prods': product}
    return render(request, 'catalogo.html', context)
    
