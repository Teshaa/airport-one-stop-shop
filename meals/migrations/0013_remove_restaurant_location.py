# Generated by Django 5.0.2 on 2024-03-31 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0012_alter_foodorder_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='location',
        ),
    ]
