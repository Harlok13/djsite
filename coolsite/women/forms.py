from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    slug = forms.SlugField(max_length=255, label='URL')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Контент')
    is_published = forms.BooleanField(label='Публикация', required=False, initial=True)  # required (обязательное поле), initial=True по-умолчанию делает поле отмеченным
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории', empty_label='Категория не выбрана')  # будет показывать соответ. список, где мы будем выбирать категорию
