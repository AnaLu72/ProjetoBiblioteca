from django.db import models

class Utilizador(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=64) #64 é o tamanho máximo de uma senha em md5 (32 caracteres) + salt (32 caracteres)

    class Meta:
        verbose_name = 'Utilizador' #verbose_name é o nome que aparece na tabela do admin do Django para o modelo Utilizador (Nome legível)

    def __str__(self) -> str:
        return self.nome
    
    

