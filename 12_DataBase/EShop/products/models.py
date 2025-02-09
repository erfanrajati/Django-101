from django.db import models

# Create your models here.

class Product(models.Model):
    # Attributes
    title = models.CharField(max_length=150)
    price = models.IntegerField()

    # Overriding __str__ method
    def __str__(self):
        return f"{self.title} {self.price}"