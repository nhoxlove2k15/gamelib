# views.py

import hashlib
import json,datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, status, viewsets,filters
from django_filters import *
from rest_framework.response import Response
from rest_framework.schemas import coreapi, openapi
from rest_framework_simplejwt.tokens import RefreshToken


from gamelib.models import Comment, Game, Like, Rating, Requirement, User
from rest_framework import generics,filters

import django_filters

from gamelib.serializers import CommentSerializer, GetCommentSerializer, GetGameSerializer, GetLikeSerializer, LikeSerializer, RatingSearializer, UserSerializer


# search
class GameEngineSearchByCategory(django_filters.FilterSet):
    tag = django_filters.Filter(field_name='categories',lookup_expr='in')
    filter_backends = [filters.OrderingFilter]
    class Meta:
        model = Game
        fields = []
#search category
class GameSearchByCategory(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GetGameSerializer
    filter_class = GameEngineSearchByCategory

class GameEngineFilterByDate(django_filters.FilterSet):
    min_date = django_filters.Filter(field_name='release_date' ,lookup_expr='gte')
    max_date = django_filters.Filter(field_name='release_date' , lookup_expr='lte')
    class Meta:
        model = Game 
        fields = []
class GameFilterByDate(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class=GetGameSerializer
    filter_class = GameEngineFilterByDate

# sort name & release_date
class GameSortByNameAndDate(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GetGameSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name','release_date']
# search name
#      
class GameSearchByName(generics.ListAPIView):
    
    search_fields = ['name','publisher','description']
    filter_backends = (filters.SearchFilter,)
    queryset = Game.objects.all()
    serializer_class = GetGameSerializer

class GameDetailEngine(generics.GenericAPIView):
    serializer_class = GetGameSerializer
    def get(self, request, *args,**kwargs):
        game_id = request.path[request.path.rfind('/') + 1: ]
        print("hello:" , game_id )
        
        game = Game.objects.filter(pk=game_id)
        serializer_game = GetGameSerializer(game , many=True)
        comments = Comment.objects.filter(game_id=game_id)
        serializer_comment = GetCommentSerializer(comments,many=True)
        rates = Rating.objects.filter(game_id=game_id)
        serializer_rate = RatingSearializer(rates,many=True)
        #print(type(serializer_rate.data))
        a = serializer_rate.data
        b = []
        for i in range(len(a)):
            b.append(a[i]['rate'])
        v = [sum(x) for x in zip(*b)]
        if len(v) != 0 :
            rate = {
                'story':v[0],
                'gameplay':v[1],
                'sound':v[2],
                'graphic':v[3],
                'overall':v[4]
            }
        else :
            rate =[]
        print(type(rate))
        return JsonResponse({
            'game' : serializer_game.data,
            'comment':serializer_comment.data,
            'rate' : rate
        })

    
class GameLatest(generics.ListAPIView):
    queryset = Game.objects.all().order_by('-release_date')[:5]
    serializer_class = GetGameSerializer

def query_popular_game():
    popular_games = Rating.objects.raw("SELECT  1 as id , game_id_id , (SELECT SUM(s) FROM UNNEST(rate) s) as total_usage from gamelib_rating ")
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
            if(len(rates[:break_points]) == 0 ) :
                games_dict[games_id[i]] = sum(rates[:break_points])/1
            else :
                games_dict[games_id[i]] = sum(rates[:break_points])/len(rates[:break_points])

            rates = rates[break_points:]
            
    print(games_dict)
    data = {}
    gameess=[]
    count = 1 
    for key in games_dict.keys() :
        if games_dict[key] > 5.0 :
            gameess.append(key)
    #queryset 

    
    queryset = Game.objects.filter(id__in=gameess)
    
    return queryset
      
class GamePopular(generics.ListAPIView) :
    serializer_class = GetGameSerializer
    queryset = query_popular_game()    
    
