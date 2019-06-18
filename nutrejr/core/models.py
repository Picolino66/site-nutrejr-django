from django.db import models
from tinymce.models import HTMLField
from stdimage.models import StdImageField

# Create your models here.

class Apresentacao(models.Model):
    descricao = HTMLField('descricao',)
    imagem = StdImageField('Imagem', upload_to='apresentacao')

    class Meta:
        verbose_name = 'Apresentacao'
        verbose_name_plural = 'Apresentacoes'

    def __str__(self):
        return self.descricao