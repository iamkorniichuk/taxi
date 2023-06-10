from django.contrib import admin
from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('trip', 'report_datetime', 'manager', 'is_completed')
    fields = ('trip', 'message', 'answer', 'manager')
    fieldsets = ()
    add_fieldsets = (
        (None, {
            'fields': ('trip', 'message', 'manager'),
        }),
    )
