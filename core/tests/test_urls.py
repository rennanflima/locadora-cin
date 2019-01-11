from django.urls import reverse, resolve

class TestUrls:
    
    # Início CRUD Gênero
    def test_genero_listar(self):
        path = reverse('admin:genero-listar')
        assert resolve(path).view_name == 'admin:genero-listar'

    def test_genero_novo(self):
        path = reverse('admin:genero-novo')
        assert resolve(path).view_name == 'admin:genero-novo'

    def test_genero_editar(self):
        path = reverse('admin:genero-edita', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'admin:genero-edita'

    def test_genero_detalhe(self):
        path = reverse('admin:genero-detalhe', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'admin:genero-detalhe'

    def test_genero_deletar(self):
        path = reverse('admin:genero-deletar', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'admin:genero-deletar'
    # Termino CRUD Gênero

    # Início CRUD Filme
    def test_filme_listar(self):
        path = reverse('admin:filme-listar')
        assert resolve(path).view_name == 'admin:filme-listar'

    def test_filme_novo(self):
        path = reverse('admin:filme-novo')
        assert resolve(path).view_name == 'admin:filme-novo'

    def test_filme_editar(self):
        path = reverse('admin:filme-editar', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'admin:filme-editar'

    def test_filme_detalhe(self):
        path = reverse('admin:filme-detalhe', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'admin:filme-detalhe'

    def test_filme_deletar(self):
        path = reverse('admin:filme-deletar', kwargs={'pk' : 1})
        assert resolve(path).view_name == 'admin:filme-deletar'
    
    # Termino CRUD Filme