from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .utils import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    full_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'password']

    