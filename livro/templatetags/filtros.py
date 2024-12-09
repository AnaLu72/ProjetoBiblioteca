from django import template #importar o template do django
from datetime import datetime #importar o datetime do python

register = template.Library() #criar uma instância do template

@register.filter #decorador para registrar o filtro
def mostra_duracao(value1, value2): #criar um filtro para mostrar a duração do livro, isto é, quanto tempo o livro ficou emprestado
    if all((isinstance(value1, datetime), isinstance(value2, datetime))): #se o valor1 e o valor2 forem instâncias de datetime
        dias = (value1 - value2).days #calcular a duração do livro em dias
        texto = 'Dias'
        if dias == 1: #se a duração do livro for 1 dia
            texto = 'Dia'

        return f'{dias} {texto}' #retornar a duração do livro em dias, é uma formatação de string (f-string)
    
    return "Ainda não foi devolvido." #retornar uma mensagem de erro


    #if data_devolucao and data_emprestimo:  #se a data de devolução e a data de empréstimo não forem nulas
        #duracao = (data_devolucao - data_emprestimo).days  #calcular a duração do livro
        #return duracao  #retornar a duração do livro em dias
    #return 'Não foi possível calcular a duração do livro'  #retornar uma mensagem de erro


# "==" significa igualdade, retorna True se os valores forem iguais, retorna False se os valores forem diferentes
# "!=" significa diferente, 
# "and" significa e, 
# "or" significa ou, 
# "not" significa não, 
# "in" significa está contido, 
# "is" significa é, "is not" significa não é, 
# "isinstance" significa é uma instância de,
# "not isinstance" significa não é uma instância de, 
# "isinstance(value, type)" significa é uma instância de type, 
# "not isinstance(value, type)" significa não é uma instância de type,
# "isinstance(value, (type1, type2, type3))" significa é uma instância de type1, type2 ou type3, ou seja, é uma instância de qualquer um dos tipos passados como parâmetro
# "not isinstance(value, (type1, type2, type3))" significa não é uma instância de type1, type2 ou type3, ou seja, não é uma instância de qualquer um dos tipos passados como parâmetro
# "isinstance(value, type1) or isinstance(value, type2)" significa é uma instância de type1 ou type2, ou seja, é uma instância de type1 ou type2
# "not isinstance(value, type1) and not isinstance(value, type2)" significa não é uma instância de type1 e não é uma instância de type2, ou seja, não é uma instância de type1 e não é uma instância de type2
# "isinstance(value, (type1, type2, type3)) or isinstance(value, (type4, type5, type6))" significa é uma instância de type1, type2 ou type3 ou é uma instância de type4, type5 ou type6, ou seja, é uma instância de type1, type2, type3, type4, type5 ou type6