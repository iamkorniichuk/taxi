from django.db import models
from django.contrib.postgres.fields import ArrayField

from accounts.models import Customer
from cars.models import TypeChoices, ClassChoices

POINT_KWARGS = {
    'max_digits': 9,
    'decimal_places': 6
}

MONEY_KWARGS = {
    'max_digits': 10,
    'decimal_places': 2
}


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='orders')
    start_point = ArrayField(models.DecimalField(**POINT_KWARGS), size=2)
    end_point = ArrayField(models.DecimalField(**POINT_KWARGS), size=2)
    stop_points = ArrayField(models.DecimalField(**POINT_KWARGS), size=3)
    price = models.DecimalField(**MONEY_KWARGS)
    note = models.CharField(max_length=128)
    datetime = models.DateTimeField(auto_now=True)
    car_type = models.CharField(max_length=5, choices=TypeChoices.choices,
                                default=TypeChoices.BASIC)
    car_class = models.CharField(max_length=5, choices=ClassChoices.choices,
                                 default=ClassChoices.BASIC)

    @property
    def is_completed(self):
        ...

    @property
    def wait_time(self):
        ...
