# Generated by Django 5.0.2 on 2024-03-28 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0009_remove_foodorder_restaurant_foodorder_food_item_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodorder',
            old_name='total_price',
            new_name='price',
        ),
    ]
