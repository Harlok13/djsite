from django import forms
from .models import *

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_lengtx=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    is_published = forms.BooleanField()
    cat = forms.ModelChoiceField(queryset=Category.objects.all)  # будет показывать соответ. список, где мы будем выбирать категорию
