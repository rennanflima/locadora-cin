from django.urls import reverse
from django.test import RequestFactory
from django.contrib.auth.models import User
from core.views import *
from mixer.backend.django import mixer
import pytest
from django.test import TestCase

@pytest.mark.django_db
class TestGeneroViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestGeneroViews, cls).setUpClass()
        cls.genero = mixer.blend('core.Genero')
        cls.factory = RequestFactory()
    
    def test_genero_lista(self):
        path = reverse('core:genero-listar')
        request = self.factory.get(path)
        # request.user = mixer.blend(User)

        response = GeneroListar.as_view()(request)
        assert response.status_code == 200
        print(response)
        # assert 'core/genero/lista.html' in response.url
        # self.assertEqual(response.url, 'core/genero/lista.html')
        
    
    def test_genero_novo(self):
        path = reverse('core:genero-novo')
        request = self.factory.get(path)
        # request.user = mixer.blend(User)

        response = GeneroCriar.as_view()(request)
        assert response.status_code == 200
    
    def test_genero_detalhe(self):
        path = reverse('core:genero-detalhe', kwargs={'pk': self.genero.pk})
        request = RequestFactory().get(path)
        # request.user = mixer.blend(User)

        response = GeneroDetalhe.as_view()(request, pk=self.genero.pk)
        assert response.status_code == 200
    
    def test_genero_editar(self):
        path = reverse('core:genero-edita', kwargs={'pk': self.genero.pk})
        request = RequestFactory().get(path)
        # request.user = mixer.blend(User)

        response = GeneroEditar.as_view()(request, pk=self.genero.pk)
        assert response.status_code == 200
    
    def test_genero_deletar(self):
        path = reverse('core:genero-deletar', kwargs={'pk': self.genero.pk})
        request = RequestFactory().get(path)
        # request.user = mixer.blend(User)

        response = GeneroDeletar.as_view()(request, pk=self.genero.pk)
        assert response.status_code == 200

