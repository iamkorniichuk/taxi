from django.contrib import admin

from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk', 'stops', 'price', 'note', 'datetime',
                    'car_type', 'car_class', 'distance')
    fields = ('customer', '_stops', 'price', 'note', 'car_type', 'car_class')
    search_fields = ('price', 'car_type', 'car_class')
    list_filter = (('car_type', admin.ChoicesFieldListFilter),
                   ('car_class', admin.ChoicesFieldListFilter))
