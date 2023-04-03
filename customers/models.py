from django.conf import settings
from django.db import models
from datetime import datetime


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name='customer', primary_key=True)
    join_date = models.DateField(auto_now=True, editable=False)

    @property
    def joined_for(self):
        return datetime.now().date() - self.join_date

    @property
    def rating(self):
        return ''