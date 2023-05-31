from django.db.models.signals import post_migrate
from django.apps import AppConfig

from .settings import DEFAULT_GROUPS


def create_group(name, permissions, **kwargs):
    from django.contrib.auth.models import Group
    obj, created = Group.objects.update_or_create(
        name=name,
        defaults=kwargs
    )

    for permission in permissions:
        obj.permissions.add(get_perm_pk(permission))


def get_perm_pk(name) -> int:
    from django.contrib.auth.models import Permission
    return Permission.objects.get(codename=name).pk


def create_default_groups(sender, **kwargs):
    for group in DEFAULT_GROUPS:
        create_group(**group)


class GroupsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'groups'

    def ready(self):
        post_migrate.connect(create_default_groups, sender=self)

        return super().ready()
