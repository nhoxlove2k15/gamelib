# Generated by Django 3.2.6 on 2021-10-08 13:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelib', '0011_alter_rating_rateeee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rateeee',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
    ]
