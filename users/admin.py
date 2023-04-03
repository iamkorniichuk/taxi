from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('id', 'phone', 'full_name', 'image', 'is_staff')
    fields = ('phone', 'password', 'first_name', 'last_name', 'image')
    search_fields = ('phone', 'first_name', 'last_name')
    list_filter = (('is_staff', admin.BooleanFieldListFilter), )
    ordering = ('id', )
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'fields': ('phone', 'password1', 'password2', 'first_name', 'last_name', 'image'),
        }),
    )
