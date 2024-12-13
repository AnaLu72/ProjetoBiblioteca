from django.urls import path #importar o path do django, permite criar rotas e o include para incluir outros arquivos de urls
from . import views #significa que é do mesmo diretório, ou seja, do próprio diretório livro, o . significa que é do mesmo diretório

urlpatterns = [
    path('home/', views.home, name='home'), #cria a rota home e chama a função home do arquivo views.py
    path('ver_livro/<int:id>/', views.ver_livro, name='ver_livro'), #url dinâmica, cria a rota ver_livro e chama a função ver_livro do arquivo views.py, é necessário passar o id do livro como parâmetro
    path('registar_livro/', views.registar_livro, name='registar_livro'), #cria a rota registar_livro e chama a função registar_livro do arquivo views.py
    path('excluir_livro/<int:id>/', views.excluir_livro, name='excluir_livro'), #cria a rota excluir_livro e chama a função excluir_livro do arquivo views.py, é necessário passar o id do livro como parâmetro
    path('registar_categoria/', views.registar_categoria, name='registar_categoria'), #cria a rota registar_categoria e chama a função registar_categoria do arquivo views.py
    path('registar_emprestimo/', views.registar_emprestimo, name='registar_emprestimo'), #cria a rota registar_emprestimo e chama a função registar_emprestimo do arquivo views.py, é necessário passar o id do livro como parâmetro
    path('devolver_livro/', views.devolver_livro, name='devolver_livro'), #cria a rota devolver_livro e chama a função devolver_livro do arquivo views.py, é necessário passar o id do livro como parâmetro
    path('alterar_livro/', views.alterar_livro, name='alterar_livro'), #cria a rota alterar_livro e chama a função alterar_livro do arquivo views.py, é necessário passar o id do livro como parâmetro
    path('meus_emprestimos/', views.meus_emprestimos, name='meus_emprestimos'), #cria a rota meus_emprestimos e chama a função meus_emprestimos do arquivo views.py, é necessário passar o id do livro como parâmetro
    path('processa_avaliacao/', views.processa_avaliacao, name='processa_avaliacao'), #cria a rota processa_avaliacao e chama a função processa_avaliacao do arquivo views.py, é necessário passar o id do livro como parâmetro
    path('historico/', views.historico_emprestimos, name='historico_emprestimos'), #cria a rota historicos e chama a função historicos do arquivo views.py, é necessário passar o id do livro como parâmetro
]
