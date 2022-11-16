from django.db import models
from django.urls import reverse


class Women(models.Model):  # последовательность полей будет такая же, как мы укажем ее здесь
    """Девушки"""
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)  # 1ый аргумент означает, что поле может быть пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")  # чтобы Джанго имел возможность выполнять операции загрузки
    # в настройках необходимо прописать следующие константы MEDIA_ROOT и MEDIA_URL
    time_create = models.DateTimeField(auto_now_add=True)  # 1ый аргумент будет использоваться один раз при создании записи
    time_update = models.DateTimeField(auto_now=True)  # 1ый аргумент будет использоваться каждый раз при изменении записи
    is_published = models.BooleanField(default=True)  # 1ый аргумент будет отображать опубликована ли запись
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # 1 аргумент в кавычках, потому что модель
    # Category находится ниже модели Women. 3ий аргумент прописывается, потому что поле нужно заполнить, а модель
    # Category еще даже не была создана

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})


class Category(models.Model):
    """Категории"""
    name = models.CharField(max_length=100, db_index=True)  # второй аргумент означает, что поле будет индексируемым,
    # т.е. поиск по нему будет происходить быстрее

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
