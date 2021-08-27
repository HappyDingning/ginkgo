from django.contrib import admin
from basic.models import carousel


@admin.register(carousel)
class newsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'content_class', 'place')
