from utilizadores.models import Utilizador #importar o modelo Utilizador do app utilizadores
from django import forms #importar o forms do django
from .models import Livros, Categoria #importar o modelo Livros do app livro e o modelo Categoria do app livro
from django.db import models #importar o models do django
from datetime import date #importar o date do datetime


class RegistoLivro(forms.ModelForm): #criar a classe RegistoLivro que herda de forms.ModelForm, vai utilizar o modelo Livros
    class Meta: #criar a classe Meta para definir o modelo e os campos do formulário
        model = Livros #definir o modelo
        fields = ['nome', 'autor', 'co_autor', 'data_registo', 'emprestado', 'isbn', 'editora', 'ano', 'categoria', 'utilizador', 'estado_leitura'] #definir os campos do formulário

    def __init__(self, *args, **kwargs): #criar o método __init__ para definir os widgets dos campos do formulário
        super(RegistoLivro, self).__init__(*args, **kwargs) #chamar o método __init__ da classe pai
        self.fields['utilizador'].widget = forms.HiddenInput() #definir o widget do campo utilizador como HiddenInput, isto é, o campo não será exibido no formulário

class CategoriaLivro(forms.Form): #criar a classe CategoriaLivro que herda de forms.Form
    nome = forms.CharField(label = 'Nome', max_length = 50) #criar o campo nome do formulário
    descricao = forms.CharField(label = 'Descrição', max_length = 20) #criar o campo descrição do formulário

    def __init__(self, *args, **kwargs): #criar o método __init__ para definir os widgets dos campos do formulário 
       super(CategoriaLivro, self).__init__(*args, **kwargs) #chamar o método __init__ da classe pai
       self.fields['descricao'].widget = forms.Textarea() #definir o widget do campo utilizador como Textarea, isto é, o campo será exibido como um textarea

