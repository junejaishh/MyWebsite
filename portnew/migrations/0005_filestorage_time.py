# Generated by Django 3.1.1 on 2020-09-26 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portnew', '0004_auto_20200926_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='filestorage',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 26, 15, 30, 33, 367191, tzinfo=utc), null=True),
        ),
    ]