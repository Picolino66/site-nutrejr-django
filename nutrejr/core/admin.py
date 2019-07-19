from django.contrib import admin
from django.contrib.auth.models import User, Group

from core.models import Apresentacao, Servico, Video, Enfeite, Depoimento, Time, Parceiro, Galeria

# Register your models here.

class ApresentacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', )

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )

class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )

class EnfeiteAdmin(admin.ModelAdmin):
    list_display = ('titulo', )

class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', )

class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', )

class ParceiroAdmin(admin.ModelAdmin):
    list_display = ('nome', )

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', )

admin.site.register(Apresentacao, ApresentacaoAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Enfeite, EnfeiteAdmin)
admin.site.register(Depoimento, DepoimentoAdmin)
admin.site.register(Time, TimeAdmin)
admin.site.register(Parceiro, ParceiroAdmin)
admin.site.register(Galeria, GaleriaAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = "Administração Nutre Jr."
admin.site.site_title = "Nutre Jr. Admin"