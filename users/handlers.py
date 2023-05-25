from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.dispatch import receiver

from accounts.models import Account


@receiver(post_save, sender=get_user_model())
def post_user_save(sender, instance, created, **kwargs):
    if created:
        add_default_account(instance)


def add_default_account(user):
    group = Group.objects.first()
    Account.objects.create(
        user=user,
        group=group
    )
