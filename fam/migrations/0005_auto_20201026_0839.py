# Generated by Django 3.1.1 on 2020-10-26 03:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fam', '0004_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
