from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        user: User = self.model(phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None):
        user: User = self.create_user(phone, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(unique=True, null=False, max_length=10,
                             validators=[RegexValidator(r'^0\d{9}$')])
    password = models.CharField(max_length=128)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(default='default.png', null=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'

    def __init__(self, *args, **kwargs):
        '''Instance attributes created according to default_related_name of account's constant ROLES'''
        from accounts.models import ROLES
        for role in ROLES:
            setattr(self, f'is_{role.model_name}',
                    lambda: self.__is_related__(role))
        super().__init__(*args, **kwargs)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __is_related__(self, model: models.Model) -> bool:
        return model.objects.filter(user=self).first() != None

    def __str__(self) -> str:
        return self.phone if self.full_name.isspace() else self.full_name
