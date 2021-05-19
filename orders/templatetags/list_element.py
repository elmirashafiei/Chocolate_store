from django import template


register = template.Library()

@register.simple_tag
def list_element(my_list, elm):
    return my_list[elm]
