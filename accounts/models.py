from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime


class Profile(models.Model):
    class Meta:
        abstract = True
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,primary_key=True)

    join_date = models.DateField(auto_now=True, editable=False)

    @property
    def joined_for(self):
        return (datetime.now().date() - self.join_date).days

    def __str__(self) -> str:
        return self.user.__str__()


class Customer(Profile):
    class Meta:
        default_related_name = 'customer'
        verbose_name = default_related_name
        verbose_name_plural = default_related_name + 's'


class Employee(Profile):
    class Meta:
        abstract = True

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE,
                                primary_key=True)
    job_title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return self.user.__str__()


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

    @property
    def rating(self):
        return ''
