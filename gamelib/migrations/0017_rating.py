# Generated by Django 3.2.6 on 2021-10-09 09:31

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamelib', '0016_delete_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelib.game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelib.user')),
            ],
        ),
    ]
