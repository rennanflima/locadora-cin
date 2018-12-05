from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('genero/<int:pk>', views.GenreDetailView.as_view(), name="genre-detail")
]
