# Generated by Django 3.0.5 on 2020-05-01 02:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200428_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patientInsurance',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patientPhone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patientSSN',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')]),
        ),
    ]
