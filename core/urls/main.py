from django.urls import path, include
from core.views import main


app_name = 'core'
urlpatterns = [
    path('', main.IndexView.as_view(), name='index'),

    path('reserva/', main.ReservaListar.as_view(), name="reserva-listar"),
    path('reserva/novo/', main.ReservaCriar.as_view(), name="reserva-novo"),
    path('reserva/<int:pk>/editar/', main.ReservaEditar.as_view(), name="reserva-editar"),
    path('reserva/<int:pk>/detalhe/', main.ReservaDetalhe.as_view(), name="reserva-detalhe"),
    path('reserva/<int:pk>/cancelar/', main.reserva_cancelar, name="reserva-cancelar"),

    path('ajax/carregar/midias/', main.carregar_tipo_midia, name="ajax-midias-carregar"),

    path('', include('core.urls.crud_urls')),
    
    path('locacao/', main.LocacaoListar.as_view(), name="locacao-listar"),
    path('locacao/realizar/', main.realizar_locacao, name="locacao-realizar"),
    path('locacao/realizar/<int:pk>/itens/', main.seleciona_itens_locacao, name="locacao-realizar-itens"),
]
