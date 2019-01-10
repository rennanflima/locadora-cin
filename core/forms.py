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
        fields = ('titulo', 'titulo_original', 'duracao', 'diretor', 'data_lancamento', 'pais', 'classificacao','genero','sinopse',)
    
    def __init__(self, *args, **kwargs):
        self.base_fields['data_lancamento'].widget.attrs['class'] = 'data'
        self.base_fields['duracao'].widget.attrs['class'] = ' time'
        self.base_fields["genero"].widget = forms.CheckboxSelectMultiple()
        super(FilmeForm, self).__init__(*args, **kwargs)