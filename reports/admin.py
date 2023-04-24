from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('trip', 'report_datetime', 'is_open', 'is_completed')
    fields = ('trip', 'message', 'manager')
