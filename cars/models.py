from django.db import models


class CarTypeChoices(models.TextChoices):
    BASIC = 'B', 'Basic'
    VAN = 'V', 'Van'
    OFF_ROAD = 'OR', 'Off-Road'


class CarClassChoices(models.TextChoices):
    BASIC = 'B', 'Basic'
    UPPER = 'U', 'Upper'
    LUXURY = 'L', 'Luxury'
