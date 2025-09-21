from django.views.generic import ListView
from veiculo.models import veiculo

class ListarVeiculos(ListView):
    model = veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculo/listar.html'
    
    def get_queryset(self):
        return Veiculo.objects.all()

