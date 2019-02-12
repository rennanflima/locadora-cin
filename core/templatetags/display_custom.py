from django import template
# from django.utils import translation
import locale
from django.utils.formats import localize

locale_set_correctly = False
try:
    locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8") # Unix
    locale_set_correctly = True
except:
    try:
        locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252") # Linux
        locale_set_correctly = True
    except:
        try:
            locale.setlocale(locale.LC_ALL, "") # Tenta usar o locale padrão
            locale_set_correctly = True
        except:
            pass

register = template.Library()

@register.filter(name='currency')
def display_money(value):
    if locale_set_correctly:
        return locale.currency(value, grouping=True)
    else:
        return localize(value)