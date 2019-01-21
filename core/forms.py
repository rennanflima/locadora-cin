from django import forms
from core.models import *
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ('nome',)
    
    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)

class PessoaFilmeForm(ModelForm):
    class Meta:
        model = PessoaFilme
        fields = ('nome', 'tipo',)
    
    def __init__(self, *args, **kwargs):
        super(PessoaFilmeForm, self).__init__(*args, **kwargs)


class FilmeForm(ModelForm):
    diretor = forms.ModelMultipleChoiceField(queryset = PessoaFilme.objects.filter(tipo__icontains='Diretor'))
    class Meta:
        model = Filme
        fields = ('titulo', 'titulo_original', 'duracao', 'diretor', 'ano', 'pais', 'classificacao', 'genero', 'sinopse',)
    
    def __init__(self, *args, **kwargs):
        super(FilmeForm, self).__init__(*args, **kwargs)

        self.base_fields['duracao'].widget.attrs['class'] = 'time'
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('titulo', css_class='form-group col-md-6 mb-0'),
                Column('titulo_original', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('classificacao', css_class='form-group col-md-4 mb-0'),
                Column('duracao', css_class='form-group col-md-2 mb-0'),
                Column('ano', css_class='form-group col-md-4 mb-0'),
                Column('pais', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('diretor', css_class='form-group col-md-6 mb-0'),
                Column('genero', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'sinopse'
        )

class MidiaForm(ModelForm):
    valor = forms.DecimalField(label='Valor da Locação', max_digits=8, decimal_places=2, localize=True)
    class Meta:
        model = Midia
        fields = ('nome','valor',)
    
    def __init__(self, *args, **kwargs):
        super(MidiaForm, self).__init__(*args, **kwargs)
        self.base_fields['valor'].localize = True
        self.base_fields['valor'].widget.is_localized = True
        self.base_fields['valor'].widget.attrs['class'] = 'form-control money2'
        
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'nome',
            PrependedText('valor','R$'),
            HTML('<hr>'),
            HTML("<a href='{% url 'admin:filme-novo' %}' class='btn btn-primary ml-2 mb-4 float-right'>Adicionar Filme</a>"),
            HTML("<a href='{% url 'admin:midia-listar' %}' class='btn btn-danger ml-2 float-right'>Cancelar</a>"),
            Submit('save_changes', 'Adicionar Tipo de Mídia', css_class="btn-success ml-2 mb-4 float-right"),

        )