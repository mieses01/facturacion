from django.shortcuts import render

# Create your views here.
def compania_list(request):
    return render(request, 'inventario/compania_list.html', {})