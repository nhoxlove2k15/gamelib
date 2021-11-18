# Generated by Django 3.2.8 on 2021-11-18 12:57

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os', models.CharField(max_length=500)),
                ('storage', models.CharField(max_length=500)),
                ('ram', models.CharField(max_length=500)),
                ('graphic', models.CharField(max_length=500)),
                ('processor', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=500)),
                ('user_name', models.CharField(max_length=500, unique=True)),
                ('pass_word', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 11, 18, 19, 57, 0, 532674), null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('producer', models.CharField(max_length=500)),
                ('publisher', models.CharField(max_length=500)),
                ('home_page', models.CharField(max_length=500)),
                ('release_date', models.DateTimeField(blank=None, null=None)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), size=None)),
                ('categories', models.ManyToManyField(to='gamelib.Category')),
                ('requirement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requirements', to='gamelib.requirement')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 11, 18, 19, 57, 0, 534719), null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelib.game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelib.user')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelib.game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelib.user')),
            ],
            options={
                'unique_together': {('user_id', 'game_id')},
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2021, 11, 18, 19, 57, 0, 534719), null=True)),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelib.game')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamelib.user')),
            ],
            options={
                'unique_together': {('user_id', 'game_id')},
            },
        ),
    ]
