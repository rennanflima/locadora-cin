from django import forms
from .models import *
from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ('nome',)
    
    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)


class FilmeForm(ModelForm):
    class Meta:
        model = Filme
        fields = ('titulo', 'titulo_original', 'duracao', 'diretor', 'ano', 'pais', 'classificacao', 'genero', 'sinopse',)
    
    def __init__(self, *args, **kwargs):
        
        campos = ('titulo', 'titulo_original', 'diretor', 'ano', 'pais', 'classificacao', 'genero', 'sinopse',)
        for c in campos:
            self.base_fields[c].widget.attrs['class'] = 'form-control'
        
        self.base_fields['duracao'].widget.attrs['class'] = 'form-control time'
        super(FilmeForm, self).__init__(*args, **kwargs)

class MidiaForm(ModelForm):
    valor = forms.DecimalField(label='Valor da Locação', max_digits=8, decimal_places=2, localize=True)
    class Meta:
        model = Midia
        fields = ('nome','valor',)
    
    def __init__(self, *args, **kwargs):
        self.base_fields['valor'].localize = True
        self.base_fields['valor'].widget.is_localized = True
        self.base_fields['valor'].widget.attrs['class'] = 'form-control money2'
        super(MidiaForm, self).__init__(*args, **kwargs)