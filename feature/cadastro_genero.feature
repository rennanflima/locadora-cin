#language:pt

Funcionalidade: Cadastro de gênero
  Cenário: Cadastro de gênero com sucesso
    Dado que estou na página de gênero "https://locadora-cin.herokuapp.com/admin/genero"
    Quando clicar no botão adicionar
    E preencher o campo nome com uma descrição
    E clicar no botão adicionar gênero
    E receber a mensagem de cadastro realizado com sucesso
    E clicar no botão para voltar para listagem
    Então serão listados os gêneros cadastrados

    Cenário: Cancelar cadastro de gênero
        Dado que estou na página de gênero "https://locadora-cin.herokuapp.com/admin/genero"
        Quando clicar no botão adicionar
        E preencher o campo nome com uma descrição
        E clicar no botão cancelar
        Então serão listados os gêneros cadastrados
