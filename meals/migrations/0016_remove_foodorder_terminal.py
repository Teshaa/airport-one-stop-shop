# Generated by Django 5.0.2 on 2024-04-19 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0015_restaurant_address_restaurant_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodorder',
            name='terminal',
        ),
    ]