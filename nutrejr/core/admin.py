from django.contrib import admin
from django.contrib.auth.models import User, Group

from core.models import Apresentacao, Servico, Video, Enfeite, Depoimento, Time

# Register your models here.

class ApresentacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', )

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao', 'icon',)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )

class EnfeiteAdmin(admin.ModelAdmin):
    list_display = ('titulo', )

class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', )

class TimeAdmin(admin.ModelAdmin):
    list_display = ('nome', )

admin.site.register(Apresentacao, ApresentacaoAdmin)
admin.site.register(Servico, ServicoAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Enfeite, EnfeiteAdmin)
admin.site.register(Depoimento, DepoimentoAdmin)
admin.site.register(Time, TimeAdmin)


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = "Administração Nutre Jr."
admin.site.site_title = "Nutre Jr. Admin"