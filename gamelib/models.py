from datetime import time
import datetime
import json
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.postgres.fields import ArrayField

# Create your models here.
len_medium = 50 
len_medium = 500
len_max = 10000
class User(models.Model):
    full_name = models.CharField(max_length=len_medium)
    user_name = models.CharField(max_length=len_medium , unique=True)
    pass_word = models.CharField(max_length=len_medium)
    created_at = models.DateTimeField(null=True , default=datetime.datetime.now())
class Requirement(models.Model):
    os = models.CharField(max_length=len_medium)
    storage = models.CharField(max_length=len_medium)
    ram = models.CharField(max_length=len_medium)
    graphic = models.CharField(max_length=len_medium)
    processor = models.CharField(max_length=len_medium)

class Category(models.Model):
    name = models.CharField(max_length=len_medium)
class Game(models.Model):
    name = models.CharField(max_length=len_medium)
    description = models.CharField(max_length=len_max)
    producer = models.CharField(max_length=len_medium)
    publisher = models.CharField(max_length=len_medium)
    home_page = models.CharField(max_length=len_medium)
    requirement_id = ForeignKey(Requirement , on_delete=models.CASCADE , related_name='requirements' )
    release_date = models.DateTimeField(blank=None,null=None)
    images = ArrayField(models.CharField(max_length=len_medium))
    categories = models.ManyToManyField(Category)
    


class Like(models.Model) :
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True , default=datetime.datetime.now())
    class Meta:
        unique_together = [['user_id', 'game_id']]

class Comment(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.CharField(max_length=len_medium)
    created_at = models.DateTimeField(null=True , default=datetime.datetime.now())

class Rating(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    rate = ArrayField(models.IntegerField())
    class Meta:
        unique_together = [['user_id', 'game_id']]
   
