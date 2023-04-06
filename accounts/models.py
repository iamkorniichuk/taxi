from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime


class Profile(models.Model):
    class Meta:
        abstract = True

    join_date = models.DateField(auto_now=True, editable=False)

    @property
    def joined_for(self):
        return (datetime.now().date() - self.join_date).days


class Customer(Profile):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                related_name='customer', primary_key=True)

    def __str__(self) -> str:
        return self.user.__str__()

class Employee(Profile):
    class Meta:
        abstract = True

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)
    job_title = models.CharField(max_length=100, default='%(class)s',
                                blank=False, null=False)


class MyDirector(Employee):
    class Meta:
        default_related_name = 'director'
        verbose_name = default_related_name
        verbose_name_plural = default_related_name + 's'


class MyManager(Employee):
    director = models.ForeignKey(MyDirector, on_delete=models.RESTRICT,
                                 related_name='managers')

    class Meta:
        default_related_name = 'manager'
        verbose_name = default_related_name
        verbose_name_plural = default_related_name + 's'


class Driver(Employee):
    manager = models.ForeignKey(MyManager, on_delete=models.RESTRICT,
                                related_name='drivers')

    class Meta:
        default_related_name = 'driver'

    @property
    def rating(self):
        return ''
