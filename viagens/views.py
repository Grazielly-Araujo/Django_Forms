from viagens.forms import ViagemForms
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def index(request):
    form = ViagemForms()
    contexto = {'form':form}
    return render(request, 'index.html', contexto)

# Create your views here.
