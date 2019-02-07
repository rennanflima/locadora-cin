from django.urls import path, include
from django.conf.urls import url
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

    path('locacao/realizar/<int:pk>/', main.realizar_locacao, name="locacao-realizar"),
    path('locacao/realizar/', main.realizar_locacao, name="locacao-realizar"),
    path('locacao/realizar/<int:pk>/itens/', main.seleciona_itens_locacao, name="locacao-realizar-itens"),
    path('locacao/realizar/<int:pk>/confirmar/', main.confirmar_locacao, name="locacao-confirmar"),
    path('locacao/realizar/<int:pk>/finalizar/', main.finalizar_locacao, name="locacao-finalizar"),
    
    path('locacao/<int:pk>/detalhe/', main.LocacaoDetalhe.as_view(), name="locacao-detalhe"),
    path('locacao/item/adicionar/', main.item_add, name='ajax-item-add'),
    path('locacao/item/<int:pk>/editar/', main.item_edit, name='ajax-item-update'),
    path('locacao/item/<int:pk>/deletar/', main.item_delete, name='ajax-item-delete'),
    path('ajax/carregar/item/', main.carregar_item_ajax, name="ajax-item-carregar"),
    path('locacao/<int:pk>/detalhe/', main.LocacaoDetalhe.as_view(), name="locacao-detalhe"),

    path('ajax/locacao/pagamento', main.pagamento_locacao, name="locacao-pagamento"),
    path('ajax/carregar/campos/', main.carregar_argumento_forma_pagamento, name="ajax-campos-carregar"), 
    path('ajax/detalhe/pagamento/<int:pk>/', main.detalhe_pagamento, name="ajax-pagamento-detalhe"), 
]
