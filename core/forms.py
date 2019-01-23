from django import forms
from django.forms import BaseInlineFormSet
from core.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ('nome',)
    
    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)

class ArtistaForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ('nome', 'tipo',)
    
    def __init__(self, *args, **kwargs):
        super(ArtistaForm, self).__init__(*args, **kwargs)


class DiretorForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ('nome',)
    
    def __init__(self, *args, **kwargs):
        super(DiretorForm, self).__init__(*args, **kwargs)


class AtorForm(forms.ModelForm):
    class Meta:
        model = Artista
        fields = ('nome',)
    
    def __init__(self, *args, **kwargs):
        super(AtorForm, self).__init__(*args, **kwargs)


class FilmeForm(forms.ModelForm):
    diretor = forms.ModelMultipleChoiceField(queryset = Artista.objects.filter(tipo__icontains='Diretor'))
    class Meta:
        model = Filme
        fields = ('titulo', 'titulo_original', 'duracao', 'diretor', 'ano', 'pais', 'classificacao', 'genero', 'sinopse',)
    
    def __init__(self, *args, **kwargs):
        super(FilmeForm, self).__init__(*args, **kwargs)

        self.base_fields['duracao'].widget.attrs['class'] = 'time'
        
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('titulo', css_class='form-group col-md-6 mb-0'),
                Column('titulo_original', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('classificacao', css_class='form-group col-md-4 mb-0'),
                Column('duracao', css_class='form-group col-md-2 mb-0'),
                Column('ano', css_class='form-group col-md-3 mb-0'),
                Column('pais', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('diretor', css_class='form-group col-md-6 mb-0'),
                Column('genero', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'sinopse',
            # HTML('<hr>'),
            # HTML("<a href='{% url 'admin:genero-novo' %}' class='btn btn-primary ml-2 mb-4 float-right'>Adicionar Gênero</a>"),
            # HTML("<a href='{% url 'admin:filme-listar' %}' class='btn btn-danger ml-2 float-right'>Cancelar</a>"),
            # Submit('save_changes', 'Adicionar Filme', css_class="btn-success ml-2 mb-4 float-right"),
        )

class MidiaForm(forms.ModelForm):
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

class ElencoForm(forms.ModelForm):
    ator = forms.ModelChoiceField(queryset = Artista.objects.filter(tipo__icontains='Ator'), empty_label='Selecione um ator ...')
    # DELETE = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'hidden'}), required=False)
    class Meta:
        model = Elenco
        fields = ('ator', 'personagem', 'principal', )
    
    def __init__(self, *args, **kwargs):
        super(ElencoForm, self).__init__(*args, **kwargs)

class BaseElencoFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseElencoFormSet, self).__init__(*args, **kwargs)

        for form in self.forms:
            form.fields['ator'].queryset = Artista.objects.filter(tipo__icontains='Ator')
            form.fields['ator'].widget.attrs['class'] = 'form-control js-ator'

    def clean(self):
        for form in self.forms:
            if form.cleaned_data:
                if 'ator' in form.cleaned_data:
                    ator = form.cleaned_data['ator']
                else:
                    ator = None
                
                if 'personagem' in form.cleaned_data:
                    personagem = form.cleaned_data['personagem']
                else:
                    personagem = None

                if 'principal' in form.cleaned_data:
                    principal = form.cleaned_data['principal']
                else:
                    principal = None

                if not ator and not personagem:
                    form.cleaned_data['ator'] = None
                    form.cleaned_data['personagem'] = None
                    form.cleaned_data['principal'] = None
                    form.cleaned_data['DELETE'] = True   

                # print(form.prefix+' '+str(form.cleaned_data['DELETE']))

                if ator and not personagem:
                    raise forms.ValidationError('É obrigatório informar o personagem', code='missing_personagem')

        if any(self.errors):
            return




    

ElencoInlineFormSet = forms.inlineformset_factory(
    Filme, 
    Elenco, 
    form=ElencoForm,
    extra=1,
    formset=BaseElencoFormSet,
    widgets={'personagem': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Informe o personagem aqui'
            }),
    },
    min_num=1,
    can_delete=True,
)