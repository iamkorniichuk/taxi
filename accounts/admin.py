from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'join_date')
    ordering = ('join_date', )
    fields = ('user', )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('customer', 'join_date')
    ordering = ('join_date', )
    fields = ('customer', )


admin.site.register(MyDirector, EmployeeAdmin)


@admin.register(MyManager)
class ManagerAdmin(EmployeeAdmin):
    fields = ('customer', 'director')


@admin.register(Driver)
class DriverAdmin(EmployeeAdmin):
    list_display = ('customer', 'rating', 'join_date')
    fields = ('customer', 'manager')
