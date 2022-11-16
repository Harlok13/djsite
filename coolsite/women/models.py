from django.db import models
from django.urls import reverse


class Women(models.Model):  # последовательность полей будет такая же как мы укажем ее здесь
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d")  # чтобы джанго имел возможность выполнять операции загрузки в насстройках
    # необходимо прописать следующие константы MEDIA ROOT и MEDIA_URL
    time_create = models.DateTimeField(auto_now_add=True)  # 1ый аргумент будет использоваться один раз при создании записи
    time_update = models.DateTimeField(auto_now=True)  # 1ый аргумент будет использоваться каждый раз при изменении записи
    is_published = models.BooleanField(default=True )  # 1ый аргумент будет отображать опубликована ли запись

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
