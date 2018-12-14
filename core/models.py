from django.db import models
from django.urls import reverse

# Create your models here.

class Genre(models.Model):
    name = models.CharField("Nome", blank=False, null=False, max_length=100)
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

    def get_absolute_url(self):
        return reverse('core:genre-detail', args=[str(self.pk)])

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField("Titulo", blank=True, max_length=100)
    release = models.BooleanField("Lançamento", default=False)
    release_year = models.PositiveSmallIntegerField("Ano Lançamento", blank=True, null=True)
    abstract = models.TextField("Sinopse", blank=True)
    age_min = models.PositiveSmallIntegerField("Idade minima", blank=True, null=True)
    duration = models.PositiveSmallIntegerField("Duração", blank=False, null=False)
    main_actor = models.CharField("Ator Principal", blank=False, max_length=100)
    genre = models.ForeignKey(
        Genre, on_delete=models.PROTECT, verbose_name="genero"
    )
    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'

    def __str__(self):
        return self.title
