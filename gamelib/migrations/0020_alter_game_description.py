# Generated by Django 3.2.6 on 2021-10-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamelib', '0019_auto_20211013_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.CharField(max_length=10000),
        ),
    ]