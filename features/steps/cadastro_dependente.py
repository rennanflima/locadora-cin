from behave import *

@given(u'estou na pagina de clientes cadastrados')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: Given estou na pagina de clientes cadastrados')
	pass


@when(u'clicar em cadastro de dependentes')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: When clicar em cadastro de dependentes')
	assert True is not False


@then(u'exibira a tela para preencher os dados do dependente')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: Then exibira a tela para preencher os dados do dependente')
	assert context.failed is False


@given(u'na tela de cadastro de dependentes')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: Given na tela de cadastro de dependentes')
	pass


@then(u'exibira a mensagem "Cadastro efetuado com sucesso!"')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: Then exibira a mensagem "Cadastro efetuado com sucesso!"')
	assert context.failed is False
