from django.shortcuts import render, get_object_or_404
from django.views import generic
from core.models import Genero, Filme
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseRedirect

class IndexView(generic.ListView):
    model = Filme
    paginate_by = 30
    template_name = 'loja/index.html' 
    context_object_name = 'filmes'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['generos'] = Genero.objects.all()
        return context
    




def filmes_por_genero(request, slug):
    genero = get_object_or_404(Genero, slug=slug)
    generos = Genero.objects.all()
    filme_list = Filme.objects.filter(genero=genero)
    paginator = Paginator(filme_list, 30)

    page = request.GET.get('page')
    filmes = paginator.get_page(page)

    return render(request, 'loja/filmes_genero.html', {'filmes': filmes, 'generos':generos, 'genero': genero, })
