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
from django.utils.html import strip_tags
from pycep_correios import consultar_cep
from pycep_correios.excecoes import ExcecaoPyCEPCorreios
from core.filters import *
from datetime import date
from django.core.paginator import Paginator


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
    context_object_name = 'genero'
    template_name = 'core/genero/detalhe.html'


class GeneroDeletar(SuccessMessageMixin, generic.DeleteView):
    model = Genero
    template_name = "core/genero/deletar.html"
    success_url = reverse_lazy('core:genero-listar')
    success_message = "Gênero excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(GeneroDeletar, self).delete(request, *args, **kwargs)

# Incício CRUD Pessoas do Filme
class ArtistaCriar(SuccessMessageMixin, generic.CreateView):
    model = Artista
    form_class = ArtistaForm
    template_name = 'core/artista/novo.html'
    success_message = "Artista adicionado com sucesso."

class ArtistaEditar(SuccessMessageMixin, generic.UpdateView):
    model = Artista
    form_class = ArtistaForm
    template_name = 'core/artista/editar.html'
    success_message = "Artista editado com sucesso."

class ArtistaListar(generic.ListView):
    model = Artista
    paginate_by = 10
    template_name = 'core/artista/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(nome__icontains = nome)

class ArtistaDetalhe(generic.DetailView):
    model = Artista
    template_name = 'core/artista/detalhe.html'

class ArtistaDeletar(generic.DeleteView):
    model = Artista
    template_name = "core/artista/deletar.html"
    success_url = reverse_lazy('core:artista-listar')
    success_message = "Artista excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ArtistaDeletar, self).delete(request, *args, **kwargs)

# Início CRUD Filme

# View Criar filme com Form e Formset
def criar_filme(request):
    
    form = FilmeForm()
    elenco_forms = ElencoInlineFormSet(queryset=Elenco.objects.none())

    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES)
        elenco_forms = ElencoInlineFormSet(
            request.POST, request.FILES,
            queryset=Elenco.objects.none()
        )
        if form.is_valid() and elenco_forms.is_valid():
            try:
                with transaction.atomic():
                    filme = form.save()
                    elencos = elenco_forms.save(commit=False)
                    for elenco in elencos:
                        elenco.filme = filme
                        elenco.save()
                    messages.success(request, 'Filme adicionado com sucesso.')
                    return HttpResponseRedirect(reverse('core:filme-detalhe', kwargs={'pk': filme.pk}))
            except Exception as e:
                messages.error(request, e)
    
    return render(request, 'core/filme/novo.html', {'form': form, 'formset':elenco_forms})
             

def editar_filme(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    form = FilmeForm(instance=filme)
    elenco_filme = Elenco.objects.filter(filme=filme.id)
    elenco_forms = ElencoInlineFormSet(instance=filme)

    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)
        elenco_forms = ElencoInlineFormSet(request.POST, request.FILES, instance=filme)
        if form.is_valid() and elenco_forms.is_valid():
            try:
                with transaction.atomic():
                    filme = form.save()
                    elencos = elenco_forms.save()
                    for obj in elencos:
                        if obj.filme != filme:
                            obj.filme = filme
                            obj.save()

                    messages.success(request, 'Filme editado com sucesso.')
                    return HttpResponseRedirect(filme.get_absolute_url())
            except Exception as e:
                messages.error(request, e)
            
    return render(request, 'core/filme/editar.html', {'form': form, 'formset':elenco_forms})

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
            data['html_diretor_list'] = render_to_string('core/ajax/partial_select_diretor.html', {'diretores': diretores})
        else:
            try:
                diretor = Artista.objects.get(nome=form.instance.nome)
                
                if 'Ator' in ator.tipo:
                    ator.tipo = 'Diretor', 'Ator'
                
                diretor.save()
                data['form_diretor_is_valid'] = True
                diretores = Artista.objects.filter(tipo__icontains='Diretor')
                data['html_diretor_list'] = render_to_string('core/ajax/partial_select_diretor.html', {'diretores': diretores})           
            except:
                data['form_diretor_is_valid'] = False
    
    context = {'form': form}
    data['html_form_diretor'] = render_to_string('core/ajax/partial_diretor_novo.html', context, request=request,)

    return JsonResponse(data)

