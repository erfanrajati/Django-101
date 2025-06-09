from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=15, null=True, blank=True)
    activation = models.CharField(max_length=100)

    def __str__(self):
        return self.get_full_name()