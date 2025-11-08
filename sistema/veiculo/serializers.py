from rest_framework import serializers
from veiculo.models import Veiculo

class SerializadorVeiculo(serializers.ModelSerializer):
    """
    Serializador para o modelo Veículo
    """
    cor_nome = serializers.CharField(source='get_cor_display')
    combustivel_nome = serializers.CharField(source='get_combustivel_display')
    marca_nome = serializers.CharField(source='get_marca_display')
    
    class Meta:
        model = Veiculo
        exclude = []  