#Formulario de genero no modal
def genero_novo_ajax(request):
    data = dict()
    form = GeneroForm

    if request.method == 'POST':
        form = GeneroForm(request.POST)
        if form.is_valid():
            form.save()
            data['form_genero_is_valid'] = True
            generos = Genero.objects.all()
            data['html_genero_list'] = render_to_string('core/ajax/partial_select_genero.html', {'generos': generos})
        else:
            data['form_genero_is_valid'] = False
    
    context = {'form': form}
    data['html_form_genero'] = render_to_string('core/ajax/partial_genero_novo.html', context, request=request,)

    return JsonResponse(data)

#Formulario de ator no modal
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
            data['html_ator_list'] = render_to_string('core/ajax/partial_select_ator.html', {'atores': atores})
        else:
            try:
                ator = Artista.objects.get(nome=form.instance.nome)
                
                if 'Diretor' in ator.tipo:
                    ator.tipo = 'Diretor', 'Ator'
                
                ator.save()
                data['form_ator_is_valid'] = True
                atores = Artista.objects.filter(tipo__icontains='Ator')
                data['html_ator_list'] = render_to_string('core/ajax/partial_select_ator.html', {'atores': atores})           
            except:
                data['form_ator_is_valid'] = False
    
    context = {'form': form}
    data['html_form_ator'] = render_to_string('core/ajax/partial_ator_novo.html', context, request=request,)

    return JsonResponse(data)

class FilmeDeletar(generic.DeleteView):
    model = Filme
    template_name = "core/filme/deletar.html"
    success_url = reverse_lazy('core:filme-listar')
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
    success_url = reverse_lazy('core:midia-listar')
    success_message = "Mídia excluída com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(MidiaDeletar, self).delete(request, *args, **kwargs)


# Início CRUD Distribuidora      
# @transaction.atomic  
def criar_distribuidora(request):    
    form = DistribuidoraForm()
    end_form = EnderecoForm()

    if request.method == 'POST':
        form = DistribuidoraForm(request.POST)
        end_form = EnderecoForm(request.POST)
        if form.is_valid() and end_form.is_valid():
            try:
                with transaction.atomic():
                    distribuidora = form.save(commit=False)
                    endereco = end_form.save()
                    distribuidora.endereco = endereco
                    distribuidora.save()
                    messages.success(request, 'Distribuidora adicionada com sucesso.')
                    return HttpResponseRedirect(reverse('core:distribuidora-detalhe', kwargs={'pk': distribuidora.pk}))
            except Exception as e:
                messages.error(request, e)
    
    return render(request, 'core/distribuidora/novo.html', {'form': form, 'end_form':end_form})


def editar_distribuidora(request, pk):    
    distribuidora = get_object_or_404(Distribuidora, pk=pk)
    form = DistribuidoraForm(instance=distribuidora)
    end_form = EnderecoForm(instance=distribuidora.endereco)

    if request.method == 'POST':
        form = DistribuidoraForm(request.POST, instance=distribuidora)
        end_form = EnderecoForm(request.POST, instance=distribuidora.endereco)
        if form.is_valid() and end_form.is_valid():
            try:
                with transaction.atomic():
                    distribuidora = form.save(commit=False)
                    endereco = end_form.save()
                    distribuidora.endereco = endereco
                    distribuidora.save()
                    messages.success(request, "Distribuidora editada com sucesso.")
                    return HttpResponseRedirect(reverse('core:distribuidora-detalhe', kwargs={'pk': distribuidora.pk}))
            except Exception as e:
                messages.error(request, e)
    
    return render(request, 'core/distribuidora/editar.html', {'form': form, 'end_form':end_form})

class DistribuidoraListar(generic.ListView):
    model = Distribuidora
    paginate_by = 10
    template_name = 'core/distribuidora/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(razao_social__icontains = nome)

class DistribuidoraDetalhe(generic.DetailView):
    model = Distribuidora
    context_object_name = 'distribuidora' 
    template_name = 'core/distribuidora/detalhe.html'


