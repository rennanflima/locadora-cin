Feature: Cadastro de Generos

	Scenario: acesso a cadastro de generos
		Given estou na pagina principal
		When clicar em cadastro de generos
		Then exibira a tela para preencher os dados do cadastro do genero

	Scenario: cadastrar genero
		Given a tela de cadastro de generos
		When preencho todos os dados de genero
		Then exibira a mensagem "Genero adicionado com sucesso"
