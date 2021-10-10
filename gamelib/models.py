from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class User(models.Model):
    full_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50 , unique=True)
    pass_word = models.CharField(max_length=50)
    created_at = models.DateTimeField()
class Requirement(models.Model):
    os = models.CharField(max_length=500)
    storage = models.CharField(max_length=500)
    ram = models.CharField(max_length=500)
    graphic = models.CharField(max_length=750)
    processor = models.CharField(max_length=750)
class Game(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1500)
    producer = models.CharField(max_length=500)
    publisher = models.CharField(max_length=500)
    home_page = models.CharField(max_length=750)
    requirement_id = ForeignKey(Requirement , on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    images = ArrayField(ArrayField(models.CharField(max_length=1000)))

class Category(models.Model):
    name = models.CharField(max_length=250)
    
class Game_Category(models.Model):
    game_id = ForeignKey(Game, on_delete=models.CASCADE)
    category_id = ForeignKey(Category,on_delete=models.CASCADE)


class Like(models.Model) :
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

class Comment(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField()

class Rating(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    rate = ArrayField(models.IntegerField())
   
