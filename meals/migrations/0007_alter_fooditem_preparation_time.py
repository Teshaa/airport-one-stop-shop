# Generated by Django 5.0.2 on 2024-03-23 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0006_foodtype_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='preparation_time',
            field=models.IntegerField(blank=True, help_text='Estimated time in minutes to prepare the food item', null=True),
        ),
    ]
