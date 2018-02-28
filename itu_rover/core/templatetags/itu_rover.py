from django import template

register = template.Library()


@register.filter(name='uppercase')
def uppercase(string):
    """ upper function preserving Turkish 'i' letter """
    string = string.replace('i', '0').upper()
    return string.replace('0', 'İ')
