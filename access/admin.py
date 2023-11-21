from django.contrib import admin

from access.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'user_type')

    
admin.site.register(User, UserAdmin)