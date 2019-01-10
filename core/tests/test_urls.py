from django.urls import reverse, resolve

class TestUrls:

    def test_genero_listar(self):
        path = reverse('core:genero-listar')
        assert resolve(path).view_name == 'core:genero-listar'

    def test_genero_novo(self):
        path = reverse('core:genero-novo')
        assert resolve(path).view_name == 'core:genero-novo'

    def test_genero_editar(self):
        path = reverse('core:genero-edita', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'core:genero-edita'

    def test_genero_detalhe(self):
        path = reverse('core:genero-detalhe', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'core:genero-detalhe'

    def test_genero_deletar(self):
        path = reverse('core:genero-deletar', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'core:genero-deletar'