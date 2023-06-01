from django import template

from math import floor

register = template.Library()

# TODO: To refactor / use include tag
@register.simple_tag()
def stars(rating: float):
    MAX_RATING = 5

    result = []
    int_part = floor(rating)
    filled_stars = 0
    for i in range(int_part):
        result.append('<i class="bi bi-star-fill"></i>')
        filled_stars += 1

    float_part = rating - int_part
    if float_part >= 0.5:
        result.append('<i class="bi bi-star-half"></i>')
        filled_stars += 1

    for j in range(MAX_RATING - filled_stars):
        result.append('<i class="bi bi-star"></i>')
    return result
