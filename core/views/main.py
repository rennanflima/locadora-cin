from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from core.models import *
from core.forms import *
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from datetime import date
from datetime import timedelta 
from django.utils.formats import localize
from django.core.serializers import serialize
import json

class IndexView(generic.TemplateView):
    template_name = "core/index.html"

# Início das views de Reserva de filme



class ReservaListar(generic.ListView):
    model = Reserva
    paginate_by = 10
    template_name = 'core/reserva/lista.html'    

    def get_queryset(self):
        nome = self.request.GET.get('nome', '')
        return self.model.objects.filter(Q(filme__titulo__icontains = nome) | Q(filme__titulo_original__icontains=nome) | Q(cliente__user__first_name__icontains = nome) | Q(cliente__user__last_name__icontains = nome))
            # Q(cliente__codigo__icontains = nome) | 

class ReservaCriar(SuccessMessageMixin, generic.CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'core/reserva/novo.html'
    success_message = "Reserva adicionada com sucesso."

class ReservaDetalhe(generic.DetailView):
    model = Reserva
    context_object_name = 'reserva'
    template_name = 'core/reserva/detalhe.html'

class ReservaEditar(SuccessMessageMixin, generic.UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'core/reserva/editar.html'
    success_message = "Reserva editada com sucesso."

def carregar_tipo_midia(request):
    filme_id = request.GET.get('filme')
    midias = Midia.objects.filter(item_midia__filme_id=filme_id)    
    return render(request, 'core/ajax/partial_select_midia.html', {'midias': midias})

def reserva_cancelar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.status = 'Expirada'
        messages.success(request, 'Reserva cancelada com sucesso.')
        return HttpResponseRedirect(reverse_lazy('core:reserva-listar'))
    
    return render(request, 'core/reserva/cancelar.html')



# Início das views de Locação

class LocacaoListar(generic.ListView):
    model = Locacao
    paginate_by = 10
    template_name = 'core/locacao/lista.html'   


class LocacaoDetalhe(generic.DetailView):
    model = Locacao
    context_object_name = 'locacao'
    template_name = 'core/locacao/detalhe.html'


def realizar_locacao(request):
    form = LocacaoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            locacao = form.save()
            return HttpResponseRedirect(reverse('core:locacao-realizar-itens', kwargs={'pk': locacao.pk}))    
    return render(request, 'core/locacao/buscar_cliente.html', {'form': form})


def seleciona_itens_locacao(request, pk):
    locacao = get_object_or_404(Locacao, pk=pk)
    itens = ItemLocacao.objects.filter(locacao=locacao)
    return render(request, 'core/locacao/itens_locacao.html', {'itens_list': itens, 'locacao': locacao,})



def save_item_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            locacao = form.cleaned_data.get('locacao') 
            valor = form.cleaned_data.get('valor')
            locacao.valor_total = locacao.valor_total + valor
            locacao.save()
            itens_list = ItemLocacao.objects.filter(locacao=locacao)
            data['html_item_list'] = render_to_string('core/ajax/partial_itens_list.html', {'itens_list': itens_list, })
        else:
            data['form_is_valid'] = False

    context = { 'form' : form }
    data['html_form'] = render_to_string(template_name, context, request=request,)
    return JsonResponse(data)

def item_add(request):
    form = ItemLocacaoForm(request.POST or None)
    return save_item_form(request, form, 'core/ajax/partial_item_add.html' )


def item_edit(request, pk):
    item = get_object_or_404(ItemLocacao, pk=pk)
    form = ItemLocacaoForm(request.POST or None, instance=item)
    return save_item_form(request, form, 'core/ajax/partial_item_update.html' )


def item_delete(request, pk):
    item = get_object_or_404(ItemLocacao, pk=pk)
    locacao = item.locacao
    data = dict()
    if request.method == 'POST':
        item.delete()
        data['form_is_valid'] = True
        itens_list = ItemLocacao.objects.filter(locacao=locacao)
        data['html_item_list'] = render_to_string('core/ajax/partial_itens_list.html', {'itens_list': itens_list, })
    else:
        context = {'item': item}
        data['html_form'] = render_to_string('core/ajax/partial_item_delete.html', context, request=request,)
    return JsonResponse(data)


def carregar_item_ajax(request):
    data = dict()
    item_id = request.GET.get('item')
    item = get_object_or_404(Item, pk=item_id)
    data['valor'] = localize(item.tipo_midia.valor)
    today = date.today()
    if item.filme.is_lancamento:
        data['data_devolucao'] = (today + timedelta(days=1)).strftime("%d/%m/%Y")   
    else:
        data['data_devolucao'] = (today + timedelta(days=3)).strftime("%d/%m/%Y")
    return JsonResponse(data)

class LocacaoDetalhe(generic.DetailView):
    model = Locacao
    context_object_name = 'locacao'
    template_name = 'core/locacao/detalhe.html'

    def get_context_data(self, **kwargs):
        context = super(LocacaoDetalhe, self).get_context_data(**kwargs)
        context['item_list'] = ItemLocacao.objects.filter(locacao=self.object)
        return context



    