from utilizadores.models import Utilizador
from django.contrib import admin
 
admin.site.register(Utilizador) # admin.site.register(Utilizador) significa que o modelo Utilizador está registado no admin
class UtilizadorAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'password',) #readonly_fields significa que os campos nome, email e password são apenas de leitura

    

    
    


