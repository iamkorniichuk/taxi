from django.contrib.gis.db import models
from geopy.geocoders import Nominatim

from accounts.models import Customer
from cars.models import TypeChoices, ClassChoices


geolocator = Nominatim(user_agent='taxi')

MONEY_KWARGS = {
    'max_digits': 10,
    'decimal_places': 2
}


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE,
                                 related_name='orders')
    _stops = models.MultiPointField()
    price = models.DecimalField(**MONEY_KWARGS)
    note = models.TextField(max_length=128, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    car_type = models.CharField(max_length=5, choices=TypeChoices.choices,
                                default=TypeChoices.BASIC)
    car_class = models.CharField(max_length=5, choices=ClassChoices.choices,
                                 default=ClassChoices.BASIC)

    @property
    def is_open(self):
        return not hasattr(self, 'trip')

    def set_stops(self, value):
        self._stops = value

    def get_stops(self):
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
