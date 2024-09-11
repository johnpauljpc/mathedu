from django import template

register = template.Library()

@register.filter
def magnitude(val):
    value = int(val)
    if value < 0:
        return val
    return f"+ {val}"