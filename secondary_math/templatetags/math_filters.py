from django import template

register = template.Library()


@register.filter
def magnitude(val):
    value = float(val)
    if value < 0:
        return f"- {abs(value)}"
    return f"+ {value}"