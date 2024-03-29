# Generated by Django 5.0.2 on 2024-03-23 17:22

import taggit.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_alter_room_feature'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='amenities',
        ),
        migrations.RemoveField(
            model_name='room',
            name='feature',
        ),
        migrations.AddField(
            model_name='hotel',
            name='amenities',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='room',
            name='feature',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
