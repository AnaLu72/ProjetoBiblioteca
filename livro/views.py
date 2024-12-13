from .import views #importar o views do livro
from django.shortcuts import render, redirect, get_object_or_404 #importar o render e o redirect do django, para renderizar o template e redirecionar para outra página
from django.http import HttpResponse #importar o HttpResponse do django
from utilizadores.models import Utilizador #importar o modelo Utilizador
from .models import Livros, Categoria, Emprestimos #importar o modelo Livros
from .forms import RegistoLivro, CategoriaLivro #importar o formulário RegistoLivro
from django import forms #importar o forms do django
from datetime import date, datetime #importar o date e o datetime do datetime
from django.db.models import Q #importar o Q do django, Q (Query) é uma classe que permite fazer consultas mais complexas
from django.http import JsonResponse #importar o JsonResponse do django
from django.shortcuts import redirect
import json
from .models import Avaliacao

# Create your views here.

def home(request):
        if request.session.get('utilizador'): #se existir uma sessão com o utilizador
            utilizador = Utilizador.objects.get(id = request.session['utilizador']) #obter o utilizador com o id passado na url
            status_categoria = request.GET.get('registo_categoria') #obter o valor do parâmetro registo_categoria da url
            livros = Livros.objects.filter(utilizador = utilizador) #obter todos os livros do utilizador
            total_livros = livros.count() #obter o número de livros do utilizador
            form = RegistoLivro() #criar uma instância do formulário RegistoLivro
            form.fields['utilizador'].initial = request.session['utilizador'] #preencher o campo nome do formulário com o nome do utilizador
            form.fields['categoria'].queryset = Categoria.objects.filter(utilizador = utilizador) #preencher o campo categoria do formulário com a categoria com o id 1
            form_categoria = CategoriaLivro()
            utilizadores = Utilizador.objects.all() # obter todos os utilizadores

            livros_emprestar = Livros.objects.filter(utilizador = utilizador).filter(emprestado = False)
            livros_emprestados = Livros.objects.filter(utilizador = utilizador).filter(emprestado = True)   

            return render(request, 'home.html', {
                                'livros': livros, 
                                'utilizador_autenticado': request.session.get('utilizador'), #renderizar o template home.html e passar os livros para o template e o utilizador autenticado para o template
                                'form': form,
                                'status_categoria': 'status_categoria',
                                'form_categoria': form_categoria,
                                'utilizadores': utilizadores,
                                'livros_emprestar': livros_emprestar,
                                'total_livro': total_livros,
                                'livros_emprestados': livros_emprestados
                                }) #renderizar o template home.html e passar os livros para o template e o utilizador autenticado para o template
        else:
            return redirect('/auth/login/?status=2') #redirecionar para a página de login se o utilizador não estiver autenticado
        
def ver_livro(request, id): 
    if request.session.get('utilizador'):  # verificar se o utilizador está autenticado 
        livro = Livros.objects.get(id=id) # Recupera o livro ou retorna um erro 404 se não existir
        
        utilizador = Utilizador.objects.get(id = request.session['utilizador'])
        categoria_livro = Categoria.objects.filter(utilizador = request.session.get('utilizador')) #obter todas as categorias do utilizador
        emprestimos = Emprestimos.objects.filter(livro = livro) #obter todos os empréstimos do livro
        livros = Livros.objects.filter(utilizador = utilizador) #obter todos os livros do utilizador
        total_livros = livros.count() #obter o número de livros do utilizador
        form = RegistoLivro() #criar uma instância do formulário RegistoLivro
        form.fields['utilizador'].initial = request.session['utilizador'] #preencher o campo nome do formulário com o nome do utilizador
        form.fields['categoria'].queryset = Categoria.objects.filter(utilizador = utilizador) #preencher o campo categoria do formulário com a categoria com o id 1
        
        form_categoria = CategoriaLivro()
        utilizadores = Utilizador.objects.all()
        livros_emprestar = Livros.objects.filter(utilizador = utilizador, emprestado = False)
        livros_emprestados = Livros.objects.filter(utilizador = utilizador, emprestado = True)
            
        return render(request, 'ver_livro.html', {
                                'livro': livro,
                                'livros': livros,
                                'categoria_livro': categoria_livro, 
                                'emprestimos': emprestimos, 
                                'utilizador_autenticado': request.session.get('utilizador'), 
                                'form': form,
                                'id_livro': id,
                                'form_categoria': form_categoria,
                                'utilizadores': utilizadores,
                                'livros_emprestar': livros_emprestar,
                                'livros_emprestados': livros_emprestados
                                }) #renderizar o template ver_livro.html e passar para o template
    else:
        return HttpResponse('Esse livro não é seu!') #se o utilizador não estiver logado ou se o id do utilizador não for igual ao id do livro, retornar um erro
    return redirect('/auth/login/?status=2')   
          
   
def registar_livro(request):
    if request.method == 'POST':
        form = RegistoLivro(request.POST, request.FILES)  # Inclua request.FILES aqui
        if form.is_valid():
            form.save()  # Salva o livro no banco de dados
            return redirect('home')  # Redireciona para a página inicial ou outra
        else:
            return render(request, 'registar_livro.html', {'form': form})
    else:
        form = RegistoLivro()
        return render(request, 'registar_livro.html', {'form': form})

              
def excluir_livro(request, id): #criar a função excluir_livro que recebe um request e o id do livro
        livros = Livros.objects.get(id = id).delete() #obter o livro com o id passado na url
        return redirect('/livro/home') #redirecionar para a página home

