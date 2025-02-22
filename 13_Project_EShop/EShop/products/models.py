from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(default="N/A", max_length=100)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(default="", unique=True)

    def __str__(self):
        return f"{self.name}"