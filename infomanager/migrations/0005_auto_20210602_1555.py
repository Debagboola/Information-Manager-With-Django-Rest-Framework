# Generated by Django 3.1.2 on 2021-06-02 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infomanager', '0004_auto_20210602_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
