from django.contrib import admin
from article.models import article, tag


@admin.register(article)
class articleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'source')

@admin.register(tag)
class tagAdmin(admin.ModelAdmin):
    list_display = ('label',)
