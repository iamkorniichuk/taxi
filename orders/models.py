from django.contrib.gis.db import models


from accounts.models import Customer
from cars.models import TypeChoices, ClassChoices


MONEY_KWARGS = {
    'max_digits': 10,
    'decimal_places': 2
}


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='orders')
    start_point = models.PointField()
    end_point = models.PointField()
    price = models.DecimalField(**MONEY_KWARGS)
    note = models.TextField(max_length=128, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    car_type = models.CharField(max_length=5, choices=TypeChoices.choices,
                                default=TypeChoices.BASIC)
    car_class = models.CharField(max_length=5, choices=ClassChoices.choices,
                                 default=ClassChoices.BASIC)

    @property
    def distance(self):
        return self.start_point.distance(self.end_point) * 100

    def __str__(self) -> str:
        return self.pk.__str__()
