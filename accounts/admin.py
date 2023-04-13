from django.contrib import admin
from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'join_date')
    ordering = ('join_date', )
    fields = ('user', )


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'join_date')
    ordering = ('join_date', )
    fields = ('user', 'job_title')


admin.site.register(MyDirector, EmployeeAdmin)


@admin.register(MyManager)
class ManagerAdmin(EmployeeAdmin):
    fields = ('user', 'director', 'job_title')


@admin.register(Driver)
class DriverAdmin(EmployeeAdmin):
    list_display = ('user', 'rating', 'join_date', 'job_title')
    fields = ('user', 'manager', 'job_title')
