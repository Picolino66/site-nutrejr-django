from django.shortcuts import render
from core.models import Apresentacao, Servico, Video, Enfeite, Depoimento, Time

# Create your views here.
def index(request):
    
    apresentacao = Apresentacao.objects.all()
    servico = Servico.objects.all()[:6]
    video = Video.objects.all()
    enfeite = Enfeite.objects.all()[:4]
    depoimento = Depoimento.objects.all()
    time = Time.objects.all()

    context = {
        'apresentacao': Apresentacao.objects.last(),
        'servico': servico,
        'video': Video.objects.last(),
        'enfeite': enfeite,
        'depoimento': depoimento,
        'time': time,
    }
    return render(request, 'core/index.html', context=context)