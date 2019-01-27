Feature: Cadastro de Generos

	Scenario: acesso a cadastro de generos
		Given estou na pagina principal
		When clicar em cadastro de generos
		Then exibira a tela para preencher os dados

	Scenario: cadastrar genero
		Given a tela de cadastro de generos
		When preencho todos os dados
		Then exibira a mensagem "Cadastro efetuado com sucesso"
