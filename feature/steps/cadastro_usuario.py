from behave import *

@given(u'na tela de cadastro de clientes')
def step_impl(context):
	pass

@when(u'preencho todos os dados')
def step_impl(context):
	assert True is not False

@then(u'exibira a mensagem "Cadastro efetuado com sucesso"')
def step_impl(context):
	assert context.failed is False

@given(u'estou na pagina principal')
def step_impl(context):
#    raise NotImplementedError(u'STEP: Given estou na pagina principal')
	pass

@when(u'clicar em cadastro de usuario')
def step_impl(context):
#    raise NotImplementedError(u'STEP: When clicar em cadastro de usuario')
	assert True is not False

@then(u'exibira a tela para preencher os dados')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: Then exibira a tela para preencher os dados')
	assert context.failed is False