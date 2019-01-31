from django import template
import locale

locale.setlocale(locale.LC_ALL, '')

register = template.Library()

@register.filter(name='currency')
def display_money(value):
    return locale.currency(value)