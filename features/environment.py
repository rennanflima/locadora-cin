from selenium import webdriver
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'locadora.settings.development')

django.setup()

def before_all(context):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    context.browser = webdriver.Chrome("/usr/local/share/chromedriver", chrome_options=chrome_options)
    context.browser.maximize_window()
    context.browser.implicitly_wait(20)

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
