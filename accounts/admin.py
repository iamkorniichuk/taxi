from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'join_date')
    ordering = ('join_date', )
    fields = ('user', )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('customer', 'join_date')
    ordering = ('join_date', )
    fields = ('customer', )


admin.site.register(MyDirector, EmployeeAdmin)
admin.site.register(MyManager, EmployeeAdmin)


@admin.register(Driver)
class DriverAdmin(EmployeeAdmin):
    list_display = ('customer', 'rating', 'join_date')
