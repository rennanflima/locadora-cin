from django.db import models
from django.urls import reverse
from multiselectfield import MultiSelectField
from core.choices import *


# Create your models here.
class Genero(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)

    def __str__(self):
        return "%s" % self.nome 

    def get_absolute_url(self):
        return reverse('admin:genero-detalhe', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['nome',]
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'

class Artista(models.Model):
    nome = models.CharField('Nome', max_length=150, unique=True)
    tipo = MultiSelectField('Atividade', choices=tipo_pessoa_filme)

    def __str__(self):
        return "%s" % self.nome 

    def get_absolute_url(self):
        return reverse('admin:artista-detalhe', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['nome',]
        verbose_name = 'Artista'
        verbose_name_plural = 'Artistas'

class Filme(models.Model):
    titulo = models.CharField('Título em Português', max_length=150) 
    titulo_original = models.CharField('Título Original', max_length=150)
    sinopse = models.TextField('Sinopse')
    classificacao = models.CharField('Classificação Indicativa', max_length=2, choices=tipo_classificacao)
    duracao = models.TimeField('Duração')
    diretor = models.ManyToManyField(Artista)
    ano = models.PositiveSmallIntegerField('Ano de Lançamento')
    pais = models.CharField('País', max_length=150)
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return "%s (%s)" % (self.titulo, self.titulo_original)
    
    def get_absolute_url(self):
        return reverse('admin:filme-detalhe', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['titulo',]
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

class Elenco(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE)
    ator =  models.ForeignKey(Artista, on_delete=models.CASCADE)
    personagem = models.CharField('Personagem', max_length=150, null=True, blank=True)
    principal = models.BooleanField('Principal ?', default=False)

    def __str__(self):
        return "%s (%s)" % (self.ator, self.personagem)

    def get_absolute_url(self):
        return reverse('admin:elenco-detalhe', kwargs={'pk': self.pk})

    class Meta:
        unique_together = ('filme', 'ator')
        ordering = ['ator', 'principal', ]
        verbose_name = 'Elenco'
        verbose_name_plural = 'Elencos'

class Midia(models.Model):
    nome = models.CharField('Nome', max_length=100, unique=True)
    valor = models.DecimalField('Valor da Locação', max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return "%s" % self.nome

    def get_absolute_url(self):
        return reverse('admin:midia-detalhe', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['nome',]
        verbose_name = 'Tipo de Mídia'
        verbose_name_plural = 'Tipos de Mídias'