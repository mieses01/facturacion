from django.shortcuts import render
from .models import compania
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
def compania_list(request):
    Compania = compania.objects.all()
    return render(request, 'inventario/compania_list.html', {'Compania' : Compania})

class detail(generic.DetailView):
    model = compania
    template_name = 'inventario/compania_detail.html'

def compania_detail(request, compania_id):
    
    Compania = get_object_or_404(compania, pk=compania_id)
    return render(request, 'inventario/compania_detail.html', {'Compania': Compania})
