from django.contrib import admin
from propaganda.models import achievement

@admin.register(achievement)
class achievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'level')
