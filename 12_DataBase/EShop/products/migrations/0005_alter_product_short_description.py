# Generated by Django 5.1.4 on 2025-02-09 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_price_alter_product_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(default=None, max_length=350),
        ),
    ]
