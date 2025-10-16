from django.forms import ModelForm
from anuncio.models import Anuncio

class FormularioAnuncio(ModelForm):
    """
    Formulário para o model Veículo
    """

    class Meta:
        model = Anuncio
        exclude = []