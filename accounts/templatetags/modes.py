from django.template import Library
from ..modes import get_mode, get_all_modes

register = Library()

register.simple_tag(get_mode, name='mode')
register.simple_tag(get_all_modes, name='modes')
