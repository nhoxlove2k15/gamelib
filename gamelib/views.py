

# Create your views here.
import json


from django.http.response import  JsonResponse
from gamelib.models import *


from django.http import JsonResponse
from django.core import serializers
from gamelib.serializers import *

from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework import viewsets
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class ListCreateGameView(ListCreateAPIView):
#     model = Game
#     serializer_class = GameSerializer

#     def get_queryset(self):
#         return Game.objects.all()

#     def create(self, request, *args, **kwargs):
#         serializer = GameSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return JsonResponse({
#                 'message': 'Create a new Car successful!'
#             }, status=status.HTTP_201_CREATED)

#         return JsonResponse({
#             'message': 'Create a new Car unsuccessful!'
#         }, status=status.HTTP_400_BAD_REQUEST)

# class UpdateDeleteGameView(RetrieveUpdateDestroyAPIView):
#     model = Game
#     serializer_class = GameSerializer

#     def put(self, request, *args, **kwargs):
#         query.QuerySet = get_object_or_404(Game, id=kwargs.get('pk'))
#         serializer = GameSerializer(post, data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return JsonResponse({
#                 'message': 'Update Car successful!'
#             }, status=status.HTTP_200_OK)

#         return JsonResponse({
#             'message': 'Update Car unsuccessful!'
#         }, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, *args, **kwargs):
#         car = get_object_or_404(Game, id=kwargs.get('pk'))
#         car.delete()

#         return JsonResponse({
#             'message': 'Delete Car successful!'
#         }, status=status.HTTP_200_OK)

def get_game_popular(request) :
    
    # result = Game.objects.values('')
    #                     .order_by('author')
    #                     .annotate(total_price=Sum('price'))
    # popular_games = Game.objects.extra(
    # select={'rate': 'gamelib_rating.rate'},    
    # tables=['gamelib_rating'],
    # where=['gamelib_rating.game_id_id=gamelib_game.id']
    # )
    #popular_games = Rating.objects.values('game_id__id').annotate(Avg('game_id'))
    
    #SELECT ID, (SELECT SUM(A) FROM UNNEST(MY_COLUMN) AS A) AS TOTAL FROM MY_TABLE;
    popular_games = Rating.objects.raw("SELECT  1 as id , game_id_id , (SELECT SUM(s) FROM UNNEST(rate) s) as total_usage from gamelib_rating ")
    #popular_games = Rating.objects.raw("SELECT  1 as id , game_id_id ,  SUM(rate)  as total_usage  from gamelib_rating GROUP BY game_id_id ")
    #popular_games = Rating.objects.raw("SELECT  1 as id , game_id_id ,  (SUM(s) FROM UNNEST(rate) s as total_usage)  from gamelib_rating GROUP BY game_id_id ")
    print("len : " , len(popular_games))
    print(type(popular_games))
    games_id = []
    rates = []
    games_dict = {}
    for i in range(len(popular_games)) :
        games_id.append(popular_games[i].game_id_id) 
        rates.append(popular_games[i].total_usage/5)
    print('game : ' , games_id) 
    print('rate',rates)
    for i in range(len(games_id)):
        break_points = 0
        
        if i == len(games_id) - 1 or games_id[i] != games_id[i+1]:
            break_points = i + 1
            games_dict[games_id[i]] = sum(rates[:break_points])/len(rates[:break_points])
            rates = rates[break_points:]
            
    print(games_dict)
    data = {}
    gameess=[]
    count = 1 
    for key in games_dict.keys() :
        if games_dict[key] > 5.0 :
            game = Game.objects.get(pk=key)
            game = serializers.serialize('json',game)
           
            gameess.append(game)

    print(type(gameess))
    data["message"] = "get popular game with rating > 5.0"
    data["status"] = "true"

    data["data"] = gameess
    
    return JsonResponse(data , safe=False)
