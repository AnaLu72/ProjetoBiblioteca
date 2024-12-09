from django.contrib import admin
from .models import Livros, Categoria, Emprestimos

# Registar o modelo Livros no admin
admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Emprestimos)
