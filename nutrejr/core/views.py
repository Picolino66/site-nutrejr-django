from django.shortcuts import render

# Create your views here.
def index(request):
    apresentacao = Apresentacao.objects
    return render(request, 'core/index.html')