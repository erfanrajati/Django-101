from django.db import models
from django.utils.text import slugify
import string, random

# Create your models here.
class Product(models.Model):
    name = models.CharField(default="N/A", max_length=100, blank=False)
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(default="", unique=True, blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        base_slug = slugify(self.name)
        chars = string.ascii_letters
        guess = base_slug
        existing_slugs = set(
            Product.objects.filter(slug__startswith=base_slug)
            .values_list("slug", flat=True)
        )
        while guess in existing_slugs:
            salt = ''.join(random.choices(chars, k=3))
            guess = base_slug + salt
        
        self.slug = guess
        super().save(*args, **kwargs)