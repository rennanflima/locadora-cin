from django.shortcuts import render
from django.views import generic
from .models import Genero
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages

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