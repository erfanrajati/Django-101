# Generated by Django 5.1.4 on 2025-02-10 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='N/A', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
