from django.contrib import admin

from .models import *

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('start_point', 'end_point', 'price', 'note', 'datetime', 'car_type', 'car_class', 'is_completed', 'wait_time')
    fields = ('customer', 'start_point', 'end_point', 'price', 'note', 'datetime', 'car_type', 'car_class')
    search_fields = ('price', 'car_type', 'car_class')
    list_filter = (('car_type', admin.ChoicesFieldListFilter), ('car_class', admin.ChoicesFieldListFilter))
    