def registar_categoria(request): #criar a função registar_categoria que recebe um request
    form = CategoriaLivro(request.POST) #criar uma instância do formulário CategoriaLivro com os dados do formulário
    nome = form.data['nome'] #obter o nome do formulário
    descricao = form.data['descricao'] #obter a descrição do formulário
    id_utilizador = request.POST.get('utilizador') #obter o id do utilizador
    if int(id_utilizador) == int(request.session.get('utilizador')): #verificar se o utilizador está logado e se o id do utilizador é igual ao id do livro
        user = Utilizador.objects.get(id = id_utilizador) #obter o utilizador com o id passado na url
        categoria = Categoria(nome = nome, descricao = descricao, utilizador_id = id_utilizador) #criar uma instância da classe Categoria com os dados do formulário
        categoria.save()
        return redirect('/livro/home?registo_categoria=1') #redirecionar para a página home
    else:
        return HttpResponse('Pare de tentar sabotar o sistema, isso não é correto!:(') #se o utilizador não estiver logado ou se o id do utilizador não for igual ao id do livro, retornar um erro
  
def registar_emprestimo(request):
    if request.method == 'POST':
        nome_emprestado = request.POST.get('nome_emprestado')
        nome_emprestado_anonimo = request.POST.get('nome_emprestado_anonimo')
        livro_emprestado = request.POST.get('livro_emprestado')
       #return HttpResponse(f"{nome_emprestado} | {nome_emprestado_anonimo} | {livro_emprestado}") -> teste
        
        if nome_emprestado_anonimo:
            emprestimo = Emprestimos(nome_emprestado_anonimo_id = nome_emprestado_anonimo, 
                                     id_livro = livro_emprestado)    
        else:
            emprestimo = Emprestimos(nome_emprestado_id = nome_emprestado,
                                     id_livro = livro_emprestado)
        emprestimo.save()

        livro = Livros.objects.get(id = livro_emprestado)
        livro.emprestado = True
        livro.save()

        return redirect('/livro/home')
    #return HttpResponse('Empréstimo realizado com sucesso!')
    

def devolver_livro(request):
            id = request.POST.get('id_livro_devolver') # Obter o ID do livro a ser devolvido
            livro_devolver = Livros.objects.get(id = id) # Obter o livro a ser devolvido
            livro_devolver.emprestado = False # Definir o estado do livro como não emprestado
            livro_devolver.save()

            emprestimo_devolver = Emprestimos.objects.get(Q(livro=livro_devolver) & Q(data_devolucao = None)) # Obter o empréstimo associado ao livro a ser devolvido
            emprestimo_devolver.data_devolucao = datetime.now() # Definir a data de devolução como a data atual
            emprestimo_devolver.save() # Salvar as alterações
            
            return redirect('/livro/home') # Redirecionar para a página inicial

def alterar_livro(request):
    id_livro = request.POST.get('id_livro')
    nome_livro = request.POST.get('nome_livro')
    autor = request.POST.get('autor')
    co_autor = request.POST.get('co_autor')
    id_categoria = request.POST.get('id_categoria')
    categoria = Categoria.objects.get(id = id_categoria)

    livro = Livros.objects.get(id = id_livro)
    if livro.utilizador == request.session['utilizador']:
        livro.nome = nome_livro
        livro.autor = autor
        livro.co_autor = co_autor
        livro.categoria = categoria
        livro.save()
        return redirect(f'/livro/ver_livro/{id_livro}') 
    else:
        return redirect('/auth/sair') # Redirecionar para a página inicial
        
def meus_emprestimos(request):
    utilizador = Utilizador.objects.get(id = request.session['utilizador'])
    emprestimos = Emprestimos.objects.filter(nome_emprestado = utilizador)
    
    form = RegistoLivro()
    form.fields['utilizador'].initial = request.session['utilizador'] #preencher o campo nome do formulário com o nome do utilizador
    form.fields['categoria'].queryset = Categoria.objects.filter(utilizador = utilizador) #preencher o campo categoria do formulário com a categoria com o id 1
    form_categoria = CategoriaLivro()
    
    return render(request, 'meus_emprestimos.html', {'utilizador_autenticado': request.session['utilizador'], 
                                                      'emprestimos': emprestimos, 'form': form, 
                                                      'form_categoria': form_categoria})



def historico_emprestimos(request): 
    emprestimos = Emprestimos.objects.all() 
    for emprestimo in emprestimos: 
        print(f"Emprestimo ID: {emprestimo.id}, Data Empréstimo: {emprestimo.data_emprestimo}, Data Devolução: {emprestimo.data_devolucao}") 
        return render(request, 'historico_emprestimos.html', {'emprestimos': emprestimos})

def processa_avaliacao(request):
    if request.method == 'POST':
        livro_id = request.POST.get('livro')
        avaliacao = request.POST.get('avaliacao')

        # Verifique se ambos os campos são enviados
        if livro_id and avaliacao:
            livro = Livros.objects.get(id=livro_id)

            #Cria uma instância do modelo Avaliacao
            Avaliacao.objects.create(livro=livro, avaliacao=avaliacao)

            return redirect('historico_emprestimos')  # Redireciona após sucesso
        else:
            # Caso não tenha enviado o livro ou a avaliação, retorna erro
            return JsonResponse({'status': 'error', 'message': 'Dados inválidos recebidos!'}, status=400)
    else:
        # Se não for um POST, retorna erro de método não permitido
        return JsonResponse({'status': 'error', 'message': 'Método não permitido!'}, status=405)




        

    


    
