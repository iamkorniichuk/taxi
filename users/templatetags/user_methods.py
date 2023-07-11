from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def has_perm(context, perm):
    return context["user"].has_perm(perm)
