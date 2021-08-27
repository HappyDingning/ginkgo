from django.contrib import admin
from notice.models import notice


@admin.register(notice)
class noticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')