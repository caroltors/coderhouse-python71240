from django.http import HttpResponse # Importação necessária para criação da view

# Exemplo de função da view
def saudacao(request): 
    return HttpResponse("Olá Django - Coder")