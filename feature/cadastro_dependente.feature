Feature: Cadastro de dependentes

	Scenario: acesso a cadastro de dependentes
		Given estou na pagina de clientes cadastrados
		When clicar em cadastro de dependentes
		Then exibira a tela para preencher os dados do dependente

	Scenario: cadastro de dependentes
		Given na tela de cadastro de dependentes
		When preencho todos os dados
		Then exibira a mensagem "Cadastro efetuado com sucesso!"

##Cadastro de dependentes sem sucesso

	Scenario: cadastro de dependentes com campo nome
		Given estou na pagina de cadastro de dependentes
		When preencher o campo nome
		When clicar em cadastro de dependentes
		Then exibira a mensagem "Preencha os campos obrigatórios"

	Scenario: cadastro de dependentes com campo email
		Given estou na pagina de cadastro de dependentes
		When preencher o campo email
		When clicar em cadastro de dependentes
		Then exibira a mensagem "Preencha os campos obrigatórios"

	Scenario: cadastro de dependentes com campo data_nascimento
		Given estou na pagina de cadastro de dependentes
		When preencher o campo data de nascimento
		When clicar em cadastro de dependentes
		Then exibira a mensagem "Preencha os campos obrigatórios"
