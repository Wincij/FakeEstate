# Generated by Django 2.1.1 on 2019-02-06 00:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_auto_20190205_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='hire_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 5, 23, 59, 58, 502541)),
        ),
    ]
