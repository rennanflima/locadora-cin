from django.urls import path, include
from core.views import cruds_views

urlpatterns = [

    #Ajax
    path('ajax/diretor/novo/', cruds_views.diretor_novo_ajax, name="ajax-diretor-novo"),
    path('ajax/genero/novo/', cruds_views.genero_novo_ajax, name="ajax-genero-novo"),
    path('ajax/ator/novo/', cruds_views.ator_novo_ajax, name="ajax-ator-novo"), 


    # Início URL CRUD Gênero
    path('genero/', cruds_views.GeneroListar.as_view(), name="genero-listar"),
    path('genero/novo/', cruds_views.GeneroCriar.as_view(), name="genero-novo"),
    path('genero/<int:pk>/editar/', cruds_views.GeneroEditar.as_view(), name="genero-edita"),
    path('genero/<int:pk>/deletar/', cruds_views.GeneroDeletar.as_view(), name="genero-deletar"),
    path('genero/<int:pk>/detalhe/', cruds_views.GeneroDetalhe.as_view(), name="genero-detalhe"),
    # Termino URL CRUD Gênero

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
    # Termino URL CRUD Filme

    #CRUD Elenco
    path('filme/<int:idFilme>/elenco/novo/', cruds_views.FilmeListar.as_view(), name="elenco-listar"),
    # path('filme/<int:idFilme>/elenco/<int:pk>/detalhe', cruds_views.filme_detalhe, name="elenco-detalhe"),


    # Início URL CRUD Midia
    path('midia/', cruds_views.MidiaListar.as_view(), name="midia-listar"),
    path('midia/novo/', cruds_views.MidiaCriar.as_view(), name="midia-novo"),
    path('midia/<int:pk>/editar/', cruds_views.MidiaEditar.as_view(), name="midia-editar"),
    path('midia/<int:pk>/deletar/', cruds_views.MidiaDeletar.as_view(), name="midia-deletar"),
    path('midia/<int:pk>/detalhe/', cruds_views.MidiaDetalhe.as_view(), name="midia-detalhe"),
    # Termino URL CRUD Midia
]