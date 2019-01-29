from django.urls import path, include
from loja import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
]