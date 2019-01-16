from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    # Início URL CRUD Gênero
    path('genero', views.GeneroListar.as_view(), name="genero-listar"),
    path('genero/novo', views.GeneroCriar.as_view(), name="genero-novo"),
    path('genero/<int:pk>/editar', views.GeneroEditar.as_view(), name="genero-edita"),
    path('genero/<int:pk>/deletar', views.GeneroDeletar.as_view(), name="genero-deletar"),
    path('genero/<int:pk>/detalhe', views.GeneroDetalhe.as_view(), name="genero-detalhe"),
    # Termino URL CRUD Gênero

    # Início URL CRUD Filme
    path('filme', views.FilmeListar.as_view(), name="filme-listar"),
    path('filme/novo', views.FilmeCriar.as_view(), name="filme-novo"),
    path('filme/<int:pk>/editar', views.FilmeEditar.as_view(), name="filme-editar"),
    path('filme/<int:pk>/deletar', views.FilmeDeletar.as_view(), name="filme-deletar"),
    path('filme/<int:pk>/detalhe', views.FilmeDetalhe.as_view(), name="filme-detalhe"),
    # Termino URL CRUD Filme
    
    # Início URL CRUD Midia
    path('midia', views.MidiaListar.as_view(), name="midia-listar"),
    path('midia/novo', views.MidiaCriar.as_view(), name="midia-novo"),
    path('midia/<int:pk>/editar', views.MidiaEditar.as_view(), name="midia-editar"),
    path('midia/<int:pk>/deletar', views.MidiaDeletar.as_view(), name="midia-deletar"),
    path('midia/<int:pk>/detalhe', views.MidiaDetalhe.as_view(), name="midia-detalhe"),
    # Termino URL CRUD Midia
]
