from django.contrib import admin
from core.models import Estado, Cidade, User, Role

# Register your models here.

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(User, UsuarioAdmin)
admin.site.register(Role)