#import models Furniture, People, house

from rest_framework import serializers
from gamelib.models import *

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['type'] # if you want all the fields of model than user '__all__'.


class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'