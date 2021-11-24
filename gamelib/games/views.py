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
from gamelib.serializers import  GetCommentSerializer, GetGameDetailSerializer, GetGameHomePageSerializer,GetGameDetailSerializer ,GetGameHomePageSerializer, GetGameSerializer, RatingSearializer

limit = 5 


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
class GameHomePage(generics.GenericAPIView):
    serializers = GetGameHomePageSerializer
    def get(self, request, *args,**kwargs):
        game_hanh_dong = Game.objects.filter(categories__id = 1 )
        serializer_game_hanh_dong = GetGameHomePageSerializer(game_hanh_dong , many=True)
        # "hành động", #1
        # "bắn súng", #2
        # "phiêu lưu", #3
        # "sinh tồn",#4
        # "thể thao",#5
        # "đối kháng",#6
        # "chiến thuật",#7
        # "kinh dị",#8
        # "nhập vai",#9
        # "offline", #10
        # "online",#11
        # "mô phỏng"#12
        game_ban_sung = Game.objects.filter(categories__id = 2 )
        serializer_game_ban_sung= GetGameHomePageSerializer(game_ban_sung , many=True)

        game_phieu_luu = Game.objects.filter(categories__id = 3 )
        serializer_game_phieu_luu= GetGameHomePageSerializer(game_phieu_luu , many=True)

        game_sinh_ton = Game.objects.filter(categories__id = 4 )
        serializer_game_sinh_ton= GetGameHomePageSerializer(game_sinh_ton , many=True)

        game_the_thao = Game.objects.filter(categories__id = 5 )
        serializer_game_the_thao = GetGameHomePageSerializer(game_the_thao , many=True)

        game_doi_khang = Game.objects.filter(categories__id = 6 )
        serializer_game_doi_khang = GetGameHomePageSerializer(game_doi_khang , many=True)

        game_chien_thuat = Game.objects.filter(categories__id = 7 )
        serializer_game_chien_thuat = GetGameHomePageSerializer(game_chien_thuat , many=True)

        game_kinh_di = Game.objects.filter(categories__id = 8 )
        serializer_game_kinh_di = GetGameHomePageSerializer(game_kinh_di , many=True)

        game_nhap_vai = Game.objects.filter(categories__id = 9 )
        serializer_game_nhap_vai = GetGameHomePageSerializer(game_nhap_vai , many=True)

        game_offline = Game.objects.filter(categories__id = 10 )
        serializer_game_offline = GetGameHomePageSerializer(game_offline , many=True)
        game_online = Game.objects.filter(categories__id = 11 )
        serializer_game_online = GetGameHomePageSerializer(game_online , many=True)

        game_mo_phong = Game.objects.filter(categories__id = 12 )
        serializer_game_mo_phong = GetGameHomePageSerializer(game_mo_phong , many=True)

        game_latest = Game.objects.all().order_by('-release_date')[:limit]
        serializer_game_latest = GetGameHomePageSerializer(game_latest, many=True)

        game_popular = query_popular_game()
        serializer_game_popular = GetGameHomePageSerializer(game_popular, many=True)

        

        return JsonResponse({
            'game_latest': serializer_game_latest.data ,
            'game_popular':serializer_game_popular.data,

            'game_hanh_dong' : serializer_game_hanh_dong.data,
            'game_ban_sung' : serializer_game_ban_sung.data,
            'game_phieu_luu' : serializer_game_phieu_luu.data,
            'game_sinh_ton' : serializer_game_sinh_ton.data,
            'game_the_thao' : serializer_game_the_thao.data,
            'game_doi_khang' : serializer_game_doi_khang.data,
            'game_chien_thuat' : serializer_game_chien_thuat.data,
            'game_kinh_di' : serializer_game_kinh_di.data,
            'game_nhap_vai' : serializer_game_nhap_vai.data,
            'game_offline' : serializer_game_offline.data,
            'game_online' : serializer_game_online.data,
            'game_mo_phong' : serializer_game_mo_phong.data,
            




        })

# game = Game.objects.get(pk=1)
# categories = game.categories.all()
# print(game.name + "" )
# for i in range(len(categories)):
#     print(categories[i].name)

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
    try:
        print("successfully!")
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
            if games_dict[key] > 3.0 :
                gameess.append(key)
        #queryset 

        
        queryset = Game.objects.filter(id__in=gameess)
        
        return queryset 
    except:
        print("error!") 
class GamePopular(generics.ListAPIView) :
    serializer_class = GetGameSerializer
    queryset = query_popular_game()   
    #query = Game.objects.all()
    
