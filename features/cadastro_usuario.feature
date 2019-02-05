Feature: Cadastro de clientes

	Scenario: cadastrar clientes com sucesso
		Given estou na tela de cadastro de usuário
		When preencho todos os dados
		Then exibira a mensagem "Cadastro efetuado com sucesso"

	Scenario: cadastrar clientes sem preencher campos
				Given estou na tela de cadastro de usuário
				When não preencho nenhum campo
				When clicar em cadastro de usuário
				Then exibira a mensagem "Preencher os campos obrigatórios"


	Scenario: cadastrar clientes apenas com o nome
				Given estou na tela de cadastro de usuário
				When preencho apenas o campo nome
				When clicar em cadastro de usuário
				Then exibira a mensagem "Preencher os campos obrigatórios"


	Scenario: cadastrar clientes apenas com cpf
				Given estou na tela de cadastro de usuário
				When preencho campo cpf
				When clicar em cadastro de usuário
				Then exibira a mensagem "Preencher os campos obrigatórios"


	Scenario: cadastrar clientes apenas com e-mail
				Given estou na tela de cadastro de usuário
				When preencho campo e-mail
				When clicar em cadastro de usuário
				Then exibira a mensagem "Preencher os campos obrigatórios"

	Scenario: cadastrar clientes apenas com estado
				Given estou na tela de cadastro de usuário
				When preencho campo estado
				When clicar em cadastro de usuário
				Then exibira a mensagem "Preencher os campos obrigatórios"
