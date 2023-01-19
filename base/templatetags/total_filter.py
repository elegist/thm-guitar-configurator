from django import template

register = template.Library()

@register.filter()
def total(value):
    totalPrice = 0
    valueIndex = range(len(value))
    for index in valueIndex:
        totalPrice += value[index].item.price
    return totalPrice