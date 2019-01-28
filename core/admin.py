from django.contrib import admin
from core.models import Estado, Cidade

# Register your models here.

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade, CidadeAdmin)