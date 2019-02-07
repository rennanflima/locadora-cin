from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from core.models import *
from core.forms import *
from django.db.models import Q
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from datetime import date
from datetime import timedelta 
from django.utils.formats import localize
from django.core.serializers import serialize
from django.db import transaction
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

# Step 1 - Locação
def realizar_locacao(request, pk = None):
    if pk:
        locacao = get_object_or_404(Locacao, pk=pk)
        if locacao.is_editavel:
            messages.error(request, 'Locação não pode ser editada.')
            return HttpResponseRedirect(reverse_lazy('core:locacao-listar'))
        form = LocacaoForm(request.POST or None, instance=locacao)
    else:
        form = LocacaoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            locacao = form.save()
            return HttpResponseRedirect(reverse('core:locacao-realizar-itens', kwargs={'pk': locacao.pk}))    
    return render(request, 'core/locacao/buscar_cliente.html', {'form': form})

# Step 2 - Locação
def seleciona_itens_locacao(request, pk):
    locacao = get_object_or_404(Locacao, pk=pk)
    if locacao.is_editavel:
            messages.error(request, 'Locação não pode ser editada.')
            return HttpResponseRedirect(reverse_lazy('core:locacao-listar'))
    itens = ItemLocacao.objects.filter(locacao=locacao)
    if request.method == 'POST':
        if itens.count() > 0:
            return HttpResponseRedirect(reverse('core:locacao-confirmar', kwargs={'pk': locacao.pk}))
        else:
            messages.error(request, 'Você precisa selecionar pelo menos item para realizar a locação')
    return render(request, 'core/locacao/itens_locacao.html', {'itens_list': itens, 'locacao': locacao,})

# Step 3 - Locação
def confirmar_locacao(request, pk):
    locacao = get_object_or_404(Locacao, pk=pk)
    if locacao.is_editavel:
            messages.error(request, 'Locação não pode ser editada.')
            return HttpResponseRedirect(reverse_lazy('core:locacao-listar'))
    itens = ItemLocacao.objects.filter(locacao=locacao)
    if request.method == 'POST':
        locacao.situacao = 'CONCLUIDA'
        locacao.save()
        messages.success(request, 'Locação concluída com sucesso.')
        return HttpResponseRedirect(reverse('core:locacao-finalizar', kwargs={'pk': locacao.pk}))
    return render(request, 'core/locacao/confirma.html', {'item_list': itens, 'locacao': locacao,})

# Step 4 - Locação
def finalizar_locacao(request, pk):
    locacao = get_object_or_404(Locacao, pk=pk)
    if locacao.is_editavel:
            messages.error(request, 'Locação não pode ser editada.')
            return HttpResponseRedirect(reverse_lazy('core:locacao-listar'))
    itens = ItemLocacao.objects.filter(locacao=locacao)
    pagamentos = Pagamento.objects.filter(locacao=locacao)
    valor_restante = locacao.valor_total - locacao.valor_pago()
    if request.method == 'POST':
        if valor_restante == 0:
            locacao.situacao = 'PAGA'
        elif valor_restante < locacao.valor_total:
            locacao.situacao = 'PAGA_PARCIAL'
        locacao.save()
        messages.success(request, 'Locação realizada com sucesso.')
        return HttpResponseRedirect(reverse_lazy('core:locacao-listar'))
    return render(request, 'core/locacao/finalizar.html', {'item_list': itens, 'locacao': locacao, 'pagamentos': pagamentos, 'valor_restante': valor_restante,})


@transaction.atomic
def save_item_form(request, form, template_name, mensagem):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            locacao = form.cleaned_data.get('locacao')

            itens_list = ItemLocacao.objects.filter(locacao=locacao)
            
            soma = 0
            desconto = 0
            for i in itens_list:
                soma = soma + i.valor
                desconto = desconto + i.desconto

            locacao.sub_total = soma
            locacao.total_descontos = desconto
            locacao.save()

            data['qtd_item'] = itens_list.count()
            data['sub_total'] = localize(locacao.sub_total)
            data['total_descontos'] = localize(locacao.total_descontos)
            data['valor_total'] = localize(locacao.valor_total)
            data['html_item_list'] = render_to_string('core/ajax/partial_itens_list.html', {'itens_list': itens_list, })
        else:
            data['form_is_valid'] = False

    context = { 'form' : form }
    data['html_form'] = render_to_string(template_name, context, request=request,)
    return JsonResponse(data)

