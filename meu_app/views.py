from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
from .models import Sala
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def entrar(request):
    if request.method == 'GET':
        return render(request, 'entrar.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('password')

        sala = Sala.objects.filter(Q(nome=nome) & Q(senha=senha)).first()
        if sala:
            return redirect(reverse('chat', args=(sala.nome, )))
        else:
            return HttpResponse('Sala errada')
        
def chat(request, nome):
    return render(request, 'chat.html', {'nome': nome})