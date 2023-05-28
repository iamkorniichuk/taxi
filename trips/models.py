from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from commons.fields import MoneyField
from orders.models import Order


class Trip(models.Model):
    order = models.OneToOneField(Order, models.CASCADE, related_name='trip')
    driver = models.ForeignKey(get_user_model(), models.CASCADE, related_name='trips')
    start_datetime = models.DateTimeField(auto_now=True)
    end_datetime = models.DateTimeField(null=True)
    rating = models.PositiveSmallIntegerField(null=True, validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    tip = MoneyField(null=True)

    @property
    def is_completed(self):
        return self.end_datetime != None

    @property
    def wait_time(self):
        if self.is_completed:
            return self.start_datetime - self.order.datetime
        return False

    @property
    def duration(self):
        if self.is_completed:
            return self.end_datetime - self.start_datetime
        return False

    def __str__(self) -> str:
        return self.order.__str__()