def item_add(request):
    form = ItemLocacaoForm(request.POST or None)
    return save_item_form(request, form, 'core/ajax/partial_item_add.html', 'Item adicionado com sucesso')


def item_edit(request, pk):
    item = get_object_or_404(ItemLocacao, pk=pk)
    form = ItemLocacaoForm(request.POST or None, instance=item)
    return save_item_form(request, form, 'core/ajax/partial_item_update.html', 'Item alterado com sucesso')


@transaction.atomic
def item_delete(request, pk):
    item = get_object_or_404(ItemLocacao, pk=pk)
    locacao = item.locacao
    data = dict()
    if request.method == 'POST':
        item.delete()
        data['form_is_valid'] = True
        itens_list = ItemLocacao.objects.filter(locacao=locacao)

        soma = 0
        desconto = 0
        for i in itens_list:
            soma = soma + i.valor
            desconto = desconto + i.desconto

        locacao.sub_total = soma
        locacao.total_descontos = desconto
        locacao.save()

        data['qtd_item'] = itens_list.count()
        data['sub_total'] = localize(locacao.sub_total)
        data['total_descontos'] = localize(locacao.total_descontos)
        data['valor_total'] = localize(locacao.valor_total)
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
        context['pagamentos'] = Pagamento.objects.filter(locacao=self.object)
        return context


@transaction.atomic
def pagamento_locacao(request):
    data = dict()
    formas_pagamento = FormaPagamento.objects.all()
    if request.method == 'POST':
        data['form_is_valid'] = True
        fp_id = request.POST.get('forma_pagamento')
        lc_id = request.POST.get('locacao')

        locacao = Locacao.objects.get(pk=lc_id)
        forma_pagamento = FormaPagamento.objects.get(pk=fp_id)
        argumentos = ArgumentoPagamento.objects.filter(forma_pagamento=forma_pagamento)

        pagamento = Pagamento()
        pagamento.locacao = locacao
        pagamento.forma_pagamento = forma_pagamento
        pagamento.save()
        
        locacao = request.POST.get('locacao')
        
        campos = dict()
        for arg in argumentos:
            campos[arg.slug()] = arg.pk

        for k, v in campos.items():
            vlr = request.POST.get(k)
            arg = ArgumentoPagamento.objects.get(pk=v)
            info_pg = InformacaoPagamento()
            info_pg.argumento = arg
            if arg.tipo_dado == 'TEXTO':
                info_pg.valor_texto = vlr
            elif arg.tipo_dado == 'INTEIRO':
                info_pg.valor_inteiro = vlr
            elif arg.tipo_dado == 'DECIMAL':
                info_pg.valor_decimal = vlr
            elif arg.tipo_dado == 'BOOLEAN':
                info_pg.valor_boolean = vlr
            elif arg.tipo_dado == 'DATA':
                info_pg.valor_data = vlr
            elif arg.tipo_dado == 'HORA':
                info_pg.valor_hora = vlr
            elif arg.tipo_dado == 'DATA_HORA':
                info_pg.valor_data_hora = vlr

            info_pg.pagamento = pagamento
            info_pg.save()
        
        valor_restante = locacao.valor_total - locacao.valor_pago()
        
        if valor_restante == 0:
            locacao.situacao = 'PAGA'
            locacao.save()
        elif valor_restante < locacao.valor_total:
            locacao.situacao = 'PAGA_PARCIAL'
            locacao.save()

        pagamentos = Pagamento.objects.filter(locacao=locacao)        
        data['html_pg_list'] = render_to_string('core/ajax/partial_pagamentos_list.html', {'pagamentos': pagamentos, })
    context = {'formas_pagamento': formas_pagamento}
    data['html_form'] = render_to_string('core/ajax/partial_pagamento_novo.html', context, request=request,)
    return JsonResponse(data)


def carregar_argumento_forma_pagamento(request):
    forma_pagamento_id = request.GET.get('forma')
    argumentos = ArgumentoPagamento.objects.filter(forma_pagamento__id=forma_pagamento_id)
    return render(request, 'core/ajax/partial_campos_pagamento.html', {'argumentos': argumentos})


def detalhe_pagamento(request, pk):
    pagamento = get_object_or_404(Pagamento, pk=pk)
    data = dict()
    context = {'pagamento': pagamento, 'dados_pagamento': pagamento.informacoes_pagamentos.all()}
    data['html_form'] = render_to_string('core/ajax/partial_detalhe_pagamento.html', context, request=request,)
    return JsonResponse(data)

    