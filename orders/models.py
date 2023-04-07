from django.db import models

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
    start_lat = models.DecimalField(**POINT_KWARGS)
    start_lon = models.DecimalField(**POINT_KWARGS)
    end_lat = models.DecimalField(**POINT_KWARGS)
    end_lon = models.DecimalField(**POINT_KWARGS)
    price = models.DecimalField(**MONEY_KWARGS)
    note = models.CharField(max_length=128)
    datetime = models.DateTimeField(auto_now=True)
    car_type = models.CharField(max_length=5, choices=TypeChoices.choices,
                                default=TypeChoices.BASIC)
    car_class = models.CharField(max_length=5, choices=ClassChoices.choices,
                                 default=ClassChoices.BASIC)

    @property
    def start_point(self):
        return (self.start_lat.__str__(), self.start_lon.__str__())
    
    @property
    def end_point(self):
        return (self.end_lat.__str__(), self.end_lon.__str__())

    @property
    def is_completed(self):
        # TODO: To end
        return False

    @property
    def wait_time(self):
        # TODO: To end
        return 0
