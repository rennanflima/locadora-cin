from django.db import models
from django.urls import reverse

# Create your models here.
class Genero(models.Model):
    nome = models.CharField('Nome', max_length=100)

    def __str__(self):
        return "%s" % self.nome 

    def get_absolute_url(self):
        return reverse('core:genero-detalhe', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Gênero'
        verbose_name_plural = 'Gêneros'
