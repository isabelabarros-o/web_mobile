from django.urls import path
from anuncio.views import *

urlpatterns = [
    path('', ListarAnuncios.as_view(), name='listar-anuncios'),
    path('novo/', CriarAnuncio.as_view(), name='criar-anuncio'),
    path('editar/<int:pk>/', EditarAnuncio.as_view(), name='editar-anuncio'),
    path('deletar/<int:pk>/', DeletarAnuncio.as_view(), name='deletar-veiculos'),
    path('<int:pk>/', DetalheAnuncio.as_view(), name='detalhe-anuncio'),
]