from django.contrib import admin

from .models import *


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('order', 'driver', 'duration', 'rating', 'tip', 'is_completed')
    fields = ('order', 'driver', 'end_datetime', 'rating', 'tip')
    search_fields = ('driver', 'rating')
