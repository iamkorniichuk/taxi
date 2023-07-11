# Generated by Django 4.2.2 on 2023-07-10 11:46

import commons.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_datetime", models.DateTimeField(auto_now_add=True)),
                ("complete_datetime", models.DateTimeField(null=True)),
                (
                    "rating",
                    models.PositiveSmallIntegerField(
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                (
                    "tip",
                    commons.models.MoneyField(
                        decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "driver",
                    models.ForeignKey(
                        limit_choices_to={"groups__name": "driver"},
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trips",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "order",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="trip",
                        to="orders.order",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]