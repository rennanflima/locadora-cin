from nose.tools import assert_equal, assert_true
from behave import Given, When, Then
from core.models import Genero

# Cadastro de generos
@given('Eu navego ate a pagina de cadastro de genero')
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000/admin/genero/novo/")

@when('Eu preencho o nome do genero')
def step_impl(context):
    context.browser.find_element_by_id("id_nome").send_keys("Terror")

@then('Eu clico no botao salvar e recebo a msg "{msg}"')
def step_impl(context, msg):    
    if Genero.objects.filter(nome="Terror").exists():
        context.browser.find_element_by_id("id_submit").click()
        assert_true(context.browser.find_element_by_class_name("alert-danger"), 'Gênero com este Nome já existe.')
    else:
        context.browser.find_element_by_id("id_submit").click()
        assert_true(context.browser.find_element_by_class_name("alert-success"), "Gênero adicionado com sucesso.")
