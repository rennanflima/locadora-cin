Feature: Cadastro de dependentes sem sucesso

	Scenario: cadastro de dependentes com campo nome
		Given estou na pagina de cadastro de dependentes
		When preencher o campo nome
		When clicar em cadastro de dependente 
		Then exibira a mensagem "Preencha os campos obrigatórios"
	  
	Scenario: cadastro de dependentes com campo email
		Given estou na pagina de cadastro de dependentes
		When preencher o campo email
		When clicar em cadastro de dependente 
		Then exibira a mensagem "Preencha os campos obrigatórios"

	Scenario: cadastro de dependentes com campo data_nascimento
		Given estou na pagina de cadastro de dependentes
		When preencher o campo data de nascimento
		When clicar em cadastro de dependente 
		Then exibira a mensagem "Preencha os campos obrigatórios"