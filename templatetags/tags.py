from django import template
register = template.Library()
@register.inclusion_tag('partials/_sidebar.html')
def show_categories():
    categories = "Rayhan"
    return {'categories': categories}
