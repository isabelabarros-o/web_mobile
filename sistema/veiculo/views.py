from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from veiculo.models import Veiculo
from django.contrib.auth.mixins import LoginRequiredMixin
from veiculo.forms import FormularioVeiculo
from django.urls import reverse_lazy
from datetime import datetime
from django.views import View
from django.http import FileResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from veiculo.serializers import SerializadorVeiculo
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.generics import ListAPIView, DestroyAPIView

class ListarVeiculos(LoginRequiredMixin, ListView):
    model = Veiculo
    context_object_name = 'lista_veiculos'
    template_name = 'veiculo/listar.html'
    
    def get_queryset(self):
        return Veiculo.objects.all()
    

class CriarVeiculos(LoginRequiredMixin, CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class FotoVeiculo(View):
    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculo/fotos/{}'.format(arquivo))
            return FileResponse(veiculo.foto)
        except ObjectDoesNotExist:
                raise Http404("Veículo não possui foto.")
        except Exception as exception:
            raise exception
        
class EditarVeiculo(LoginRequiredMixin, UpdateView):
    """
    View para editar um veículo existente.
    """
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class DeletarVeiculos(LoginRequiredMixin, DeleteView):
    '''
    View para deletar um veículo existente.
    '''
    model = Veiculo
    template_name = 'veiculo/deletar.html'
    success_url = reverse_lazy('listar-veiculos')

class APIListarVeiculos(ListAPIView):
    '''
    View para listar os veículos (por meio da API REST).
    '''
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()
    
class APIDeletarVeiculo(DestroyAPIView):
    '''
    View para deletar um veículo (por meio da API REST).
    '''
    serializer_class = SerializadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Veiculo.objects.all()