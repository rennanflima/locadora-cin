Feature: Manipulacao de Gênero
  description
  Comportamento para inserção e edicao de Gênero

  Scenario: Cadastro de Gênero
    Given Eu navego até a página de cadastro de gênero
    When Eu preencho o nome do gênero
    Then Eu clico no botão salvar
      And Eu sou redirecionado para a tela de detalhes
      And recebo a msg "Gênero adicionado com sucesso."


  Scenario: Excluir Gênero
    Given Eu navego até a página de listagem de gêneros
    When Eu clico no botão excluir
    Then Eu sou perguntado "Você tem certeza que quer apagar o Gênero ?"
      And clico em Sim, tenho certeza
      And Recebo a msg "Gênero excluído com sucesso."
