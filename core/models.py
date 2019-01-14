from django.db import models
from django.urls import reverse


# Create your models here.
class Genero(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return "%s" % self.nome 

    def get_absolute_url(self):
        return reverse('admin:genero-detalhe', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['nome',]
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'


class Filme(models.Model):
    tipo_classificacao = (
        ('L', 'Livre'),
        ('10', 'Não recomendado para menores de 10 anos'),
        ('12', 'Não recomendado para menores de 12 anos'),
        ('14', 'Não recomendado para menores de 14 anos'),
        ('16', 'Não recomendado para menores de 16 anos'),
        ('18', 'Não recomendado para maiores de 18 anos'),
    )
    titulo = models.CharField('Título', max_length=150) 
    titulo_original = models.CharField('Título Original', max_length=150)
    sinopse = models.TextField('Sinopse')
    classificacao = models.CharField('Classificação Indicativa', max_length=2, choices=tipo_classificacao)
    duracao = models.TimeField('Duração')
    diretor = models.CharField('Diretor', max_length=150)
    data_lancamento = models.DateField('Data de Lançamento')
    pais = models.CharField('País da Data de Lançamento', max_length=150)
    genero = models.ManyToManyField(Genero)

    def __str__(self):
        return "%s (%s)" % (self.titulo, self.titulo_original)
    
    def get_absolute_url(self):
        return reverse('admin:filme-detalhe', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['titulo',]
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'