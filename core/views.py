from django.shortcuts import render
from django.views import generic
from .models import Genero
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "core/index.html"

# Início CRUD Gênero

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

class GeneroDetalhe(generic.DetailView):
    model = Genero
    template_name = 'core/genero/detalhe.html'


class GeneroDeletar(generic.DeleteView):
    model = Genero
    template_name = "core/genero/deletar.html"
    success_url = reverse_lazy('core:genero-listar')
    success_message = "Gênero excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(GeneroDeletar, self).delete(request, *args, **kwargs)

# Termino CRUD Gênero

# Início CRUD Filme

class FilmeCriar(generic.CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'core/filme/novo.html'

class FilmeEditar(generic.UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'core/filme/editar.html'

class FilmeListar(generic.ListView):
    model = Filme
    paginate_by = 10
    template_name = 'core/filme/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(Q(titulo__icontains = nome) | Q(titulo_original__icontains=nome))

class FilmeDetalhe(generic.DetailView):
    model = Filme
    template_name = 'core/filme/detalhe.html'


class FilmeDeletar(generic.DeleteView):
    model = Filme
    template_name = "core/filme/deletar.html"
    success_url = reverse_lazy('core:filme-listar')
    success_message = "Filme excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(FilmeDeletar, self).delete(request, *args, **kwargs)

# Termino CRUD Filme