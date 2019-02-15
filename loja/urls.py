from django.urls import path, include
from loja import views
from allauth.socialaccount.views import ConnectionsView

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('filtro/genero/<slug:slug>/', views.filmes_por_genero, name="filme_genero"),
    path('busca/filme/', views.BuscaFilme.as_view(), name="buscar-filmes"),
    path('busca/avancada/filme/', views.buscar_avancada_filmes, name="buscar-avancada"),
    path('filme/<int:pk>/detalhe/', views.FilmeDetalhe.as_view(), name="filme-detalhe"),
    path('meu-perfil/', views.perfil_usuario_detalhe, name="meu-perfil"),
    path('meu-perfil/alterar/senha/', views.alterar_senha, name="alterar-senha"),
    path('meu-perfil/social/connections/', ConnectionsView.as_view(template_name="loja/perfil/connections_social.html"), name="meu-perfil-connections"),

]