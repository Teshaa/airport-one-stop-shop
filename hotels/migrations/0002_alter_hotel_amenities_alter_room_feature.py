# Generated by Django 5.0.2 on 2024-02-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='amenities',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='feature',
            field=models.JSONField(),
        ),
    ]
