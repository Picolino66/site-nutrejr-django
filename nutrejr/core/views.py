from django.shortcuts import render
from core.models import Apresentacao, Servico, Video, Enfeite, Depoimento, Time, Parceiro, Galeria
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import sweetify

# Create your views here.
def index(request):
    
    apresentacao = Apresentacao.objects.all()
    servico = Servico.objects.all()
    video = Video.objects.all()
    enfeite = Enfeite.objects.all()[:4]
    depoimento = Depoimento.objects.all()
    time = Time.objects.all()
    parceiro = Parceiro.objects.all()
    galeria = Galeria.objects.all()
    context = {
        'apresentacao': Apresentacao.objects.last(),
        'servico': servico,
        'video': Video.objects.last(),
        'enfeite': enfeite,
        'depoimento': depoimento,
        'time': time,
        'parceiro': parceiro,
        'galeria': galeria,
    }
    return render(request, 'core/index.html', context=context)

def email(request):
    nome = request.POST.get('name', '')
    email = request.POST.get('email', '')
    msg = request.POST.get('message', '')

    #subject, from_email, to = nome, email, 'isaiasbd@hotmail.com'
    #text_content = msg
    #msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    #msg.send()

    #return render(request, 'core/index.html')
    if nome and msg and email:
        try:
            send_mail(nome, msg, email, ['isaiasbd@hotmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        sweetify.info(request, 'Message sent', button='Ok', timer=3000)
        return HttpResponseRedirect('../')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')