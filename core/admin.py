from django.contrib import admin
from core.models import Estado, Cidade, User, Perfil, Reserva, FormaPagamento, ArgumentoPagamento
from django.utils.translation import gettext_lazy as _
# Register your models here.

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla')


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'estado')

class ProfileInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    fk_name = 'user'

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    inlines = (ProfileInline, )

    # fieldsets = [
    #     (None, {
    #         'fields': ['email', 'password']
    #     }),
    #     (_('personal information'), {
    #         'fields': ['first_name', 'last_name']
    #     }),
    # ]

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UsuarioAdmin, self).get_inline_instances(request, obj)

class ArgumentoPagamentoAdmin(admin.ModelAdmin):
    list_display = ('campo', 'is_requerido', 'pagamentos')

admin.site.register(Estado, EstadoAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(User, UsuarioAdmin)
admin.site.register(FormaPagamento)
admin.site.register(ArgumentoPagamento, ArgumentoPagamentoAdmin)
