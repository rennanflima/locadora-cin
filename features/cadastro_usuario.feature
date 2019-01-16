Feature: Cadastro de clientes

	Scenario: acesso a cadastro de clientes
		Given estou na pagina principal
		When clicar em cadastro de usuario
		Then exibira a tela para preencher os dados
	  
	Scenario: cadastrar clientes
		Given na tela de cadastro de clientes
		When preencho todos os dados 
		Then exibira a mensagem "Cadastro efetuado com sucesso"
