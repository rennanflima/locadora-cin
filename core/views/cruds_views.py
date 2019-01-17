from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from core.models import Genero
from core.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

# Create your views here.




# Início CRUD Gênero

class GeneroCriar(SuccessMessageMixin, generic.CreateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'core/genero/novo.html'
    success_message = "Gênero adicionado com sucesso."
        
class GeneroEditar(SuccessMessageMixin, generic.UpdateView):
    model = Genero
    form_class = GeneroForm
    template_name = 'core/genero/editar.html'
    success_message = "Gênero editado com sucesso."

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


class GeneroDeletar(SuccessMessageMixin, generic.DeleteView):
    model = Genero
    template_name = "core/genero/deletar.html"
    success_url = reverse_lazy('admin:genero-listar')
    success_message = "Gênero excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(GeneroDeletar, self).delete(request, *args, **kwargs)

# Início CRUD Filme

class FilmeCriar(SuccessMessageMixin, generic.CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'core/filme/novo.html'
    success_message = "Filme adicionado com sucesso."

class FilmeEditar(SuccessMessageMixin, generic.UpdateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'core/filme/editar.html'
    success_message = "Filme editado com sucesso."

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
    success_url = reverse_lazy('admin:filme-listar')
    success_message = "Filme excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(FilmeDeletar, self).delete(request, *args, **kwargs)

# Início CRUD Midia

class MidiaCriar(SuccessMessageMixin, generic.CreateView):
    model = Midia
    form_class = MidiaForm
    template_name = 'core/midia/novo.html'
    success_message = "Mídia adicionada com sucesso."

class MidiaEditar(SuccessMessageMixin, generic.UpdateView):
    model = Midia
    form_class = MidiaForm
    template_name = 'core/midia/editar.html'
    success_message = "Mídia editada com sucesso."

class MidiaListar(generic.ListView):
    model = Midia
    paginate_by = 10
    template_name = 'core/midia/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(nome__icontains = nome)

class MidiaDetalhe(generic.DetailView):
    model = Midia
    template_name = 'core/midia/detalhe.html'


class MidiaDeletar(generic.DeleteView):
    model = Midia
    template_name = "core/midia/deletar.html"
    success_url = reverse_lazy('admin:midia-listar')
    success_message = "Mídia excluída com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MidiaDeletar, self).delete(request, *args, **kwargs)

