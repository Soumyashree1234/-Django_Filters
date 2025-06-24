from django import template
register=template.Library()
def swapping(value):
    return value.swapcase()
register.filter('swap',swapping)

@register.filter()
def split(value,deli):
    return value.split(deli)