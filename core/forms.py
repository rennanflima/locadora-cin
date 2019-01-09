from django import forms
from .models import *
from django.forms import ModelForm

class GeneroForm(ModelForm):
    class Meta:
        model = Genero
        fields = ('nome',)
    
    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)
