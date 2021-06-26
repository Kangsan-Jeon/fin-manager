from django import template

register = template.Library()

@register.simple_tag
def get_earning(current_price, purchase_price, num_of_stock):
    return (current_price - purchase_price)*num_of_stock

@register.simple_tag
def get_earning_rate(current_price, purchase_price):
    return current_price/purchase_price - 1