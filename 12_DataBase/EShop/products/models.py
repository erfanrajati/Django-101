from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Product(models.Model):
    # Attributes
    title = models.CharField(default=None, max_length=150)
    price = models.IntegerField(default=None)
    rating = models.IntegerField(default=None, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
    short_description = models.CharField(default=None, max_length=350, null=True)
    is_active = models.BooleanField(default=True, null=True) # By default, this field is not Nullable, so the default value can't be None either.

    # Overriding __str__ method
    def __str__(self):
        return f"{self.title} {self.price}"
    

