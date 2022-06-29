from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render #render faz a redenderização, converte phyton para html
from django.http import HttpResponse

def contato (request):
    return render (request, 'contato.html')

def mecax (request):
    return render (request, 'meca.html')

def marcas (request):
    return render (request, 'marcas.html')

def caduser (request):
    return render (request, 'caduser.html')

def vendercarro (request):
    return render (request, 'vendercarro.html')

def login (request):
    return render (request, 'login.html')

def home (request):
    return render (request, 'home.html')

def veiculo (request):
    return render (request, 'veiculos.html')