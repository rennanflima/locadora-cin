from django.test import TestCase
from core.models import *
from mixer.backend.django import mixer
import pytest

# Create your tests here.
@pytest.mark.django_db
class TestGenero(TestCase):

    def test_str(self):
        genero = mixer.blend('core.Genero', nome='Comédia')
        self.assertEqual(str(genero), 'Comédia')

    def test_get_absolute_url(self):
        genero = mixer.blend('core.Genero', nome='Drama')
        self.assertEqual(genero.get_absolute_url(), '/core/genero/{}/detalhe'.format(genero.pk))