from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'mensagem' : 'Bem-vindo a aplicação em Django'}
    return render(request, 'test_app/index.html', context)