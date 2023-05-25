from django.db.models.signals import post_migrate
from django.apps import AppConfig

from .settings import DEFAULT_GROUPS


def __create_group__(name, permissions, **kwargs):
    from django.contrib.auth.models import Group
    obj, created = Group.objects.get_or_create(
        name=name,
        **kwargs
    )
    obj.permissions.set(permissions)


def create_default_groups(sender, **kwargs):
    for group in DEFAULT_GROUPS:
        __create_group__(**group)


class GroupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'groups'

    def ready(self):
        post_migrate.connect(create_default_groups, sender=self)

        return super().ready()
