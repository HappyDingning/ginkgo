from django.contrib import admin
from news.models import news, tag


@admin.register(news)
class newsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'source')

@admin.register(tag)
class tagAdmin(admin.ModelAdmin):
    list_display = ('label',)
