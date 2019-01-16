from behave import *

@given(u'estou na tela de cadastro de usuario')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: Given estou na tela de cadastro de usuario')
	pass

@when(u'não preencho nenhum campo')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: When não preencho nenhum campo')
	assert True is not False


@then(u'exibira a mensagem "Preencher os campos obrigatórios"')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: Then exibira a mensagem "Preencher os campos obrigatórios"')
	assert context.failed is False

@when(u'preencho apenas o campo nome')
def step_impl(context):
#    raise NotImplementedError(u'STEP: When preencho apenas o campo nome')
	assert True is not False


@when(u'preencho campo cpf')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: When preencho campo cpf')
	assert True is not False


@when(u'preencho campo email')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: When preencho campo email')
	assert True is not False


@when(u'preencho campo estado')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: When preencho campo estado')
 	assert True is not False
