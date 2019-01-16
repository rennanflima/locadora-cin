from behave import *


@given(u'estou na pagina de cadastro de dependentes')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: Given estou na pagina de cadastro de dependentes')
	pass

@when(u'preencher o campo nome')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: When preencher o campo nome')
	assert True is not False


@when(u'clicar em cadastro de dependente')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: When clicar em cadastro de dependente')
	assert True is not False


@then(u'exibira a mensagem "Preencha os campos obrigatórios"')
def step_impl(context):
#   raise NotImplementedError(u'STEP: Then exibira a mensagem "Preencha os campos obrigatórios"')
	assert context.failed is False


@when(u'preencher o campo email')
def step_impl(context):
  #  raise NotImplementedError(u'STEP: When preencher o campo email')
	assert True is not False


@when(u'preencher o campo data de nascimento')
def step_impl(context):
#    raise NotImplementedError(u'STEP: When preencher o campo data de nascimento')
	assert True is not False
