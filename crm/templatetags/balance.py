import datetime
from django import template

register = template.Library()



@register.simple_tag
def get_balance():
    pass