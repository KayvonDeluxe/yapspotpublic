# Generated by Django 3.0.6 on 2020-05-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yap', '0005_auto_20200524_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_videochat_room_name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
