from django import forms
from django.forms import BaseInlineFormSet
from core.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, HTML
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from localflavor.br.forms import BRCPFField, BRCNPJField, BRZipCodeField

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
            # HTML("<a href='{% url 'core:genero-novo' %}' class='btn btn-primary ml-2 mb-4 float-right'>Adicionar Gênero</a>"),
            # HTML("<a href='{% url 'core:filme-listar' %}' class='btn btn-danger ml-2 float-right'>Cancelar</a>"),
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
            HTML("<a href='{% url 'core:filme-novo' %}' class='btn btn-primary ml-2 mb-4 float-right'>Adicionar Filme</a>"),
            HTML("<a href='{% url 'core:midia-listar' %}' class='btn btn-danger ml-2 float-right'>Cancelar</a>"),
            Submit('save_changes', 'Adicionar Tipo de Mídia', css_class="btn-success ml-2 mb-4 float-right"),

        )

class ElencoForm(forms.ModelForm):
    ator = forms.ModelChoiceField(queryset = Artista.objects.filter(tipo__icontains='Ator'), empty_label='Selecione um ator ...')
    # DELETE = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': 'hidden'}), required=False)
    class Meta:
        model = Elenco
        fields = ('ator', 'personagem', 'principal', )
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
    
    def __init__(self, *args, **kwargs):
        super(ElencoForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(ElencoForm, self).clean()




class BaseElencoFormSet(BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseElencoFormSet, self).__init__(*args, **kwargs)

        for form in self.forms:
            form.fields['ator'].queryset = Artista.objects.filter(tipo__icontains='Ator')
            form.fields['ator'].widget.attrs['class'] = 'form-control js-ator'


    def clean(self):
        atores = []
        personagens = []
        duplicates = False
        print('BaseElencoFormSet: clean')

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

                try:
                    print('try BaseElencoFormSet')
                    artistas_filme = Elenco.objects.get(filme=form.cleaned_data['filme'], ator=ator)
                    if artistas_filme:
                        form.add_error('ator', '%s já está listado no elenco deste filme' % ator)
                except:
                    pass
                    

                if ator and personagem:
                    if ator in atores:
                        duplicates = True    
                    atores.append(ator)

                    if personagem in personagens:
                        duplicates = True
                    personagens.append(personagem)
                
                if duplicates:
                    raise forms.ValidationError('O Elenco deve ter atores e personagem exclusivo.', code='duplicates_ator')
        
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

class EnderecoForm(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset = Estado.objects.all(), empty_label='Selecione um estado ...')

    class Meta:
        model = Endereco
        fields = ('logradouro','numero','complemento', 'bairro', 'cep', 'cidade')
    
    def __init__(self, *args, **kwargs):
        super(EnderecoForm, self).__init__(*args, **kwargs)
        self.base_fields['cep'].widget.attrs['class'] = 'form-control cep'
        self.base_fields['cidade'].queryset = Cidade.objects.none()

    def clean(self):
        self.cleaned_data['cidade'] = self.clean_cidade()
        return self.cleaned_data

    def clean_cidade(self):
        if self['cidade'].value() != '':
            del self._errors['cidade']
        return self['cidade']


class DistribuidoraForm(forms.ModelForm):
    class Meta:
        model = Distribuidora
        fields = ('razao_social','cnpj','contato', 'telefone')
    
    def __init__(self, *args, **kwargs):
        super(DistribuidoraForm, self).__init__(*args, **kwargs)
        self.base_fields['cnpj'].widget.attrs['class'] = 'form-control cnpj'
        self.base_fields['telefone'].widget.attrs['class'] = 'form-control sp_celphones'



