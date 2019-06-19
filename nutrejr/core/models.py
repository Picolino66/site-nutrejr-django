from django.db import models
from tinymce.models import HTMLField
from stdimage.models import StdImageField

# Create your models here.

class Apresentacao(models.Model):
    descricao = HTMLField('Descrição',)
    imagem = StdImageField('Imagem', upload_to='apresentacao')

    class Meta:
        verbose_name = 'Apresentacao'
        verbose_name_plural = 'Apresentacoes'

    def __str__(self):
        return self.descricao

class Servico(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    descricao = HTMLField('Descrição',)
    icon = models.CharField('Icone', max_length=100)
    
    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'

    def __str__(self):
        return self.titulo

class Video(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    url = models.CharField('Url', max_length=100)
    imagem = StdImageField('Imagem', upload_to='video')
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'

    def __str__(self):
        return self.titulo

class Enfeite(models.Model):
    titulo = models.CharField('Titulo', max_length=100)
    numero = models.CharField('Numero', max_length=100)
    icon = models.CharField('Icone', max_length=100)
    class Meta:
        verbose_name = 'Enfeite'
        verbose_name_plural = 'Enfeites'

    def __str__(self):
        return self.titulo

class Depoimento(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    descricao = HTMLField('Descrição',)
    imagem = StdImageField('Imagem', upload_to='depoimento')

    class Meta:
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.nome

class Time(models.Model):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.CharField('Cargo', max_length=100)
    imagem = StdImageField('Imagem', upload_to='time')
    face = models.CharField('Facebook', max_length=100)
    twitter = models.CharField('Twitter', max_length=100)
    google = models.CharField('Google+', max_length=100)
    instagram = models.CharField('Instagram', max_length=100)

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Times'

    def __str__(self):
        return self.nome