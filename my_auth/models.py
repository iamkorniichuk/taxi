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
    image = models.ImageField(upload_to='images/', default='default.png',
                              null=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __is_employee__(self, employee_model: models.Model) -> bool:
        return employee_model.objects.filter(customer=self.customer).first() != None

    @property
    def is_driver(self):
        from accounts.models import Driver
        return self.__is_employee__(Driver)

    @property
    def is_manager(self):
        from accounts.models import MyManager
        return self.__is_employee__(MyManager)

    @property
    def is_director(self):
        from accounts.models import MyDirector
        return self.__is_employee__(MyDirector)

    def __str__(self) -> str:
        return self.phone if self.full_name.isspace() else self.full_name
