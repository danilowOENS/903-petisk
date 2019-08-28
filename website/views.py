from django.shortcuts import render
from website.models import Pessoa

# Create your views here.

def index(request):

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = requerst.POST.get('sobrenome') 
        pessoa.data_nacimento = requerst.POST.get('data_nacimento') 
        pessoa.email = requerst.POST.get('email') 
        pessoa.str_cep = requerst.POST.get('str_cep') 
        pessoa.str_numero = requerst.POST.get('str_numero') 
        pessoa.complemento = requerst.POST.get('complemento') 
        pessoa.genero = requerst.POST.get('genero') 
        pessoa.telefone = requerst.POST.get('telefone') 
        pessoa.celular = requerst.POST.get('celular') 
        pessoa.motivo = requerst.POST.get('motivo') 
        pessoa.save()

        contexto = {
        'nome': pessoa.nome
        }
        return render(request, 'index.html', contexto)

    return render(request, 'index.html')