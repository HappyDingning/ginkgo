from django.contrib import admin
from accounts.models import user_profile

@admin.register(user_profile)
class user_profileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email', 
                    'identity', 'duty', 'is_shown')
