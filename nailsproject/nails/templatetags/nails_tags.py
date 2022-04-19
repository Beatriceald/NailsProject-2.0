from django import template
from nails.models import *

register = template.Library()

@register.simple_tag()
def get_services():
    return Service.objects.all()