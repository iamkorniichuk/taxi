from django.db import models
from django.contrib.auth.models import Group

from taxi.settings import LOGIN_URL


def add_group_model_fields():
    Group.add_to_class('home_url', models.URLField(
        max_length=30, default=LOGIN_URL))


add_group_model_fields()
