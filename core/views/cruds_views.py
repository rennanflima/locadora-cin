from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from core.models import *
from core.forms import *
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect
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

class ArtistaCriar(SuccessMessageMixin, generic.CreateView):
    model = Artista
    form_class = ArtistaForm
    template_name = 'core/pessoa_filme/novo.html'
    success_message = "Filme adicionado com sucesso."

class ArtistaEditar(SuccessMessageMixin, generic.UpdateView):
    model = Artista
    form_class = ArtistaForm
    template_name = 'core/pessoa_filme/editar.html'
    success_message = "Filme editado com sucesso."

class ArtistaListar(generic.ListView):
    model = Artista
    paginate_by = 10
    template_name = 'core/pessoa_filme/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(nome__icontains = nome)

class ArtistaDetalhe(generic.DetailView):
    model = Artista
    template_name = 'core/pessoa_filme/detalhe.html'

class ArtistaDeletar(generic.DeleteView):
    model = Artista
    template_name = "core/pessoa_filme/deletar.html"
    success_url = reverse_lazy('admin:pessoafilme-listar')
    success_message = "Filme excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ArtistaDeletar, self).delete(request, *args, **kwargs)

# Início CRUD Filme

# View Criar filme com Form e Formset
def criar_filme(request):
    
    form = FilmeForm()
    elenco_forms = ElencoInlineFormSet(queryset=Elenco.objects.none())

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
            messages.success(request, 'Filme adicionado com sucesso.')
            return HttpResponseRedirect(reverse('admin:filme-detalhe', kwargs={'pk': filme.pk}))
    
    return render(request, 'core/filme/novo.html', {'form': form, 'formset':elenco_forms})
             

def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    form = FilmeForm(instance=filme)
    elenco_filme = Elenco.objects.filter(filme=filme.id)
    elenco_forms = ElencoInlineFormSet(instance=filme)

    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        elenco_forms = ElencoInlineFormSet(request.POST, instance=filme)
        if form.is_valid():
            if elenco_forms.is_valid():
                filme = form.save()
                elencos = elenco_forms.save()
                for obj in elencos:
                    if obj.filme != filme:
                        obj.filme = filme
                        obj.save()

                messages.success(request, 'Filme editado com sucesso.')
                return HttpResponseRedirect(filme.get_absolute_url())
            else:
                messages.error(request, elenco_forms.errors)
        else:
            messages.error(request, form.errors)
            
    
    return render(request, 'core/filme/editar.html', {'form': form, 'formset':elenco_forms})


# class FilmeEditar(SuccessMessageMixin, generic.UpdateView):
#     model = Filme
#     form_class = FilmeForm
#     template_name = 'core/filme/editar.html'
#     success_message = "Filme editado com sucesso."

class FilmeListar(generic.ListView):
    model = Filme
    paginate_by = 10
    template_name = 'core/filme/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(Q(titulo__icontains = nome) | Q(titulo_original__icontains=nome))

class FilmeDetalhe(generic.DetailView):
    model = Filme
    context_object_name = 'filme'
    template_name = 'core/filme/detalhe.html'

    def get_context_data(self, **kwargs):
        context = super(FilmeDetalhe, self).get_context_data(**kwargs)
        context['elencos'] = Elenco.objects.filter(filme=self.object)
        return context

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
            data['form_diretor_is_valid'] = True
            diretores = Artista.objects.filter(tipo__icontains='Diretor')
            data['html_diretor_list'] = render_to_string('core/filme/ajax/partial_select_diretor.html', {'diretores': diretores})
        else:
            try:
                diretor = Artista.objects.get(nome=form.instance.nome)
                
                if 'Ator' in ator.tipo:
                    ator.tipo = 'Diretor', 'Ator'
                
                diretor.save()
                data['form_diretor_is_valid'] = True
                diretores = Artista.objects.filter(tipo__icontains='Diretor')
                data['html_diretor_list'] = render_to_string('core/filme/ajax/partial_select_diretor.html', {'diretores': diretores})           
            except:
                data['form_diretor_is_valid'] = False
    
    context = {'form': form}
    data['html_form_diretor'] = render_to_string('core/filme/ajax/partial_diretor_novo.html', context, request=request,)

    return JsonResponse(data)

def genero_novo_ajax(request):
    data = dict()
    form = GeneroForm

    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_genero_is_valid'] = True
            generos = Genero.objects.all()
            data['html_genero_list'] = render_to_string('core/filme/ajax/partial_select_genero.html', {'generos': generos})
        else:
            data['form_genero_is_valid'] = False
    
    context = {'form': form}
    data['html_form_genero'] = render_to_string('core/filme/ajax/partial_genero_novo.html', context, request=request,)

    return JsonResponse(data)


def ator_novo_ajax(request):
    data = dict()
    form = AtorForm

    if request.method == 'POST':
        form = AtorForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.tipo = 'Ator'
            f.save()
            data['form_ator_is_valid'] = True
            atores = Artista.objects.filter(tipo__icontains='Ator')
            data['html_ator_list'] = render_to_string('core/filme/ajax/partial_select_ator.html', {'atores': atores})
        else:
            try:
                ator = Artista.objects.get(nome=form.instance.nome)
                
                if 'Diretor' in ator.tipo:
                    ator.tipo = 'Diretor', 'Ator'
                
                ator.save()
                data['form_ator_is_valid'] = True
                atores = Artista.objects.filter(tipo__icontains='Ator')
                data['html_ator_list'] = render_to_string('core/filme/ajax/partial_select_ator.html', {'atores': atores})           
            except:
                data['form_ator_is_valid'] = False
    
    context = {'form': form}
    data['html_form_ator'] = render_to_string('core/filme/ajax/partial_ator_novo.html', context, request=request,)

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

