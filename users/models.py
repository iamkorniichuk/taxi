from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        user = self.create_user(phone, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser):
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

    def has_perm(self, perm: str, obj=None) -> bool:
        if self.is_superuser:
            return True
        
        for group in self.groups:
            if perm in group.permissions.all():
                return True
        return False
    
    def has_module_perms(self, app_label):
        return self.is_superuser

    @property
    def groups(self):
        result = [account.group for account in self.accounts.all()]
        result.sort(key=lambda group: group.pk)
        return result

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self) -> str:
        return self.phone if self.full_name.isspace() else self.full_name
