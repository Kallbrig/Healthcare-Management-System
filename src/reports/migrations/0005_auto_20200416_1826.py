# Generated by Django 3.0.5 on 2020-04-16 23:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0004_auto_20200411_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 16, 23, 26, 9, 146479, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='report',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 4, 16, 23, 26, 9, 146479, tzinfo=utc)),
        ),
    ]
