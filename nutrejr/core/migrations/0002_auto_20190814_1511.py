# Generated by Django 2.2.1 on 2019-08-14 18:11

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='imagem',
            field=stdimage.models.StdImageField(upload_to='galeria', verbose_name='Imagem'),
        ),
    ]
