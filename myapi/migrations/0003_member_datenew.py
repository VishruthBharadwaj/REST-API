# Generated by Django 3.0.3 on 2020-05-05 05:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_auto_20200505_1035'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='datenew',
            field=models.DateField(default=datetime.datetime(2020, 5, 5, 10, 56, 56, 431775), verbose_name='%d-%m-%Y'),
        ),
    ]
