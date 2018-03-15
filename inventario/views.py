from django.shortcuts import render
from .models import compania

# Create your views here.
def compania_list(request):
    Compania = compania.objects.all()
    return render(request, 'inventario/compania_list.html', {'Compania' : Compania})