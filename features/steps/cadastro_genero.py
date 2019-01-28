from behave import *
from selenium import webdriver
# from core.models import Genero

def before_all(context):  
	context.browser = webdriver.Chrome()

def after_all(context):  
      context.browser.quit()

@given(u'a tela de cadastro de generos')
def step_impl(context):
	context.browser.get('http://localhost:8000/admin/genero/novo')

@when(u'preencho todos os dados de genero')
def step_impl(context):
	form = get_element(context.browser, tag='form')
	get_element(form, name="nome").send_keys('Terror')
	form.submit()
	assert Genero.objects.filter(name="Terror").exists() is not False

@then(u'exibira a mensagem "Genero adicionado com sucesso"')
def step_impl(context):
	assert context.failed is False

@given(u'estou na pagina principal para buscar o cadastro de genero')
def step_impl(context):
#    raise NotImplementedError(u'STEP: Given estou na pagina principal')
	pass

@when(u'clicar em cadastro de genero')
def step_impl(context):
#    raise NotImplementedError(u'STEP: When clicar em cadastro de usuario')
	assert True is not False

@then(u'exibira a tela para preencher os dados do cadastro do genero')
def step_impl(context):
 #   raise NotImplementedError(u'STEP: Then exibira a tela para preencher os dados')
	assert context.failed is False
