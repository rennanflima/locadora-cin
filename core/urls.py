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
    
]
