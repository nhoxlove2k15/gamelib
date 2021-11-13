# views.py

import json,datetime
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, viewsets,filters
from django_filters import *


from gamelib.models import Game, Rating, Requirement
from rest_framework import generics,filters



# game = Game.objects.get(pk=1)
# categories = game.categories.all()
# print(game.name + "" )
# for i in range(len(categories)):
#     print(categories[i].name)
# from django_filters.rest_framework import DjangoFilterBackend
# class GameList(generics.ListAPIView):
#     queryset = Game.objects.all()
#     serializer_class = GetGameSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['categories']
import django_filters

from gamelib.serializers import GetGameSerializer
# search
class GameEngineSearchByCategory(django_filters.FilterSet):
    ids = django_filters.Filter(field_name='categories',lookup_expr='in')
    filter_backends = [filters.OrderingFilter]
    class Meta:
        model = Game
        fields = ['id','name']
#search category
class GameSearchByCategory(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GetGameSerializer
    filter_class = GameEngineSearchByCategory


class GameFilterByDate(generics.ListAPIView):
    serializer_class = GetGameSerializer
    def get_queryset(self):   
        mindate = self.request.query_params.get('min_date')
        maxdate = self.request.query_params.get('max_date')
        if mindate is None :
            queryset = Game.objects.filter(release_date__lte = maxdate)
        if maxdate is None :
            queryset = Game.objects.filter(release_date__gte = mindate)
        if maxdate is not None and mindate is not None:
            # queryset = queryset.filter(game__id is1)
            queryset = Game.objects.filter(release_date__lte = maxdate).filter(release_date__gte = mindate)
        return queryset


# sort name & release_date
class GameSortByNameAndDate(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GetGameSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name','release_date']
# search name
#      
class GameSearchByName(generics.ListAPIView):
    print(Game.objects.all())
    search_fields = ['name','publisher','description']
    filter_backends = (filters.SearchFilter,)
    queryset = Game.objects.all()

    serializer_class = GetGameSerializer

# rating


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.filter(pk=4)
    serializer_class = GetGameSerializer
# class RequirementViewSet(viewsets.ModelViewSet):
#     queryset = Requirement.objects.filter(pk=1)
#     serializer_class = RequirementSerializer
class GameLatest(viewsets.ModelViewSet):
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
      
class GamePopular(viewsets.ModelViewSet) :
    serializer_class = GetGameSerializer
    queryset = query_popular_game()    
    
