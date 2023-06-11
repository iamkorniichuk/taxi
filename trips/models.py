from django.db import models
from django.db.models import Q, F, ExpressionWrapper, Exists, OuterRef
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

from commons.models import MoneyField, UserRelatedModel
from orders.models import Order

from .apps import APP_NAME


class TripManager(models.Manager):
    def get_queryset(self):
        from reports.models import Report

        return super().get_queryset().annotate(
            is_completed=ExpressionWrapper(
                Q(complete_datetime__isnull=False),
                output_field=models.BooleanField()
            ),
            has_report=ExpressionWrapper(
                ~Exists(
                    Report.objects.filter(trip=OuterRef('pk'))
                ), output_field=models.BooleanField()
            ),
            wait_time=ExpressionWrapper(
                (F('start_datetime') - F('order__datetime')),
                output_field=models.DurationField()
            ),
            duration=ExpressionWrapper(
                (F('complete_datetime') - F('start_datetime')),
                output_field=models.DurationField()
            )
        )


class Trip(UserRelatedModel):
    order = models.OneToOneField(Order, models.CASCADE, related_name='trip')
    driver = models.ForeignKey(get_user_model(), models.CASCADE, related_name='trips',
                               limit_choices_to={'groups__name': 'driver'})
    start_datetime = models.DateTimeField(auto_now_add=True)
    complete_datetime = models.DateTimeField(null=True)
    rating = models.PositiveSmallIntegerField(null=True, validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    tip = MoneyField(null=True)

    objects = TripManager()

    def get_absolute_url(self):
        return reverse(APP_NAME + ':detail', kwargs={"pk": self.pk})
