from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import RegexValidator


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **kwargs):
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password=None, **kwargs):
        user = self.create_user(phone, password, **kwargs)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(unique=True, null=False, max_length=10,
                             validators=[RegexValidator(r'^0\d{9}$')])
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(default='default.png', null=False)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = 'phone'

    @property
    def full_name(self):
        result = ' '.join([self.first_name, self.last_name])
        if result.isspace():
            result = f'User #{self.pk}'
        return result

    def __str__(self) -> str:
        return self.full_name

    @property
    def drives(self):
        return self.trips.filter(driver=self)

    @property
    def completed_drives(self):
        return self.drives.exclude(complete_datetime__isnull=True)

    @property
    def rated_drives(self):
        return self.completed_drives.exclude(rating__isnull=True)

    @property
    def rating(self) -> float:
        return self.rated_drives.aggregate(models.Avg('rating'))['rating__avg']

    @property
    def recent_trips(self):
        return self.trips.order_by('-start_datetime')[0:3]
