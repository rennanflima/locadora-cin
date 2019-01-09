from django.shortcuts import render
from django.views import generic
from .models import Genero
from .forms import *
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "core/index.html"


class GeneroCriar(generic.CreateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'core/genero/novo.html'

class GeneroEditar(generic.UpdateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'core/genero/editar.html'

class GeneroListar(generic.ListView):
    model = Genero
    paginate_by = 10
    template_name = 'core/genero/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(nome__icontains = nome)
    
    # def get_context_data(self, **kwargs):
    #     context = super(MinhaListView, self).get_context_data(**kwargs)
    #     return context

class GeneroDetalhe(generic.DetailView):
    model = Genero
    template_name = 'core/genero/detalhe.html'


class GeneroDeletar(generic.DeleteView):
    model = Genero
    template_name = "core/genero/deletar.html"
