
from django.shortcuts import render
from . import models

# Create your views here.
def inventario(request):
    prods = models.Producto.objects.all()
    return render(request, "html", {"prods" : prods})
# Create your views here.
