from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.dispatch import receiver


@receiver(post_save, sender=get_user_model())
def post_user_save(sender, instance, created, **kwargs):
    if created:
        add_default_group(instance)


def add_default_group(user):
    group = Group.objects.first()
    user.groups.add(group)
