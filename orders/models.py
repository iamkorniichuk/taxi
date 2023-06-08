from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.db.models import ExpressionWrapper, Exists, OuterRef

from commons.models import MoneyField, UserRelatedModel

from cars.models import TypeChoices, ClassChoices

from .apps import APP_NAME


# class Stop(models.Model):
#     country = models.CharField(max_length=100, default='Ukraine', null=False)
#     city = models.CharField(max_length=100, null=False)
#     street = models.CharField(max_length=150, null=False)
#     building = models.CharField(max_length=50, null=False)


class OrderManager(models.Manager):
    def get_queryset(self):
        from trips.models import Trip

        return super().get_queryset().annotate(
            is_open=ExpressionWrapper(
                ~Exists(
                    Trip.objects.filter(order=OuterRef('pk'))
                ), output_field=models.BooleanField()
            )
        )


class Order(UserRelatedModel):
    customer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                 related_name='orders', limit_choices_to={'groups__name': 'customer'})
    start = models.CharField(max_length=300, blank=False)
    end = models.CharField(max_length=300, blank=False)
    price = MoneyField()
    note = models.TextField(max_length=128, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    car_type = models.CharField(max_length=5, choices=TypeChoices.choices,
                                default=TypeChoices.BASIC)
    car_class = models.CharField(max_length=5, choices=ClassChoices.choices,
                                 default=ClassChoices.BASIC)

    objects = OrderManager()

    class Meta:
        permissions = [
            ('accept_order', 'User can accept any open order')
        ]

    def get_absolute_url(self):
        return reverse(APP_NAME + ':detail', kwargs={'pk': self.pk})

    def __str__(self) -> str:
        return self.pk.__str__()
