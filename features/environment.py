from selenium import webdriver
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locadora.settings.behave')

django.setup()
# from core.models import Genero

def before_all(context):
    #
    # context.models = model
    context.browser = webdriver.Firefox()

def after_all(context):
    context.browser.quit()
