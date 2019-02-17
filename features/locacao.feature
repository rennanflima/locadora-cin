#language:pt

Funcionalidade: Nova locação
  Cenário: Cadastro de nova locação
    Dado que estou na página de listagem de locações "http://127.0.0.1:8000/admin/locacao/"
    Quando clicar no botão Realizar Locação
    E selecionar o cliente da locação
    E clicar no botão Próximo
    E clicar no botão Adicionar Item
    E selecionar um item
    E clicar em Adicionar Item     
    Então clicar no botão Próximo
    E clicar no botão Concluir
    E Locação concluída com sucesso.
