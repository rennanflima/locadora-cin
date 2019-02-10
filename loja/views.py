from django.shortcuts import render
from django.views import generic
from core.models import Genero

class IndexView(generic.TemplateView):
    template_name = "loja/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        return context
    