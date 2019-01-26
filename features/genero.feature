Feature: Manipulacao de Genero
  description
  Comportamento para insercao e edicao de genero

Scenario: Cadastro de Genero
    Given Eu navego ate a pagina de cadastro de genero
    When Eu preencho o nome do genero
    Then Eu clico no botao salvar e recebo a msg "msg"
