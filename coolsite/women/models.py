from django.db import models
from django.urls import reverse


class Women(models.Model):  # последовательность полей будет такая же, как мы укажем ее здесь
    """Девушки"""
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')  # 1ый аргумент означает, что поле может быть пустым
    photo = models.ImageField(upload_to="photos/%Y/%m/%d", verbose_name='Фото')  # чтобы Джанго имел возможность выполнять операции загрузки в настройках необходимо прописать следующие константы MEDIA_ROOT и MEDIA_URL
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')  # 1ый аргумент будет использоваться один раз при создании записи
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')  # 1ый аргумент будет использоваться каждый раз при изменении записи
    is_published = models.BooleanField(default=True, verbose_name='Публикация')  # 1ый аргумент будет отображать опубликована ли запись
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Каталог')  # 1 аргумент в кавычках, потому что модель Category находится ниже модели Women.


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['time_create', 'title']  # сортировка (на сайте не сортируется)


class Category(models.Model):
    """Категории"""
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')  # второй аргумент означает, что поле будет индексируемым, т.е. поиск по нему будет происходить быстрее
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']  # сортировка по айди
