# Generated by Django 3.0.5 on 2020-05-01 02:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0014_auto_20200428_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 1, 2, 14, 28, 570647, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='report',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 1, 2, 14, 28, 570625, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='report',
            name='user',
            field=models.ForeignKey(limit_choices_to={'groups': 1}, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]