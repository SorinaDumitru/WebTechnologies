from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, first_name, last_name, cnp, phone_number, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must be assigned to is_staff=True'))

        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                _('Superuser must be assigned to is_superuser=True'))

        return self.create_user(email, first_name, last_name, cnp, phone_number, password, **other_fields)

    def create_user(self, email, first_name, last_name, cnp, phone_number, password, **other_fields):
        if not email:
            raise ValueError(_('Please enter an email!'))
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, cnp=cnp, phone_number=phone_number, **other_fields)
        user.set_password(password)
        user.save()

        return user


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(null=False)
    address = models.CharField(max_length=100)
    cnp = models.CharField(max_length=13)
    phone_number = models.CharField(max_length=15, null=False)
    registered_date = models.DateTimeField(default=timezone.now)

    is_doctor = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    # change is_active to true if you don't want email validation
    is_active = models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'birthday', 'address', 'cnp', 'phone_number']

    def __str__(self):
        return self.first_name + " " + self.last_name
