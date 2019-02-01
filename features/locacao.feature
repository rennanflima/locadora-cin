#Feature: Realizando locação
#  description
#  Comportamento para realizacao de uma nova locaçao

#  Scenario: Informar CPF Inválido para um Cliente
#    Given Eu navego até a página de edição da locação
#    When Eu preencho o cpf que nao pertence a nenhum cliente
#    Then Eu recebo a msg de "Cliente não encontrado."
#      And clico em buscar cliente


#  Scenario: Adicionar Item a Locação
#    Given Eu navego até a página de edição da locação
#    When Eu clico em adicionar item
#      And informo o codigo de barras
#      And clico em salvar item
#    Then Eu recebo a msg "Item adicionado com sucesso"

#  Scenario: Excluir Item da Locação
#    Given Eu navego até a página de edição da locação
#    When Eu clico no botão excluir ao lado do item que quero excluir
#    Then Eu sou questionado "Tem certeza que deseja remover este Item?"
#    When Clico em "Sim"
#    Then Eu recebo a msg "Item Excluido com Sucesso."


#  Scenario: Finalizar Locação
#    Given Eu navego até a página de edição da locação
#    When Eu clico no botão Salvar
#    Then Eu recebo a msg "Locação Salva com Sucesso!"
