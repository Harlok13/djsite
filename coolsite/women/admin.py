from django.contrib import admin
from women.models import Women, Category


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'photo', 'is_published')  # отображает поля, которые мы хотим увидеть
    list_display_links = ('id', 'title')  # поля, на которые мы можем кликнуть и перейти на соответствующую статью для
    # ее редактирования
    search_fields = ('title', 'content')  # по каким полям можно производить поиск
    list_editable = ('is_published',)  # создает редактируемое поле в админке
    list_filter = ('is_published', 'time_create')  # позволяет сортировать записи по этим полям в админке


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)  # обязательна запятая, потому что это кортеж


admin.site.register(Women, WomenAdmin)
admin.site.register(Category, CategoryAdmin)
