from django import template
from women.models import Category

register = template.Library()  # регистрация собственных тегов

@register.simple_tag(name='getcats')  # связывание функции с тегом
def get_categories():
    return Category.objects.all()  # возвращение всех записей этой модели в виде коллекций

@register.inclusion_tag('women/tags/list_categories.html')
def show_categories():
    cats = Category.objects.all()
    return {'cats': cats}

