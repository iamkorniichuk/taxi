from django.contrib import admin

from .models import *


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('order', 'driver', 'rating', 'tip')
    fields = ('order', 'driver', 'complete_datetime', 'rating', 'tip')
    search_fields = ('driver', 'rating')
