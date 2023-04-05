from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime


class Customer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                related_name='customer', primary_key=True)
    join_date = models.DateField(auto_now=True, editable=False)

    @property
    def joined_for(self):
        return datetime.now().date() - self.join_date

    @property
    def rating(self):
        return ''

    def __str__(self) -> str:
        return self.user.__str__()


class Employee(models.Model):
    related_customer_name = 'employee'
    default_job_title = related_customer_name
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE,
                                    related_name=related_customer_name, primary_key=True)
    join_date = models.DateField(auto_now=True, editable=False)
    job_title = models.CharField(max_length=100, default=default_job_title,
                                 blank=False, null=False)

    @property
    def joined_for(self):
        return datetime.now().date() - self.join_date


class MyDirector(Employee):
    related_customer_name = 'director'

    class Meta:
        verbose_name = 'director'
        verbose_name_plural = 'directors'


class MyManager(Employee):
    related_customer_name = 'manager'
    director = models.ForeignKey(MyDirector, on_delete=models.RESTRICT,
                                 related_name='managers')

    class Meta:
        verbose_name = 'manager'
        verbose_name_plural = 'managers'


class Driver(Employee):
    related_customer_name = 'driver'
    manager = models.ForeignKey(MyManager, on_delete=models.RESTRICT,
                                related_name='drivers')

    @property
    def rating(self):
        return ''
