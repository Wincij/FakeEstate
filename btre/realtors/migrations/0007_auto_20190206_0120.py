# Generated by Django 2.1.1 on 2019-02-06 01:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0006_auto_20190206_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 6, 1, 20, 34, 45034)),
        ),
    ]
