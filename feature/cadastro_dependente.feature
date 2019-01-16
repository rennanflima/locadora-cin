Feature: Cadastro de dependentes

	Scenario: acesso a cadastro de dependentes
		Given estou na pagina de clientes cadastrados
		When clicar em cadastro de dependentes
		Then exibira a tela para preencher os dados do dependente
	  
	Scenario: cadastro de dependentes
		Given na tela de cadastro de dependentes
		When preencho todos os dados 
		Then exibira a mensagem "Cadastro efetuado com sucesso!"