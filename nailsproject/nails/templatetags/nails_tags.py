from django import template
from nails.models import *

register = template.Library()

@register.simple_tag(name='servs')
def get_services():
    return Service.objects.all()

@register.simple_tag()
def get_people_services():
    ms = MasterService.objects.get(Master_id = 'master_id')
    return MasterService.objects.filter()