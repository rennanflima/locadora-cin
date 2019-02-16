#language:pt

Funcionalidade: Cadastro de gênero
  Cenário: Cadastro de gênero com sucesso
    Dado que estou logado
    E que estou na página de gênero "http://127.0.0.1:8000/admin/genero"
    Quando clicar no botão adicionar
    E preencher o campo nome com uma descrição
    E clicar no botão adicionar gênero
    E receber a mensagem de cadastro realizado com sucesso
    E clicar no botão para voltar para listagem
    Então serão listados os gêneros cadastrados

    Cenário: Cancelar cadastro de gênero
        Dado que estou na página de gênero "http://127.0.0.1:8000/admin/genero"
        Quando clicar no botão adicionar
        E preencher o campo nome com uma descrição
        E clicar no botão cancelar
        Então serão listados os gêneros cadastrados
