from django.shortcuts import render
from website.models import Pessoa
from website.models import Ong

# Create your views here.

def index(request):

    if request.method == 'POST':
        pessoa = Pessoa()
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome') 
        pessoa.data_nascimento = request.POST.get('data_nascimento') 
        pessoa.email = request.POST.get('email') 
        pessoa.str_cep = request.POST.get('str_cep') 
        pessoa.str_numero = request.POST.get('str_numero') 
        pessoa.complemento = request.POST.get('complemento') 
        pessoa.genero = request.POST.get('genero') 
        pessoa.telefone = request.POST.get('telefone') 
        pessoa.celular = request.POST.get('celular') 
        pessoa.motivo = request.POST.get('motivo') 
        pessoa.save()

        contexto = {
            'nome': pessoa.nome
        }
        return render(request, 'index.html', contexto)

    return render(request, 'index.html')


def pessoas(request):
    pessoas = Pessoa.objects.filter(ativo=True).all()
    
    contexto = {
        'pessoas': pessoas
    }
    return render(request, 'pessoas.html', contexto)


def cadastrar(request):

    if request.method == 'POST':
        x= Ong()
        x.nome = request.POST.get('nome')
        x.sobrenome = request.POST.get('sobrenome') 
        x.data_nacimento = request.POST.get('data_nacimento') 
        x.email = request.POST.get('email') 
        x.str_cep = request.POST.get('str_cep') 
        x.str_numero = request.POST.get('str_numero') 
        x.complemento = request.POST.get('complemento') 
        x.genero = request.POST.get('genero') 
        x.telefone = request.POST.get('telefone') 
        x.celular = request.POST.get('celular') 
        x.motivo = request.POST.get('motivo') 
        x.save()
        
        
        contexto = {
        'nome': x.nome
        }
        return render(request, 'cadastro_de_ong.html', contexto)

    return render(request, 'cadastro_de_ong.html')

def ong_cadastro(request):
    o = Ong.objects.all()
    
    contexto = {
        'ong': o
    }
    return render(request, 'ongs.html', contexto)








