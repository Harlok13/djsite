from django import forms
from django.core.exceptions import ValidationError

from .models import *

# class AddPostForm(forms.Form):
#     title = forms.CharField(max_length=255, label='Заголовок')
#     slug = forms.SlugField(max_length=255, label='URL')
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}), label='Контент')
#     is_published = forms.BooleanField(label='Публикация', required=False, initial=True)  # required (обязательное поле), initial=True по-умолчанию делает поле отмеченным
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории', empty_label='Категория не выбрана')  # будет показывать соответ. список, где мы будем выбирать категорию
# поля с датами здесь не указываются, потому что они сами создаются при создании записи в бд

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  # вызывает конструктор
        super().__init__(*args, **kwargs)  # вызывает конструктор базового класса, после него появится поле
        self.fields['cat'].empty_label = 'Категория не выбрана'  # меняет поле cat

    class Meta:
        model = Women  # делает связь этой формы с моделью
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']  # какие поля нужно отобразить в форме
        widgets = {
           'title': forms.TextInput(attrs={'class': 'form-input'}),
           'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
        # ('__all__' отобразит все поля, кроме тех, что указываются автоматически)

    def clean_title(self):
        title = self.cleaned_data['title']  # получаем данные по заголовку из коллекции cleaned_data, которая доступна в экземпляре класса AddPostForm
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')
        return title
