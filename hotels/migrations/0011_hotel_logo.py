# Generated by Django 5.0.2 on 2024-04-13 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0010_rename_days_reservation_nights_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='logo',
            field=models.ImageField(default='logo.png', upload_to='hotels/logos'),
            preserve_default=False,
        ),
    ]
