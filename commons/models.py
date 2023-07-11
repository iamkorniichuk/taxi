from django.core.exceptions import PermissionDenied
from django.db.models import DecimalField, Model


class MoneyField(DecimalField):
    def __init__(self, *args, **kwargs):
        kwargs["max_digits"] = 10
        kwargs["decimal_places"] = 2
        super().__init__(*args, **kwargs)


class UserRelatedModel(Model):
    class Meta:
        abstract = True

    def has_user_in_field(self, user, field, is_safe=True):
        has_user = getattr(self, field) == user
        if is_safe or has_user:
            return has_user
        raise PermissionDenied

    def has_user_in_any_field(self, user, fields, is_safe=True):
        return any(self.has_user_in_field(user, field, is_safe) for field in fields)
