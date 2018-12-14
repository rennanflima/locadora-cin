from django.shortcuts import render
from django.views.generic import DetailView
from .models import Genre
# Create your views here.

class GenreDetailView(DetailView):
    model = Genre
