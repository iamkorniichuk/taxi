from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def has_perm(context, perm_codename):
    return context['user'].has_perm(perm_codename)
