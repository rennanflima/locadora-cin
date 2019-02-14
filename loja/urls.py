from django.urls import path, include
from loja import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('filtro/genero/<slug:slug>/', views.filmes_por_genero, name="filme_genero"),
    path('busca/filme/', views.BuscaFilme.as_view(), name="buscar-filmes"),
    path('busca/avancada/filme/', views.buscar_avancada_filmes, name="buscar-avancada"),
    path('filme/<int:pk>/detalhe/', views.FilmeDetalhe.as_view(), name="filme-detalhe"),
]