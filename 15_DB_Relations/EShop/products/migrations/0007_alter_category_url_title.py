# Generated by Django 5.1.6 on 2025-03-02 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_alter_product_slug_product_categgory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url_title',
            field=models.CharField(max_length=300, null=True, verbose_name='url_title'),
        ),
    ]
