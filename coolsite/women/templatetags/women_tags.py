from django import template
from women.models import Category

register = template.Library()  # регистрация собственных тегов

@register.simple_tag()  # связывание функции с тегом
def get_categories():
    return Category.objects.all()  # возвращение всех записей этой модели

