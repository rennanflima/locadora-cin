from django.urls import path, include
from loja import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('filtro/genero/<slug:slug>/', views.filmes_por_genero, name="filme_genero"),
]