from datetime import datetime
from django.db import models

from accounts.models import Driver


class TypeChoices(models.TextChoices):
    BASIC = 'B', 'Basic'
    VAN = 'V', 'Van'
    OFF_ROAD = 'OR', 'Off-Road'


class ClassChoices(models.TextChoices):
    BASIC = 'B', 'Basic'
    UPPER = 'U', 'Upper'
    LUXURY = 'L', 'Luxury'


class ColorChoices(models.TextChoices):
    RED = 'R', 'Red'
    ORANGE = 'OR', 'Orange'
    YELLOW = 'YL', 'Yellow'
    GREEN = 'GRE', 'Green'
    BLUE = 'BLU', 'Blue'
    VIOLET = 'VL', 'Violet'
    BLACK = 'BLA', 'Black'
    GRAY = 'GRY', 'Gray'
    WHITE = 'WH', 'White'


YEAR_CHOICES = [(y, y) for y in range(1980, datetime.now().year)]


class Car(models.Model):
    number = models.CharField(max_length=12, unique=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE,
                               related_name='cars')
    brand = models.CharField(max_length=32, blank=False)
    model = models.CharField(max_length=32, blank=False)
    type = models.CharField(max_length=5, choices=TypeChoices.choices,
                            blank=False)
    year = models.IntegerField(choices=YEAR_CHOICES, null=False)
    _class = models.CharField(verbose_name='class', max_length=5,
                              choices=ClassChoices.choices, blank=False)
    color = models.CharField(max_length=5, choices=ColorChoices.choices,
                             blank=False)

    @property
    def full_name(self):
        return f'{self.color} {self.brand} {self.model}'

    def __str__(self) -> str:
        return self.full_name
