from nose.tools import assert_equal, assert_true
from behave import Given, When, Then
from core.models import Genero
from datetime import datetime

# Cadastro de generos
@given('Eu navego até a página de cadastro de gênero')
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000/admin/genero/novo/")

@when('Eu preencho o nome do gênero')
def step_impl(context):
    elem = context.browser.find_element_by_id("id_nome")
    nome_genero = "Outro".format(datetime.now())
    elem.send_keys(nome_genero)

@then('Eu clico no botão salvar')
def step_impl(context):
    context.browser.find_element_by_id("id_submit").click()

@then('Eu sou redirecionado para a tela de detalhes')
def step_impl(context):
    assert_true(context.browser.find_element_by_tag_name("h2"), "Detalhar Gênero")

@then('recebo a msg "Gênero adicionado com sucesso."')
def step_impl(context):
    assert_true(context.browser.find_element_by_class_name("alert-success"), "Gênero adicionado com sucesso.")


# Exclusão de gêneros

@given(u'Eu navego até a página de listagem de gêneros')
def step_impl(context):
    context.browser.get("http://127.0.0.1:8000/admin/genero/")


@when(u'Eu clico no botão excluir')
def step_impl(context):
    context.browser.find_element_by_class_name("btn-danger").click()


@then(u'Eu sou perguntado "Você tem certeza que quer apagar o Gênero ?"')
def step_impl(context):
    conteudo = context.browser.find_element_by_id("pergunta_delete").text
    if "Você tem certeza que quer apagar o Gênero" in conteudo:
        assert True is not False
    else:
        assert True is not True

@then(u'clico em Sim, tenho certeza')
def step_impl(context):
    context.browser.find_element_by_id("btn_confirm_delete").click()

@then(u'Recebo a msg "Gênero excluído com sucesso."')
def step_impl(context):
    assert_true(context.browser.find_element_by_class_name("alert-success"), "Gênero excluído com sucesso.")
