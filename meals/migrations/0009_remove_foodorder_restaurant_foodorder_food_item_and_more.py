# Generated by Django 5.0.2 on 2024-03-28 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0008_fooditem_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodorder',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='foodorder',
            name='food_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='food_orders', to='meals.fooditem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodorder',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
