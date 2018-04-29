# coding: utf-8
from django import template
from decimal import Decimal

register = template.Library()

@register.filter
def igual(value, value2):
    if value and value2:
        lista = value.split(' ')
        for l in lista:
            if value2 == l.upper():
                return True
    return False

@register.filter
def mod(value, div):
    if value % div == 0:
        return True
    return False

@register.filter
def get_photo_gravatar(email, size=100, default="", alt=""):
    # GRAVATAR
    import urllib, hashlib

    # construct the url
    gravatar_url = "http://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d':default, 's':str(size)})

    if gravatar_img:
        return '<img alt="{{ alt }}" src="{0">'.format(gravatar_url)
    else:
        return ''