from django.db import models

# Create your models here.

class Product(models.Model):
    # Attributes
    title = models.CharField(max_length=150)
    price = models.IntegerField()