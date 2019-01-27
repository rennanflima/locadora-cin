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
        self.assertEqual(genero.get_absolute_url(), '/admin/genero/{}/detalhe/'.format(genero.pk))

class TestFilme(TestCase):

    def test_str(self):
        filme = mixer.blend('core.Filme', titulo='Velocidade Máxima', titulo_original='Speed')
        self.assertEqual(str(filme), "%s (%s)" % ('Velocidade Máxima', 'Speed'))

    def test_get_absolute_url(self):
        filme = mixer.blend('core.Filme', titulo='A Rocha', titulo_original='The Rock')
        self.assertEqual(filme.get_absolute_url(), '/admin/filme/{}/detalhe/'.format(filme.pk))

class TestMidia(TestCase):

    def test_str(self):
        midia = mixer.blend('core.Midia', nome='DVD')
        self.assertEqual(str(midia), 'DVD')

    def test_get_absolute_url(self):
        midia = mixer.blend('core.Midia', nome='VHS')
        self.assertEqual(midia.get_absolute_url(), '/admin/midia/{}/detalhe/'.format(midia.pk))
