# -*- coding: utf-8 *-
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.shortcuts import render

class Login(View):
    """
    Class Based View para autenticação de usuários.
    """

    def get(self,request):
        contexto = {}
        return render(request, 'autenticacao.html', contexto)
    
    def post(self,request):
        # Obtem as credenciais de autenticação
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Usuário autenticado com sucesso!")
                #return redirect('home')
        else:
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário ou senha inválidos!'})