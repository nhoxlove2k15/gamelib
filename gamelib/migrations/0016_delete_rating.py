# Generated by Django 3.2.6 on 2021-10-09 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamelib', '0015_remove_rating_rate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating',
        ),
    ]