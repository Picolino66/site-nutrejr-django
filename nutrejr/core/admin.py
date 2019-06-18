from django.contrib import admin
from django.contrib.auth.models import User, Group

from core.models import Apresentacao

# Register your models here.

class ApresentacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', )

admin.site.register(Apresentacao, ApresentacaoAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = "Administração Nutre Jr."
admin.site.site_title = "Nutre Jr. Admin"