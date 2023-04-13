from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from orders.models import Order, MONEY_KWARGS
from accounts.models import Driver


class Trip(models.Model):
    order = models.OneToOneField(Order, models.CASCADE, related_name='trip')
    driver = models.ForeignKey(Driver, models.CASCADE, related_name='trips')
    start_datetime = models.DateTimeField(auto_now=True)
    end_datetime = models.DateTimeField(null=True)
    rating = models.PositiveSmallIntegerField(null=True, validators=[
        MinValueValidator(1), MaxValueValidator(5)
    ])
    tip = models.DecimalField(null=True, **MONEY_KWARGS)

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
