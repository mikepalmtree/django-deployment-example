from django import template

register = template.Library()

@register.filter(name='cutfunc')
def cutfunc(value,arg):
    """
    this cuts out all values of arg from the string
    """
    return value.replace(arg,'')

#register.filter('cutfunc',cutfunc)
