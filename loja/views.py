from django.shortcuts import render
from django.views import generic
from core.models import Genero, Filme

class IndexView(generic.ListView):
    model = Filme
    paginate_by = 30
    template_name = 'loja/index.html' 
    context_object_name = 'filmes'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        return context
    