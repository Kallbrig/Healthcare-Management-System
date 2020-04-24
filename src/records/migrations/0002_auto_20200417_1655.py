# Generated by Django 3.0.5 on 2020-04-17 16:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='height_feet',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')], default=0),
        ),
        migrations.AlterField(
            model_name='record',
            name='appointment_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='record',
            name='appointment_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
