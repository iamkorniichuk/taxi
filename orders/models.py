from django.contrib.gis.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

from commons.fields import MoneyField
from commons.geo import geolocator
from cars.models import TypeChoices, ClassChoices

from .apps import APP_NAME


class Order(models.Model):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                 limit_choices_to={'groups__name': 'customer'}, related_name='orders')
    _stops = models.MultiPointField()
    price = MoneyField()
    note = models.TextField(max_length=128, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    car_type = models.CharField(max_length=5, choices=TypeChoices.choices,
                                default=TypeChoices.BASIC)
    car_class = models.CharField(max_length=5, choices=ClassChoices.choices,
                                 default=ClassChoices.BASIC)
    
    def get_absolute_url(self):
        return reverse(APP_NAME + ':detail', kwargs={'pk': self.pk})
    

    @property
    def is_open(self):
        return not hasattr(self, 'trip')

    def set_stops(self, value):
        self._stops = value

    def get_stops(self):
        # TODO: Wrong stops name
        # TODO: Slow loading
        addresses = []
        for stop in self._stops:
            couroutine = geolocator.reverse(stop, language='en', timeout=None)
            if couroutine:
                addresses.append(couroutine.address)
        return addresses

    stops = property(get_stops, set_stops)

    @property
    def distance(self):
        km = 0
        for i in range(1, len(self._stops)):
            km += self._stops[i - 1].distance(self._stops[i]) * 100
        return round(km, 3)

    def __str__(self) -> str:
        return self.pk.__str__()
