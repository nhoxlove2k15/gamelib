# Generated by Django 3.2.6 on 2021-11-12 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelib', '0030_auto_20211112_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 16, 0, 22, 123269), null=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 16, 0, 22, 122266), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 16, 0, 22, 119279), null=True),
        ),
    ]
