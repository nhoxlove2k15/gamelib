from datetime import datetime
from typing import Tuple
from django.db.models import query
from django.db.models.base import Model
from rest_framework import serializers

from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'user_name', 'full_name')


class GameSearializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class RequirementSearializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = '__all__'

class RatingSearializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user_id','game_id','content']

class GetCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CategorySearializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MentorBookingInforSearializer(serializers.Serializer):
    total_ongoing = serializers.IntegerField()
    total_cancel = serializers.IntegerField()
    total_mentee = serializers.IntegerField()

    class Meta:
        fields = ['total_ongoing', 'total_cancel', 'total_mentee']


class CreateUpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class GetGameSerializer(serializers.ModelSerializer):
    requirement_id = RequirementSearializer(read_only=True)
    categories = CategorySearializer(many=True, read_only=True)
    class Meta:
        model = Game
        fields = '__all__'

class GetGameDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Game 
        fields = '__all__'
    


class CreateUpdateRatingSerializer(serializers.ModelSerializer):
    # requirement_id = RequirementSearializer(read_only=True)
    # categories = CategorySearializer(many=True, read_only=True)
    class Meta:
        model = Rating
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
class GetLikeSerializer(serializers.ModelSerializer):
    # requirement_id = RequirementSearializer(read_only=True)
    # categories = CategorySearializer(many=True, read_only=True)
    user_id = UserSerializer(read_only=True)
    game_id = GetGameSerializer(read_only=True)
    class Meta:
        model = Like
        fields = '__all__'
# class GetMentorSerializerTest(serializers.Serializer):
#     mentor = GetMentorSerializer()
#     bookings = MentorBookingInforSearializer()


# class CreateBookingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = ['mentor', 'mentee', 'duration', 'status']


# class BookingMenteeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'email', 'user_name', 'image']


# class BookingMentorSerialzer(serializers.ModelSerializer):
#     user = UserSerializer(read_only=True)

#     class Meta:
#         model = Mentor
#         fields = ['user', 'id', 'full_name', 'thumbnail', 'status']


# class GetBookingSerializer(serializers.ModelSerializer):
#     mentor = BookingMentorSerialzer(read_only=True)
#     mentee = BookingMenteeSerializer(read_only=True)

#     class Meta:
#         model = Booking
#         fields = '__all__'


# class PatchBookingStatusSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Booking
#         fields = ['status']