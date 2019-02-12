import django_filters
from core.models import *

class ItemFilter(django_filters.FilterSet):
    class Meta:
        model = Item
        fields = {
            'numero_serie': ['exact', ], 
            'filme__titulo_original': ['icontains', ], 
            'filme__titulo': ['icontains', ],
        }