class DistribuidoraDeletar(SuccessMessageMixin, generic.DeleteView):
    model = Distribuidora
    template_name = "core/distribuidora/deletar.html"
    success_url = reverse_lazy('core:distribuidora-listar')
    success_message = "Distribuidora excluída com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DistribuidoraDeletar, self).delete(request, *args, **kwargs)


def carregar_cidades(request):
    estado_id = request.GET.get('estado')
    cidades = Cidade.objects.filter(estado_id=estado_id)    
    return render(request, 'core/ajax/partial_select_cidade.html', {'cidades': cidades})


def buscar_cep(request):
    data = dict()
    cep = request.GET.get('cep')
    try:
        data = consultar_cep(cep)
        estado = Estado.objects.get(sigla=data['uf'])
        cidade = Cidade.objects.get(nome=data['cidade'], estado=estado)

        data['uf'] = estado.id
        data['cidade'] = cidade.id
    except ExcecaoPyCEPCorreios as exc:
        data['error'] = exc.message       

    return JsonResponse(data)

# Início CRUD Item
class ItemCriar(SuccessMessageMixin, generic.CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'core/item/novo.html'
    success_message = "Item adicionado com sucesso."
        
class ItemEditar(SuccessMessageMixin, generic.UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'core/item/editar.html'
    success_message = "Item editado com sucesso."

class ItemListar(generic.ListView):
    model = Item
    paginate_by = 10
    template_name = 'core/item/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(Q(numero_serie__icontains = nome)| Q(filme__titulo__icontains = nome) | Q(filme__titulo_original__icontains=nome))

class ItemDetalhe(generic.DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'core/item/detalhe.html'

class ItemDeletar(SuccessMessageMixin, generic.DeleteView):
    model = Item
    template_name = "core/item/deletar.html"
    success_url = reverse_lazy('core:item-listar')
    success_message = "Item excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ItemDeletar, self).delete(request, *args, **kwargs)

@transaction.atomic
def item_desativar(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.is_active = False
    item.save()
    
    messages.success(request, 'Item desativado com sucesso')
    return HttpResponseRedirect(reverse_lazy('core:item-listar'))

@transaction.atomic
def item_ativar(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.is_active = True
    item.save()

    messages.success(request, 'Item ativado com sucesso')
    return HttpResponseRedirect(reverse_lazy('core:item-listar'))


# Início CRUD Cliente

def criar_cliente(request):    
    form = ClienteForm()
    end_form = EnderecoForm()
    formset = TelefoneInlineFormSet(queryset=Telefone.objects.none())
    today = date.today()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        end_form = EnderecoForm(request.POST)
        formset = TelefoneInlineFormSet(request.POST, queryset=Telefone.objects.none())
        if form.is_valid() and end_form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
                    user.refresh_from_db()
                    user.perfil.cpf = form.cleaned_data.get('cpf')
                    user.perfil.data_nascimento = form.cleaned_data.get('data_nascimento')
                    user.perfil.sexo = form.cleaned_data.get('sexo')
                    
                    endereco = end_form.save()
                    user.perfil.endereco = endereco
                    user.save()
                    
                    telefones = formset.save(commit=False)
                    for fone in telefones:
                        fone.perfil = user.perfil
                        fone.save()
                    
                    cliente = Cliente()
                    cliente.codigo = '%s%s' % (str(today.year), str(user.pk))
                    cliente.local_trabalho = form.cleaned_data.get('local_trabalho')
                    cliente.user = user
                    cliente.save()

                    historico = HistoricoCliente()
                    historico.cliente = cliente
                    historico.save()
                    
                    messages.success(request, 'Cliente adicionada com sucesso.')
                    return HttpResponseRedirect(reverse('core:cliente-detalhe', kwargs={'pk': cliente.pk}))
            except Exception as e:
                messages.error(request, e)
    
    return render(request, 'core/cliente/novo.html', {'form': form, 'end_form': end_form, 'formset': formset})


def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    data_init = {'cpf': cliente.user.perfil.cpf, 'data_nascimento': cliente.user.perfil.data_nascimento, 'sexo':cliente.user.perfil.sexo, 'local_trabalho': cliente.local_trabalho,}
    form = ClienteForm(instance=cliente.user, initial=data_init)
    end_form = EnderecoForm(instance=cliente.user.perfil.endereco)
    formset = TelefoneInlineFormSet(instance=cliente.user.perfil)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente.user)
        end_form = EnderecoForm(request.POST, instance=cliente.user.perfil.endereco)
        formset = TelefoneInlineFormSet(request.POST, instance=cliente.user.perfil)
        if form.is_valid() and end_form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
                    user.refresh_from_db()
                    user.perfil.cpf = form.cleaned_data.get('cpf')
                    user.perfil.data_nascimento = form.cleaned_data.get('data_nascimento')
                    user.perfil.sexo = form.cleaned_data.get('sexo')

                    endereco = end_form.save()
                    user.perfil.endereco = endereco
                    user.save()

                    telefones = formset.save()
                    for fone in telefones:
                        if fone.perfil != user.perfil:
                            fone.perfil = user.perfil
                            fone.save()

                    cliente.local_trabalho = form.cleaned_data.get('local_trabalho')
                    cliente.save()

                    messages.success(request, 'Cliente editado com sucesso.')
                    return HttpResponseRedirect(cliente.get_absolute_url())
            except Exception as e:
                messages.error(request, e)
            
    return render(request, 'core/cliente/editar.html', {'form': form, 'end_form': end_form, 'formset': formset,})


class ClienteListar(generic.ListView):
    model = Cliente
    paginate_by = 10
    template_name = 'core/cliente/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(Q(codigo__icontains = nome) | Q(user__first_name__icontains = nome)| Q(user__last_name__icontains = nome))

class ClienteDetalhe(generic.DetailView):
    model = Cliente
    context_object_name = 'cliente'
    template_name = 'core/cliente/detalhe.html'


class ClienteDeletar(SuccessMessageMixin, generic.DeleteView):
    model = Cliente
    template_name = "core/cliente/deletar.html"
    success_url = reverse_lazy('core:cliente-listar')
    success_message = "Cliente excluído com sucesso."

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ClienteDeletar, self).delete(request, *args, **kwargs)

@transaction.atomic
def cliente_desativar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.is_active = False
    cliente.save()
    
    historico = HistoricoCliente()
    historico.cliente = cliente
    historico.situacao_cliente = False
    historico.save()

    dependentes = Cliente.objects.filter(titular=cliente)

    for d in dependentes:
        d.is_active = False
        d.save()

        historico = HistoricoCliente()
        historico.cliente = d
        historico.titular = cliente
        historico.situacao_cliente = False
        historico.save()

    
    messages.success(request, 'Cliente desativado com sucesso')
    return HttpResponseRedirect(reverse_lazy('core:cliente-listar'))

@transaction.atomic
def cliente_ativar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.is_active = True
    cliente.save()

    historico = HistoricoCliente()
    historico.cliente = cliente
    historico.situacao_cliente = True
    historico.save()

    messages.success(request, 'Cliente ativado com sucesso')
    return HttpResponseRedirect(reverse_lazy('core:cliente-listar'))



# Inicio CRUD Dependente
def criar_dependente(request, pk):
    titular = get_object_or_404(Cliente, pk=pk)

    if titular.quantidade_dependentes() == 3:
        messages.error(request, 'O número máximo de dependentes foi alcançado.')
        return HttpResponseRedirect(reverse('core:dependente-listar', kwargs={'pk': pk}))
    
    form = DependenteForm

    data = dict()
    today = date.today()

    if request.method == 'POST':
        form = DependenteForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
                    user.refresh_from_db()
                    user.perfil.cpf = form.cleaned_data.get('cpf')
                    user.perfil.data_nascimento = form.cleaned_data.get('data_nascimento')
                    user.perfil.sexo = form.cleaned_data.get('sexo')
                    user.save()


                    dependente = Cliente()
                    dependente.codigo = '%s%s%s' % (str(today.year), str(titular.pk), str(user.pk))
                    dependente.user = user
                    dependente.titular = titular
                    dependente.save()

                    historico = HistoricoCliente()
                    historico.cliente = dependente
                    historico.titular = titular
                    historico.save()

                    messages.success(request, 'Dependente salvo com sucesso.')
                    return HttpResponseRedirect(reverse('core:dependente-listar', kwargs={'pk': pk}))
            except Exception as e:
                messages.error(request, e)

    return render(request, 'core/dependente/novo.html', {'form': form, 'pk': pk,})

def editar_dependente(request, pk, id_dep):
    titular = get_object_or_404(Cliente, pk=pk)
    dependente = get_object_or_404(Cliente, pk=id_dep)
    data_init = {'cpf': dependente.user.perfil.cpf, 'data_nascimento': dependente.user.perfil.data_nascimento, 'sexo':dependente.user.perfil.sexo,}
    form = DependenteForm(instance=dependente.user, initial=data_init)
    data = dict()

    if request.method == 'POST':
        form = DependenteForm(request.POST, instance=dependente.user)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
                    user.perfil.cpf = form.cleaned_data.get('cpf')
                    user.perfil.data_nascimento = form.cleaned_data.get('data_nascimento')
                    user.perfil.sexo = form.cleaned_data.get('sexo')
                    user.save()
                    messages.success(request, 'Dependente atualizado com sucesso.')
                    return HttpResponseRedirect(reverse('core:dependente-listar', kwargs={'pk': pk}))
            except Exception as e:
                messages.error(request, e)
            

    context = {'form': form, 'pk': pk, 'id_dep': id_dep,}
    return render(request, 'core/dependente/editar.html', context)


def dependente_listar(request, pk):
    titular = get_object_or_404(Cliente, pk=pk)
    nome = request.GET.get('nome', '')
    dependente_list = Cliente.objects.filter(Q(titular=titular) & (Q(codigo__icontains = nome) | Q(user__first_name__icontains = nome) | Q(user__last_name__icontains = nome)))
    paginator = Paginator(dependente_list, 10)

    page = request.GET.get('page')
    dependentes = paginator.get_page(page)
    return render(request, 'core/dependente/lista.html', {'dependentes': dependentes, 'pk': pk, 'titular': titular,})


def dependente_detalhe(request, pk, id_dep):
    dependente = get_object_or_404(Cliente, pk=id_dep)
    return render(request, 'core/dependente/detalhe.html', {'dependente': dependente, 'pk': pk, 'id_dep': id_dep,})


class DependenteDetalhe(generic.DetailView):
    model = Cliente
    context_object_name = 'dependente'
    template_name = 'core/dependente/detalhe.html'


def dependente_deletar(request, pk, id_dep):
    dependente = get_object_or_404(Cliente, pk=id_dep)
    if request.method == 'POST':
        dependente.delete()
        messages.success(request, 'Dependente atualizado com sucesso.')
        return HttpResponseRedirect(reverse('core:dependente-listar', kwargs={'pk': pk}))
    
    return render(request, 'core/dependente/deletar.html')

@transaction.atomic
def dependente_desativar(request, pk, id_dep):
    titular = get_object_or_404(Cliente, pk=pk)
    dependente = get_object_or_404(Cliente, pk=id_dep)
    
    dependente.is_active = False
    dependente.save()

    historico = HistoricoCliente()
    historico.cliente = dependente
    historico.titular = titular
    historico.situacao_cliente = False
    historico.save()

    messages.success(request, 'Dependente desativado com sucesso')
    return HttpResponseRedirect(reverse('core:dependente-listar', kwargs={'pk': pk}))

@transaction.atomic
def dependente_ativar(request, pk, id_dep):
    titular = get_object_or_404(Cliente, pk=pk)
    dependente = get_object_or_404(Cliente, pk=id_dep)

    dependente.is_active = True
    dependente.save()
    
    historico = HistoricoCliente()
    historico.cliente = dependente
    historico.titular = titular
    historico.situacao_cliente = True
    historico.save()
    
    messages.success(request, 'Dependente ativado com sucesso')
    return HttpResponseRedirect(reverse('core:dependente-listar', kwargs={'pk': pk}))
