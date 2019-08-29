from django.shortcuts import render
from website.models import Pessoa
from website.models import Ong

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


def pessoas(request):
    pessoas = Pessoa.objects.filter(ativo=True).all()
    
    contexto = {
        'pessoas': pessoas
    }
    return render(request, 'pessoas.html', contexto)


def cadastrar(request):

    if request.method == 'POST':
        Ong= Pessoa()
        Ong.nome = request.POST.get('nome')
        Ong.sobrenome = requerst.POST.get('sobrenome') 
        Ong.data_nacimento = requerst.POST.get('data_nacimento') 
        Ong.email = requerst.POST.get('email') 
        Ong.str_cep = requerst.POST.get('str_cep') 
        Ong.str_numero = requerst.POST.get('str_numero') 
        Ong.complemento = requerst.POST.get('complemento') 
        Ong.genero = requerst.POST.get('genero') 
        Ong.telefone = requerst.POST.get('telefone') 
        Ong.celular = requerst.POST.get('celular') 
        Ong.motivo = requerst.POST.get('motivo') 
        Ong.save()
        
        
        contexto = {
        'nome': Ong.nome
        }
        return render(request, 'index.html', contexto)

    return render(request, 'index.html')

    def ong(request):
    ong = ongs.objects.filter(ativo=True).all()
    
    contexto = {
        'ong': ong
    }
    return render(request, 'ongs.html', contexto)








