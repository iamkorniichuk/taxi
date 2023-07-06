from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models import Q, F, ExpressionWrapper

from trips.models import Trip

from commons.models import UserRelatedModel


class ReportManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                is_completed=ExpressionWrapper(
                    Q(complete_datetime__isnull=False),
                    output_field=models.BooleanField(),
                ),
                completition_time=ExpressionWrapper(
                    (F("complete_datetime") - F("report_datetime")),
                    output_field=models.DurationField(),
                ),
            )
        )


class Report(UserRelatedModel):
    trip = models.OneToOneField(Trip, models.CASCADE, related_name="report")
    message = models.TextField(max_length=256)
    report_datetime = models.DateTimeField(auto_now_add=True, editable=False)
    answer = models.TextField(max_length=256, blank=True, default="")
    complete_datetime = models.DateTimeField(null=True)
    manager = models.ForeignKey(
        get_user_model(),
        models.CASCADE,
        null=True,
        blank=True,
        related_name="reports",
        limit_choices_to={"groups__name": "manager"},
    )

    objects = ReportManager()

    class Meta:
        permissions = [("answer_report", "Can answer to any reports of others")]

    def get_absolute_url(self):
        return reverse("reports:detail", kwargs={"pk": self.pk})
