Feature: Cadastro de clientes sem sucesso

	Scenario: cadastrar clientes sem preencher campos
		Given estou na tela de cadastro de usuario
		When não preencho nenhum campo
		When clicar em cadastro de usuario
		Then exibira a mensagem "Preencher os campos obrigatórios"


	Scenario: cadastrar clientes apenas com o nome
		Given estou na tela de cadastro de usuario
		When preencho apenas o campo nome
		When clicar em cadastro de usuario
		Then exibira a mensagem "Preencher os campos obrigatórios"
		
		
	Scenario: cadastrar clientes apenas com cpf
		Given estou na tela de cadastro de usuario
		When preencho campo cpf
		When clicar em cadastro de usuario
		Then exibira a mensagem "Preencher os campos obrigatórios"
		
		
	Scenario: cadastrar clientes apenas com email
		Given estou na tela de cadastro de usuario
		When preencho campo email
		When clicar em cadastro de usuario
		Then exibira a mensagem "Preencher os campos obrigatórios"
		
	Scenario: cadastrar clientes apenas com estado	
		Given estou na tela de cadastro de usuario
		When preencho campo estado
		When clicar em cadastro de usuario
		Then exibira a mensagem "Preencher os campos obrigatórios"