from django.template.defaultfilters import register



@register.filter(name='sum')
def sum(list):
    return sum(list)