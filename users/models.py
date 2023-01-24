from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    middle_name = models.CharField(max_length=35, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(unique=True)
