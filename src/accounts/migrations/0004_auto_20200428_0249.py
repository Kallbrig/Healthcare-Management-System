# Generated by Django 3.0.5 on 2020-04-28 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200428_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='nurse',
            name='salary',
            field=models.PositiveIntegerField(),
        ),
    ]