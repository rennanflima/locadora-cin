from django.urls import reverse, resolve

class TestUrls:
    
    # Início CRUD Gênero
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
    # Termino CRUD Gênero

    # Início CRUD Filme
    def test_filme_listar(self):
        path = reverse('core:filme-listar')
        assert resolve(path).view_name == 'core:filme-listar'

    def test_filme_novo(self):
        path = reverse('core:filme-novo')
        assert resolve(path).view_name == 'core:filme-novo'

    def test_filme_editar(self):
        path = reverse('core:filme-editar', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'core:filme-editar'

    def test_filme_detalhe(self):
        path = reverse('core:filme-detalhe', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'core:filme-detalhe'

    def test_filme_deletar(self):
        path = reverse('core:filme-deletar', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'core:filme-deletar'
    
    # Termino CRUD Filme