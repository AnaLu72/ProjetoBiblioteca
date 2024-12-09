# jardim_de_folhas_soltas/context_processors.py

def global_vars(request):
    # define as variáveis de contexto globais aqui
    return {
        'some_global_var': 'value',
    }
