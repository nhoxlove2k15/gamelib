# Generated by Django 3.2.6 on 2021-10-09 09:23

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelib', '0013_rename_rateeee_rating_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), size=None), size=None),
        ),
    ]