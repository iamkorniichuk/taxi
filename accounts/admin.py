from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'join_date')
    ordering = ('join_date', )
    fields = ('user', )
