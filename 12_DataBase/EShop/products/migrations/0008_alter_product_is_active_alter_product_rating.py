# Generated by Django 5.1.4 on 2025-02-09 19:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=None, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
