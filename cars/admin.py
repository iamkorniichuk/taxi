from django.contrib import admin

from .models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("number", "full_name", "year", "type", "_class")
    fields = ("driver", "number", "brand", "model", "color", "year", "type", "_class")
    search_fields = ("driver", "number")
    list_filter = (
        ("type", admin.ChoicesFieldListFilter),
        ("_class", admin.ChoicesFieldListFilter),
    )
