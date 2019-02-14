import django_filters
from django import forms
from core.models import *

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = {
            'numero_serie': ['exact', ], 
            'filme__titulo_original': ['icontains', ], 
            'filme__titulo': ['icontains', ],
        }

class FilmeFilter(django_filters.FilterSet):
    genero = django_filters.ModelMultipleChoiceFilter(queryset=Genero.objects.all(), widget=forms.CheckboxSelectMultiple)
    diretor = django_filters.CharFilter(label='Diretor',lookup_expr='icontains', field_name='diretor__nome')
    tipo_midia = django_filters.ModelChoiceFilter(label='Tipo de Mídia', queryset=Midia.objects.all(), field_name='item_filme__tipo_midia')
    ator = django_filters.CharFilter(label='Ator',lookup_expr='icontains', field_name='elenco__ator__nome')
    # lancamento = django_filters.BooleanFilter
    class Meta:
        model = Filme
        fields = ['titulo', 'titulo_original', 'genero', 'diretor', 'pais', 'is_lancamento',]
        filter_overrides = {
             models.BooleanField: {
                 'filter_class': django_filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
         }