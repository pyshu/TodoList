# __author__ = 'lius'

from django import template
from  django.template.defaultfilters import stringfilter
from  django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def time_filter(value,arg):
    print(arg)
    value += " -- 1天前发布"
    return value
