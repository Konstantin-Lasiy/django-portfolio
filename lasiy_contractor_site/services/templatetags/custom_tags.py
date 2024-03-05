from django import template
from django.utils import timezone

register = template.Library() 

@register.simple_tag
def current_year():
    return "{0}".format(timezone.now().year)