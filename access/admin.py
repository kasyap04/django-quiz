from django.contrib import admin

from access.models import User, Setting

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'user_type')

class SettingAdmin(admin.ModelAdmin):
    list_display = ('id', 'max_questions', 'mark_per_questions', 'time_per_questions')
    list_editable = ('max_questions', 'mark_per_questions', 'time_per_questions')

    
admin.site.register(User, UserAdmin)
admin.site.register(Setting, SettingAdmin)