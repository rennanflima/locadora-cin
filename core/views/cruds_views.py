from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from core.models import Genero
from core.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.db import transaction

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

# Incício CRUD Pessoas do Filme

class PessoaFilmeCriar(SuccessMessageMixin, generic.CreateView):
    model = PessoaFilme
    form_class = PessoaFilmeForm
    template_name = 'core/pessoa_filme/novo.html'
    success_message = "Filme adicionado com sucesso."

class PessoaFilmeEditar(SuccessMessageMixin, generic.UpdateView):
    model = PessoaFilme
    form_class = PessoaFilmeForm
    template_name = 'core/pessoa_filme/editar.html'
    success_message = "Filme editado com sucesso."

class PessoaFilmeListar(generic.ListView):
    model = PessoaFilme
    paginate_by = 10
    template_name = 'core/pessoa_filme/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(nome__icontains = nome)

class PessoaFilmeDetalhe(generic.DetailView):
    model = PessoaFilme
    template_name = 'core/pessoa_filme/detalhe.html'

class PessoaFilmeDeletar(generic.DeleteView):
    model = PessoaFilme
    template_name = "core/pessoa_filme/deletar.html"
    success_url = reverse_lazy('admin:pessoafilme-listar')
    success_message = "Filme excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PessoaFilmeDeletar, self).delete(request, *args, **kwargs)

# Início CRUD Filme

class FilmeCriar(SuccessMessageMixin, generic.CreateView):
    model = Filme
    form_class = FilmeForm
    template_name = 'core/filme/novo.html'
    success_message = "Filme adicionado com sucesso."


class FilmeElencoCriar(generic.CreateView):
    model = Filme
    form_class = FilmeForm

    def get_context_data(self, **kwargs):
        data = super(FilmeElencoCriar, self).get_context_data(**kwargs)
        if self.request.POST:
            data['elencos'] = ElencoFormSet(self.request.POST)
        else:
            data['elencos'] = ElencoFormSet()
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        elencos = context['elencos']
        with transaction.atomic():
            self.object = form.save()

            if elencos.is_valid():
                elencos.instace = self.object
                elencos.save()
        return super(FilmeElencoCriar, self).form_valid(form)

def criar_filme(request):
    
    form = FilmeForm()
    elenco_forms = ElencoInlineFormSet(
        queryset=Elenco.objects.none()
    )

    if request.method == 'POST':
        form = FilmeForm(request.POST)
        elenco_forms = ElencoInlineFormSet(
            request.POST,
            queryset=Elenco.objects.none()
        )
        if form.is_valid() and elenco_forms.is_valid():
            filme = form.save()
            elencos = elenco_forms.save(commit=False)
            for elenco in elencos:
                elenco.filme = filme
                elenco.save()
    
    return render(request, 'core/filme/novo.html', {'form': form, 'formset':elenco_forms})
             

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

#Formulario de diretor no modal
def diretor_novo_ajax(request):
    data = dict()
    form = DiretorForm

    if request.method == 'POST':
        form = DiretorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.tipo = 'Diretor'
            f.save()
            data['form_is_valid'] = True
            diretores = PessoaFilme.objects.filter(tipo__icontains='Diretor')
            data['html_diretor_list'] = render_to_string('core/filme/ajax/partial_select_diretor.html', {'diretores': diretores})
        else:
            data['form_is_valid'] = False
    
    context = {'form': form}
    data['html_form'] = render_to_string('core/filme/ajax/partial_diretor_novo.html', context, request=request,)

    return JsonResponse(data)

def genero_novo_ajax(request):
    data = dict()
    form = GeneroForm

    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            generos = Genero.objects.all()
            data['html_genero_list'] = render_to_string('core/filme/ajax/partial_select_genero.html', {'generos': generos})
        else:
            data['form_is_valid'] = False
    
    context = {'form': form}
    data['html_form'] = render_to_string('core/filme/ajax/partial_genero_novo.html', context, request=request,)

    return JsonResponse(data)

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

