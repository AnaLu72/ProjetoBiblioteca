from django.db import models #importar o models do django
from datetime import date, datetime #importar o date e o datetime do datetime   
import datetime #importar o datetime
from utilizadores.models import Utilizador #importar o modelo Utilizador do app utilizadores
from django.core.exceptions import ValidationError



# criar a classe Categoria que herda de models.Model
class Categoria(models.Model):
    nome = models.CharField(max_length = 50)
    descricao = models.TextField()
    utilizador = models.ForeignKey(Utilizador, on_delete = models.DO_NOTHING) #criar uma chave estrangeira para o utilizador, on_delete = models.DO_NOTHING significa que se o utilizador for deletado, o livro não será deletado

    def __str__(self) -> str:
        return self.nome
    

# criar a classe Livros que herda de models.Model
class Livros(models.Model):
    img = models.ImageField(upload_to = 'capa_livro/', null = True, blank = True) # criar um campo para a imagem do livro
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 100)
    co_autor = models.CharField(max_length = 30, blank = True) # o campo pode estar em branco e ainda assim ser válido
    data_registo = models.DateField(default = date.today)
    emprestado = models.BooleanField(default = False)
    isbn = models.CharField(max_length = 20)
    editora = models.CharField(max_length = 100)
    ano = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete = models.PROTECT) # criar uma chave estrangeira para a categoria, on_delete = models.PROTECT significa que se a categoria for deletada, o livro não será deletado
    utilizador = models.ForeignKey(Utilizador, on_delete = models.PROTECT) # criar uma chave estrangeira para o utilizador, on_delete = models.PROTECT significa que se o utilizador for deletado, o livro não será deletado 
    estado_leitura = models.CharField(max_length = 20, choices = 
                                      [('nao_lido', 'Não Lido'), 
                                       ('a_ler', 'A Ler'), 
                                       ('lido', 'Lido'), 
                                       ('emprestado', 'Emprestado'), 
                                       ('entregue', 'Entregue')])
    
    #criar a função para mostrar o nome do livro no admin
    class Meta:
        verbose_name = 'Livro' #nome do modelo no admin

    def __str__(self):
            return f"{self.nome} - {self.autor}" #mostrar o nome do livro no admin
    
class Emprestimos(models.Model):
    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo'),
        ('E', 'Excelente'),
    )
    nome_emprestado = models.ForeignKey(Utilizador, on_delete = models.DO_NOTHING, blank = True, null = True)
    nome_emprestado_anonimo = models.CharField(max_length = 50, blank = True, null = True)
   # data_emprestimo = models.DateTimeField(default=date.today)
    data_emprestimo = models.DateTimeField(default=datetime.datetime.now)
    data_devolucao = models.DateTimeField(blank = True, null = True)
    livro = models.ForeignKey(Livros, on_delete = models.DO_NOTHING, blank = True, null = True)
    avaliacao = models.CharField(max_length = 1, choices = choices, blank = True, null = True) #o campo pode estar em branco e ainda assim ser válido

    def clean(self):
        if not self.livro:
            raise ValidationError('O campo livro é obrigatório.')
        # Verifica se o livro existe
        if not Livros.objects.filter(id=self.livro.id).exists():
            raise ValidationError('Livro inválido.')

    class Meta:
        verbose_name = 'Emprestimo' #nome do modelo no admin, para aparecer no admin como Emprestimo

    def __str__(self): #função para mostrar o nome do emprestimo no admin
        return f"{self.nome_emprestado} | {self.livro}"
    
class Avaliacao(models.Model):
    livro = models.ForeignKey(Livros, on_delete=models.CASCADE)
    avaliacao = models.CharField(max_length=255)  # Ou use outro tipo de campo para avaliação, como IntegerField para notas
    data_avaliacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Avaliação do livro {self.livro} - {self.avaliacao}'
	
    



