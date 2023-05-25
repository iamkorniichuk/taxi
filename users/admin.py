from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
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

    def save_model(self, request, obj, form, change):
        get_user_model().objects.create_user(**form.cleaned_data)
