from django.shortcuts import render, get_object_or_404
from django.views import generic
from core.models import Genero, Filme
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from core.filters import *

class IndexView(generic.ListView):
    model = Filme
    paginate_by = 30
    template_name = 'loja/index.html' 
    context_object_name = 'filmes'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        return context
    
class BuscaFilme(generic.ListView):
    model = Filme
    paginate_by = 30
    template_name = 'loja/buscar_filmes.html' 
    context_object_name = 'filmes'

    def get_context_data(self, **kwargs):
        context = super(BuscaFilme, self).get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        return context

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(Q(titulo__icontains = nome) | Q(titulo_original__icontains=nome))

    def render_to_response(self, context):
        nome = self.request.GET.get('nome', '')
        if nome == '':
            return HttpResponseRedirect(reverse_lazy('index'))
        return super().render_to_response(context)



def filmes_por_genero(request, slug):
    genero = get_object_or_404(Genero, slug=slug)
    generos = Genero.objects.all()
    filme_list = Filme.objects.filter(genero=genero)
    paginator = Paginator(filme_list, 30)

    page = request.GET.get('page')
    filmes = paginator.get_page(page)

    return render(request, 'loja/filmes_genero.html', {'filmes': filmes, 'generos':generos, 'genero': genero, })


class FilmeDetalhe(generic.DetailView):
    model = Filme
    context_object_name = 'filme'
    template_name = 'loja/filme_detalhe.html'

    def get_context_data(self, **kwargs):
        context = super(FilmeDetalhe, self).get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        return context


def buscar_avancada_filmes(request):
    generos = Genero.objects.all()
    filmes_list = Filme.objects.all()
    filme_filter = FilmeFilter(request.GET, queryset=filmes_list)
    paginator = Paginator(filme_filter.qs, 10)

    page = request.GET.get('page')
    filmes = paginator.get_page(page)
    return render(request, 'loja/buscar_filmes_avancada.html', {'filmes': filmes, 'filter': filme_filter, 'generos': generos,})