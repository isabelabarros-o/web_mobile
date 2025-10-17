from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from anuncio.models import Anuncio
from veiculo.models import Veiculo
from django.contrib.auth.mixins import LoginRequiredMixin
from anuncio.forms import FormularioAnuncio
from django.urls import reverse_lazy


class ListarAnuncios(ListView):
    """
    View para listar todos os anúncios ativos.
    """
    model = Anuncio
    context_object_name = 'lista_anuncio'
    template_name = 'anuncio/listar.html'
   

class DetalheAnuncio(DetailView):
    """
    View para exibir detalhes de um anúncio específico.
    """
    model = Anuncio
    template_name = 'anuncio/detalhe_anuncio.html'
    context_object_name = 'anuncio'


class CriarAnuncio(LoginRequiredMixin, CreateView):
    """
    View para criar um novo anúncio.
    """
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/novo.html'
    success_url = reverse_lazy('listar-anuncios')

    def form_valid(self, form):
        """
        Define o usuário logado como autor do anúncio.
        """
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        veiculos_com_anuncios = Anuncio.objects.filter(status='ativo').values_list('veiculo_id', flat=True)
        form.fields['veiculo'].queryset = Veiculo.objects.exclude(id__in=veiculos_com_anuncios)
        return form

class EditarAnuncio(LoginRequiredMixin, UpdateView):
    """
    View para editar um anúncio existente.
    """
    model = Anuncio
    form_class = FormularioAnuncio
    template_name = 'anuncio/editar_anuncio.html'
    success_url = reverse_lazy('meus-anuncios')

    def get_queryset(self):
        """
        Permite editar apenas anúncios do usuário logado.
        """
        return Anuncio.objects.filter(usuario=self.request.user)


class DeletarAnuncio(LoginRequiredMixin, DeleteView):
    """
    View para apagar um anúncio.
    """
    model = Anuncio
    template_name = 'anuncio/deletar.html'
    success_url = reverse_lazy('meus-anuncios')

    def get_queryset(self):
        """
        Permite apagar apenas anúncios do usuário logado.
        """
        return Anuncio.objects.filter(usuario=self.request.user)