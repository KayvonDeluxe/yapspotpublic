# Generated by Django 3.0.6 on 2020-05-26 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yap', '0008_event_time_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
    ]
