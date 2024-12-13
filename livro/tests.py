from django.test import TestCase
from livro.forms import AvaliacaoForm
from livro.models import Livros

# Dados de teste
data = {
    'avaliacao': 'R',
    'livro': 15  # ID do livro a ser testado
}

form = AvaliacaoForm(data)
if form.is_valid():
    emprestimo = form.save(commit=False)
    print("Formulário válido:", emprestimo)
else:
    print("Erros no formulário:", form.errors)


