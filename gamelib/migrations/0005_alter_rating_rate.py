# Generated by Django 3.2.6 on 2021-10-08 12:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelib', '0004_rename_created_date_user_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None), size=None),
        ),
    ]