from django.urls import path, re_path, include
from core.views import cruds_views

urlpatterns = [

    #Ajax
    path('ajax/diretor/novo/', cruds_views.diretor_novo_ajax, name="ajax-diretor-novo"),
    path('ajax/genero/novo/', cruds_views.genero_novo_ajax, name="ajax-genero-novo"),
    path('ajax/ator/novo/', cruds_views.ator_novo_ajax, name="ajax-ator-novo"),
    path('ajax/carregar/cidades/', cruds_views.carregar_cidades, name="ajax-cidades-carregar"), 
    path('ajax/buscar/cep/', cruds_views.buscar_cep, name="ajax-buscar-cep"),

    # Início URL CRUD Gênero
    path('genero/', cruds_views.GeneroListar.as_view(), name="genero-listar"),
    path('genero/novo/', cruds_views.GeneroCriar.as_view(), name="genero-novo"),
    path('genero/<int:pk>/editar/', cruds_views.GeneroEditar.as_view(), name="genero-editar"),
    path('genero/<int:pk>/deletar/', cruds_views.GeneroDeletar.as_view(), name="genero-deletar"),
    path('genero/<int:pk>/detalhe/', cruds_views.GeneroDetalhe.as_view(), name="genero-detalhe"),

    # Início URL CRUD Artista
    path('artista/', cruds_views.ArtistaListar.as_view(), name="artista-listar"),
    path('artista/novo/', cruds_views.ArtistaCriar.as_view(), name="artista-novo"),
    path('artista/<int:pk>/editar/', cruds_views.ArtistaEditar.as_view(), name="artista-editar"),
    path('artista/<int:pk>/deletar/', cruds_views.ArtistaDeletar.as_view(), name="artista-deletar"),
    path('artista/<int:pk>/detalhe/', cruds_views.ArtistaDetalhe.as_view(), name="artista-detalhe"),

    # Início URL CRUD Filme
    path('filme/', cruds_views.FilmeListar.as_view(), name="filme-listar"),
    path('filme/novo/', cruds_views.criar_filme, name="filme-novo"),
    path('filme/<int:pk>/editar/', cruds_views.editar_filme, name="filme-editar"),
    path('filme/<int:pk>/deletar/', cruds_views.FilmeDeletar.as_view(), name="filme-deletar"),
    path('filme/<int:pk>/detalhe/', cruds_views.FilmeDetalhe.as_view(), name="filme-detalhe"),

    # Início URL CRUD Midia
    path('midia/', cruds_views.MidiaListar.as_view(), name="midia-listar"),
    path('midia/novo/', cruds_views.MidiaCriar.as_view(), name="midia-novo"),
    path('midia/<int:pk>/editar/', cruds_views.MidiaEditar.as_view(), name="midia-editar"),
    path('midia/<int:pk>/deletar/', cruds_views.MidiaDeletar.as_view(), name="midia-deletar"),
    path('midia/<int:pk>/detalhe/', cruds_views.MidiaDetalhe.as_view(), name="midia-detalhe"),

    # Início URL CRUD Distribuidora
    path('distribuidora/', cruds_views.DistribuidoraListar.as_view(), name="distribuidora-listar"),
    path('distribuidora/novo/', cruds_views.criar_distribuidora, name="distribuidora-novo"),
    path('distribuidora/<int:pk>/editar/', cruds_views.editar_distribuidora, name="distribuidora-editar"),
    path('distribuidora/<int:pk>/deletar/', cruds_views.DistribuidoraDeletar.as_view(), name="distribuidora-deletar"),
    path('distribuidora/<int:pk>/detalhe/', cruds_views.DistribuidoraDetalhe.as_view(), name="distribuidora-detalhe"),

    # Início URL CRUD Item
    path('item/', cruds_views.ItemListar.as_view(), name="item-listar"),
    path('item/novo/', cruds_views.ItemCriar.as_view(), name="item-novo"),
    path('item/<int:pk>/editar/', cruds_views.ItemEditar.as_view(), name="item-editar"),
    path('item/<int:pk>/deletar/', cruds_views.ItemDeletar.as_view(), name="item-deletar"),
    path('item/<int:pk>/detalhe/', cruds_views.ItemDetalhe.as_view(), name="item-detalhe"),
    path('item/<int:pk>/ativar/', cruds_views.item_ativar, name="item-ativar"),
    path('item/<int:pk>/desativar/', cruds_views.item_desativar, name="item-desativar"),

    # Início URL CRUD Cliente
    path('cliente/', cruds_views.cliente_listar, name="cliente-listar"),
    path('cliente/novo/', cruds_views.criar_cliente, name="cliente-novo"),
    path('cliente/<int:pk>/editar/', cruds_views.editar_cliente, name="cliente-editar"),
    path('cliente/<int:pk>/deletar/', cruds_views.ClienteDeletar.as_view(), name="cliente-deletar"),
    path('cliente/<int:pk>/detalhe/', cruds_views.ClienteDetalhe.as_view(), name="cliente-detalhe"),
    path('cliente/<int:pk>/ativar/', cruds_views.cliente_ativar, name="cliente-ativar"),
    path('cliente/<int:pk>/desativar/', cruds_views.cliente_desativar, name="cliente-desativar"),
    re_path(r'^cliente-autocomplete/$', cruds_views.ClienteAutocomplete.as_view(), name="cliente-autocomplete"),

    # Início URL CRUD Dependente
    path('cliente/<int:pk>/dependentes/', cruds_views.dependente_listar, name="dependente-listar"),
    path('cliente/<int:pk>/dependente/<int:id_dep>/detalhe/', cruds_views.dependente_detalhe, name="dependente-detalhe"),
    path('cliente/<int:pk>/depentente/novo/', cruds_views.criar_dependente, name="dependente-novo"),
    path('cliente/<int:pk>/dependente/<int:id_dep>/editar/', cruds_views.editar_dependente, name="dependente-editar"),
    path('cliente/<int:pk>/dependente/<int:id_dep>/deletar/', cruds_views.dependente_deletar, name="dependente-deletar"),
    path('cliente/<int:pk>/dependente/<int:id_dep>/ativar/', cruds_views.dependente_ativar, name="dependente-ativar"),
    path('cliente/<int:pk>/dependente/<int:id_dep>/desativar/', cruds_views.dependente_desativar, name="dependente-desativar"),


    # Início URL CRUD Funcionário
    path('funcionario/buscar/', cruds_views.buscar_funcionario, name="funcionario-buscar"),
    path('funcionario/', cruds_views.funcionario_listar, name="funcionario-listar"),
    path('funcionario/novo/', cruds_views.criar_funcionario, name="funcionario-novo"),
    path('funcionario/<int:pk>/editar/', cruds_views.editar_funcionario, name="funcionario-editar"),
    path('funcionario/<int:pk>/deletar/', cruds_views.FuncionarioDeletar.as_view(), name="funcionario-deletar"),
    path('funcionario/<int:pk>/detalhe/', cruds_views.FuncionarioDetalhe.as_view(), name="funcionario-detalhe"),
    path('funcionario/<int:pk>/ativar/', cruds_views.funcionario_ativar, name="funcionario-ativar"),
    path('funcionario/<int:pk>/desativar/', cruds_views.funcionario_desativar, name="funcionario-desativar"),
]