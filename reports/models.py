from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from trips.models import Trip

from commons.models import UserRelatedModel

from .apps import APP_NAME


class Report(UserRelatedModel):
    trip = models.ForeignKey(Trip, models.CASCADE, related_name='reports')
    message = models.TextField(max_length=256)
    report_datetime = models.DateTimeField(auto_now=True, editable=False)
    answer = models.TextField(max_length=256, blank=True, default='')
    complete_datetime = models.DateTimeField(null=True)
    manager = models.ForeignKey(get_user_model(), models.CASCADE, null=True, blank=True,
                                related_name='reports', limit_choices_to={'groups__name': 'manager'})

    class Meta:
        permissions = [
            ('answer_report', 'Can answer to any reports of others')
        ]

    def get_absolute_url(self):
        return reverse(APP_NAME + ':detail', kwargs={'pk': self.pk})

    @property
    def is_completed(self):
        return self.complete_datetime != None

    @property
    def completition_time(self):
        if self.is_completed:
            return self.complete_datetime - self.report_datetime
        return False
