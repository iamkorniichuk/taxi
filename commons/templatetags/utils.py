from django import template

register = template.Library()


@register.filter()
def delta(delta, format: str):
    d = {"d": delta.days}
    d["H"], rem = divmod(delta.seconds, 3600)
    d["m"], d["s"] = divmod(rem, 60)
    return format.format(**d)


@register.simple_tag()
def format(format: str, **vars):
    return format.format(**vars)
