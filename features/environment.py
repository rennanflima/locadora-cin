from selenium import webdriver
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locadora.settings.behave')

django.setup()

def before_all(context):
    # context.browser = webdriver.Chrome("/usr/local/share/chromedriver")
    context.browser = webdriver.Chrome("/usr/local/share/chromedriver")

def after_all(context):
    context.browser.quit()

# def before_all(context):
#     desired_caps = {
#         'platform': 'LINUX',
#         'browserName': 'chrome',
#         'name': 'teste-comportamento',
#         'client_key': '331d36f347d47c98951b34a15b6cd310',
#         'client_secret': '040b3f266b76496698d912fa4df587ca'
#     }
#     context.browser = webdriver.Remote(
#       command_executor='http://locahost:8000/wd/hub',
#       desired_capabilities=desired_caps
#     )
#
# def after_all(context):
#     context.browser.quit()
