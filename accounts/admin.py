from django.contrib import admin

from .models import *


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'group')
    fields = list_display
    search_fields = list_display
    ordering = ('group', )
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'fields': list_display,
        }),
    )
