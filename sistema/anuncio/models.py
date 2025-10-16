from django.db import models
from django.contrib.auth.models import User
from veiculo.models import Veiculo
from anuncio.consts import OPCOES_STATUS

class Anuncio(models.Model):
   
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name='anuncios')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='anuncios')
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(max_length=1000)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quilometragem = models.IntegerField(help_text="Quilometragem em KM")
    status = models.CharField(max_length=10, choices=OPCOES_STATUS, default='ativo')
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    data_criacao = models.DateTimeField(auto_now_add=True)
    