from django.shortcuts import render, redirect #importar o render e o redirect do django, para renderizar a página e redirecionar para outra página
from django.http import HttpResponse #importar o HttpResponse para acessar o request.POST
from .models import Utilizador #importar o modelo Utilizador do app utilizadores
from hashlib import sha256 #importa o sha256 para criptografar a senha


def login(request):
    if request.session.get('utilizador'): #se existir uma sessão com o utilizador
        return redirect('/livro/home/') #redirecionar para a página home
    status = request.GET.get('status') #request.GET.get('status') significa acessar o request.GET e pegar o valor do status
    return render(request, 'login.html', {'status' : status}) #return HttpResponse significa retornar uma string html

def registo(request):
    if request.session.get('utilizador'): #se existir uma sessão com o utilizador
        return redirect('/livro/home/') #redirecionar para a página home
    status = request.GET.get('status') #request.GET.get('status') significa acessar o request.GET e pegar o valor do status
    return render(request, 'registo.html', {'status': status}) #render significa retornar uma página html

def validar_registo(request): 
    nome = request.POST.get('nome') #request.POST.get('nome') significa acessar o request.POST e pegar o valor do nome
    password = request.POST.get('password')
    email = request.POST.get('email')

    utilizador = Utilizador.objects.filter(email = email) #filter significa filtrar os utilizadores que tem o email igual ao email que foi digitado

    if len(nome.strip()) == 0 or len(email.strip()) == 0: #len(nome.strip()) == 0 significa que se o len(nome) for igual a 0 ou se o len(email) for igual a 0
        return redirect('/auth/registo/?status=1') #redirect significa redirecionar para outra página
    
    if len(password) < 8: #len(password) < 8 significa que se a senha for menor que 8 caracteres
        return redirect('/auth/registo/?status=2') #redirect significa redirecionar para outra página
    
    if len(utilizador) > 0: #len(utilizador) > 0 significa que se o len(utilizador) for maior que 0, ou seja, se o utilizador já existir
        return redirect('/auth/registo/?status=3') #redirect significa redirecionar para outra página 
    
    try:
        password = sha256(password.encode('utf-8')).hexdigest() #sha256 significa criptografar a senha em md5
        utilizador = Utilizador(nome = nome,
                                 email = email, 
                                 password = password) #utilizador significa que é um objeto do tipo Utilizador
        utilizador.save() #save significa salvar o objeto utilizador

        return redirect('/auth/registo/?status=0') #redirect significa redirecionar para outra página
    except:
        return redirect('/auth/registo/?status=4') #redirect significa redirecionar para outra página
    

    return HttpResponse(f"{nome} {email} {password}") #HttpResponse significa retornar uma string html

def validar_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    password = sha256(password.encode()).hexdigest()

    utilizador = Utilizador.objects.filter(email = email).filter(password = password)
    
    if len(utilizador) == 0:
        return redirect('/auth/login/?status=1')
    elif len(utilizador) > 0:
        request.session['utilizador'] = utilizador[0].id
        return redirect(f'/livro/home')

    return HttpResponse(f"{email} {password}")

def logout(request):
    request.session.flush() #flush significa limpar a sessão
    return redirect('/auth/login/')
