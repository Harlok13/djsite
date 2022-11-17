from django import template
from women.models import Category

register = template.Library()  # регистрация собственных тегов

@register.simple_tag(name='getcats')  # связывание функции с тегом
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)  # возвращение всех записей этой модели в виде коллекций

@register.inclusion_tag('women/tags/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)
    return {'cats': cats, 'cat_selected': cat_selected}

