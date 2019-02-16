from django.urls import reverse
from django.test import RequestFactory
from core.views.cruds_views import *
from mixer.backend.django import mixer
from django.contrib.auth.models import Permission, AnonymousUser
from django.core.exceptions import PermissionDenied
import pytest
from django.test import TestCase
from django.test import Client

@pytest.mark.django_db
class TestGeneroViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestGeneroViews, cls).setUpClass()
        number_of_generos = 13
        for i in range(number_of_generos):
            cls.genero = mixer.blend('core.Genero')
        cls.factory = RequestFactory()
        cls.user = mixer.blend('core.User', email="test@test.com", password="test")
        cls.user.user_permissions.set(Permission.objects.filter(content_type__model='genero', content_type__app_label='core'))
        cls.client = Client()
        
    
    def test_genero_lista_by_url(self):
        request = self.factory.get('/admin/genero/')
        request.user = self.user

        response = GeneroListar.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_genero_lista_by_name(self):
        path = reverse('core:genero-listar')
        request = self.factory.get(path)
        request.user = self.user

        response = GeneroListar.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_genero_lista_uses_correct_template(self):
        path = reverse('core:genero-listar')
        request = self.factory.get(path)
        request.user = self.user

        response = GeneroListar.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response, 'core/genero/lista.html')
    #     response = self.client.get(reverse('authors'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'catalog/author_list.html')

    def test_genero_lista_redirect_if_not_logged_in(self):
        # path = reverse('core:genero-listar')
        # request = self.factory.get(path)
        # request.user = AnonymousUser()
        # response = GeneroListar.as_view()(request)
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(response.url, '/accounts/login/?next=/admin/genero/')
        #                     or
        response = self.client.get(reverse('core:genero-listar'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/login/?next=/admin/genero/')

    def test_genero_lista_not_permission(self):
        path = reverse('core:genero-listar')
        request = self.factory.get(path)
        request.user = mixer.blend('core.User')
        with self.assertRaises(PermissionDenied):
            response = GeneroListar.as_view()(request)


    def test_genero_lista_pagination_is_ten(self):
        path = reverse('core:genero-listar')
        request = self.factory.get(path)
        request.user = self.user

        response = GeneroListar.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context_data)
        self.assertTrue(response.context_data['is_paginated'] == True)
        self.assertTrue(len(response.context_data['object_list']) == 10)

    def test_genero_lista_all(self):
        path = reverse('core:genero-listar')
        # Get second page and confirm it has (exactly) remaining 3 items
        request = self.factory.get(path+'?page=2')
        request.user = self.user

        response = GeneroListar.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context_data)
        self.assertTrue(response.context_data['is_paginated'] == True)
        self.assertTrue(len(response.context_data['object_list']) == 3)
        
    
    def test_genero_novo(self):
        path = reverse('core:genero-novo')
        request = self.factory.get(path)
        request.user = self.user

        response = GeneroCriar.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_genero_detalhe(self):
        path = reverse('core:genero-detalhe', kwargs={'pk': self.genero.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = GeneroDetalhe.as_view()(request, pk=self.genero.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_genero_editar(self):
        path = reverse('core:genero-editar', kwargs={'pk': self.genero.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = GeneroEditar.as_view()(request, pk=self.genero.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_genero_deletar(self):
        path = reverse('core:genero-deletar', kwargs={'pk': self.genero.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = GeneroDeletar.as_view()(request, pk=self.genero.pk)
        self.assertEqual(response.status_code, 200)


@pytest.mark.django_db
class TestFilmeViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestFilmeViews, cls).setUpClass()
        cls.filme = mixer.blend('core.Filme')
        cls.factory = RequestFactory()
        cls.user = mixer.blend('core.User', email="test@test.com", password="test")
        cls.user.user_permissions.set(Permission.objects.filter(content_type__model='filme', content_type__app_label='core'))
        
    
    def test_filme_lista(self):
        path = reverse('core:filme-listar')
        request = self.factory.get(path)
        request.user = self.user

        response = FilmeListar.as_view()(request)
        self.assertEqual(response.status_code, 200)
        
    
    def test_filme_novo(self):
        path = reverse('core:filme-novo')
        request = self.factory.get(path)
        request.user = self.user

        response = criar_filme(request)
        self.assertEqual(response.status_code, 200)
    
    def test_filme_detalhe(self):
        path = reverse('core:filme-detalhe', kwargs={'pk': self.filme.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = FilmeDetalhe.as_view()(request, pk=self.filme.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_filme_editar(self):
        path = reverse('core:filme-editar', kwargs={'pk': self.filme.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = editar_filme(request, pk=self.filme.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_filme_deletar(self):
        path = reverse('core:filme-deletar', kwargs={'pk': self.filme.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = FilmeDeletar.as_view()(request, pk=self.filme.pk)
        self.assertEqual(response.status_code, 200)

@pytest.mark.django_db
class TestMidiaViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestMidiaViews, cls).setUpClass()
        cls.midia = mixer.blend('core.Midia')
        cls.factory = RequestFactory()
        cls.user = mixer.blend('core.User', email="test@test.com", password="test")
        cls.user.user_permissions.set(Permission.objects.filter(content_type__model='midia', content_type__app_label='core'))
    
    def test_midia_lista(self):
        path = reverse('core:midia-listar')
        request = self.factory.get(path)
        request.user = self.user

        response = MidiaListar.as_view()(request)
        self.assertEqual(response.status_code, 200)
        
    
    def test_midia_novo(self):
        path = reverse('core:midia-novo')
        request = self.factory.get(path)
        request.user = self.user

        response = MidiaCriar.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_midia_detalhe(self):
        path = reverse('core:midia-detalhe', kwargs={'pk': self.midia.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = MidiaDetalhe.as_view()(request, pk=self.midia.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_midia_editar(self):
        path = reverse('core:midia-editar', kwargs={'pk': self.midia.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = MidiaEditar.as_view()(request, pk=self.midia.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_midia_deletar(self):
        path = reverse('core:midia-deletar', kwargs={'pk': self.midia.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = MidiaDeletar.as_view()(request, pk=self.midia.pk)
        self.assertEqual(response.status_code, 200)


@pytest.mark.django_db
class TestArtistaViews(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestArtistaViews, cls).setUpClass()
        cls.artista = mixer.blend('core.Artista')
        cls.user = mixer.blend('core.User', email="test@test.com", password="test")
        cls.user.user_permissions.set(Permission.objects.filter(content_type__model='artista', content_type__app_label='core'))
        cls.factory = RequestFactory()
    
    def test_artista_lista(self):
        path = reverse('core:artista-listar')
        request = self.factory.get(path)
        request.user = self.user

        response = ArtistaListar.as_view()(request)
        self.assertEqual(response.status_code, 200)
        
    
    def test_artista_novo(self):
        path = reverse('core:artista-novo')
        request = self.factory.get(path)
        request.user = self.user

        response = ArtistaCriar.as_view()(request)
        self.assertEqual(response.status_code, 200)
    
    def test_artista_detalhe(self):
        path = reverse('core:artista-detalhe', kwargs={'pk': self.artista.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = ArtistaDetalhe.as_view()(request, pk=self.artista.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_artista_editar(self):
        path = reverse('core:artista-editar', kwargs={'pk': self.artista.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = ArtistaEditar.as_view()(request, pk=self.artista.pk)
        self.assertEqual(response.status_code, 200)
    
    def test_artista_deletar(self):
        path = reverse('core:artista-deletar', kwargs={'pk': self.artista.pk})
        request = self.factory.get(path)
        request.user = self.user

        response = ArtistaDeletar.as_view()(request, pk=self.artista.pk)
        self.assertEqual(response.status_code, 200)