# Generated by Django 2.1.1 on 2019-02-05 23:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 2, 5, 23, 52, 56, 652207)),
        ),
    ]
