from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'phone', 'full_name', 'image')
    fields = ('phone', 'password', 'first_name', 'last_name', 'image')
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('id', )
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'fields': ('phone', 'password1', 'password2', 'first_name', 'last_name', 'image'),
        }),
    )
