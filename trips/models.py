from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

from commons.models import MoneyField, UserRelatedModel
from orders.models import Order

from .apps import APP_NAME


class Trip(UserRelatedModel):
    order = models.OneToOneField(Order, models.CASCADE, related_name='trip')
    driver = models.ForeignKey(get_user_model(), models.CASCADE, related_name='trips',
                               limit_choices_to={'groups__name': 'driver'})
    start_datetime = models.DateTimeField(auto_now=True)
    complete_datetime = models.DateTimeField(null=True)
    rating = models.PositiveSmallIntegerField(null=True, validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    tip = MoneyField(null=True)

    @property
    def is_completed(self):
        return self.complete_datetime != None

    @property
    def wait_time(self):
        if self.is_completed:
            return self.start_datetime - self.order.datetime

    @property
    def duration(self):
        if self.is_completed:
            return self.complete_datetime - self.start_datetime
        return False

    def get_absolute_url(self):
        return reverse(APP_NAME + ':detail', kwargs={"pk": self.pk})

    def __str__(self) -> str:
        return self.order.__str__()
