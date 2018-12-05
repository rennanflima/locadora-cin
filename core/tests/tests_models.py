from django.test import TestCase
from ..models import Genre

# Create your tests here.

class GenreTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Genre.objects.create(name='Drama')

    def test_get_absolute_url(self):
        genre = Genre.objects.get(name='Drama')
        self.assertEquals(genre.get_absolute_url(), '/core/genero/{}'.format(genre.pk))
