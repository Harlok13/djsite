from django.contrib import admin
from women.models import Women, Category


# class WomenAdmin(admin.ModelAdmin):



admin.site.register(Women)
admin.site.register(Category)
